import sys
from struct import pack, unpack


def F(w):
    return ((w * 31337) ^ (w * 1337 >> 16)) % 2 ** 32


def encrypt(block):
    a, b, c, d = unpack("<4I", block)  # block 16 bit = 2 byte
    for rno in xrange(32):
        a, b, c, d = b ^ F(a | F(c ^ F(d)) ^ F(a | c) ^ d), c ^ F(a ^ F(d) ^ (a | d)), d ^ F(
            a | F(a) ^ a), a ^ 31337  # first stage(num one)
        a, b, c, d = c ^ F(d | F(b ^ F(a)) ^ F(d | b) ^ a), b ^ F(d ^ F(a) ^ (d | a)), a ^ F(
            d | F(d) ^ d), d ^ 1337  # second stage(num two)
    return pack("<4I", a, b, c, d)


pt = open(sys.argv[1]).read()
while len(pt) % 16: pt += "#"

ct = "".join(encrypt(pt[i:i + 16]) for i in xrange(0, len(pt), 16))
print ct
open(sys.argv[1] + ".enc", "w").write(ct)

# P
# ÄþÙŠ Ü®ùŽhqŽ>Þ’¼b	ÀMÀS\›¨j
# FLAG{G3N3R4L123D_F31573L_EZ!}###
