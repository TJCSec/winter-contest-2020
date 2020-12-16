#!/usr/bin/env python3

print("                      `:++:`                      ")
print("                   `-+syyyyso:`                   ")
print("                 -+sssyyyyyyyys+-                 ")
print("              ./syyys+-syys-/syyys/-              ")
print("           ./syyys+-`  ssss   -+ssyys/.           ")
print("        `:oyyyso:`   `-oooo-`   `-+syyyo/.        ")
print("     `:oyyyyo:`    ./oooooooo/-    `:osysyo:`     ")
print("    :syyys/.    ./oooooooooooooo/.    `:syyys/    ")
print("    +yyyyyo:`.:oooooooooooooooooooo:.`:oyyyyyo    ")
print("    /yyysssyyssoooooooooooooooooooossyyyysyyyo    ")
print("    /yyy.`:osyyyssoooooooooooooosssyyys/.`yyy+    ")
print("    /yyy.   ossyyysssoooooooosssyyysso   `yyy+    ")
print("    /yyy.   +oosssyyysssoosssyyysssooo   `yyy+    ")
print("    /yyy.   +ooooosssyyyssyyyyssoooooo   `yyy+    ")
print("    /yyy.`:oooooooooossyyyyssoooooooooo:``yyy+    ")
print("    /yyyosyssoooooooooosyyyoooooooooooyysoyyy+    ")
print("    /yyyyys/../oooooooosyyyoooooooo/../oyyyyy+    ")
print("    :syyys:`    ./ooooosyyyooooo/-    `:syyyy/    ")
print("     `:oyyyso:`   `-/oosyysoo+-`   `-+syyyo/.     ")
print("        ./syyss+-`   `-syys:`    -+syyys/.        ")
print("           ./syyys+-   syys   ./syyys+-           ")
print("              -+syyys/.syys./syyys+-              ")
print("                `-+syyyyyyysyyso:`                ")
print("                   `:osyyyyyo:`                   ")
print("                      `:oo/.                      ")
print("")
print("performing ginkoid magic...")

from Crypto.Util.number import getPrime

flag = int(open("flag.txt", "rb").read().strip().hex(), 16)

p = getPrime(1024)
q = getPrime(1024)
e = 17

n = p * q
c = pow(flag, e, n)

print(f"n: {n}")
print(f"c: {c}")
