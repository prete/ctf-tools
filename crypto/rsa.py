from Crypto.Util.number import inverse

from binascii import unhexlify
p = # p
q = # q
n = p*q # if only given n use factordb to obtain p and q
e = # e 
c = # ciphertext

# solves
d = inverse(e,(p-1)*(q-1))
m = pow(c,d,n)


print(unhexlify(hex(m)[2:]))
