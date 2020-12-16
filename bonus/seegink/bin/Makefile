CFLAGS = -Wno-unused-result -s -pie -fstack-protector -O3 -Wl,-z,relro,-z,now

seegink: seegink.c
	gcc -o $@ $^ $(CFLAGS)
