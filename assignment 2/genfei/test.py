from struct import pack, unpack

def F(w):
    return ((w * 31337) ^ (w * 1337 >> 16)) % 2 ** 32


# 0000 0100 1101 0010  # (1234)
# 0000 0101 0011 1001  # (1337)
# 0111 1010 0110 1001  # (31337)
a, b, c, d = 1, 2, 3, 4
# at first we will unpack the 2 byte block using "<4I" format
# which stands for leaving the first 4 bits as it's and forming the rest in 4 byte

# 5 xor 6 = 3  and 3 xor 6 = 5 and  3 xor 6 = 5 therefor the reverse of xor operation is the same xor
# F() function do xor operation then it's the reverse of itself


##Analysing encryption stage two
# starting of <a>, <b,> <c>, <d> resultant of second stage
a, b, c, d = c ^ F(d | F(b ^ F(a)) ^ F(d | b) ^ a), \
             b ^ F(d ^ F(a) ^ (d | a)), \
             a ^ F(d | F(d) ^ d), \
             d ^ 1337
print(a)
print(b)
print(c)
print(d)
# Second stage decryption #obtain <d> -> <a> -> <b> -> <c> obtained from secand stage
# notice we will use <a>(encrypted version) in obtaining <c> at te end
# but we will over write it when obtaining <a>(decrypted version) itself
# so we store it in tempa

##Decryotion of  stage two
tempa = a
d = d ^ 1337  # 0000 0101 0011 1001
a = c ^ (F(d | F(d) ^ d))
b = b ^ (F(d ^ F(a) ^ (d | a)))
c = tempa ^ (F(d | F(b ^ F(a)) ^ F(d | b) ^ a))
print(a)
print(b)
print(c)
print(d)

##Analysing encryption stage one
# assuming starting of <a>, <b,> <c>, <d> resultant of first stage
a, b, c, d = b ^ F(a | F(c ^ F(d)) ^ F(a | c) ^ d), \
             c ^ F(a ^ F(d) ^ (a | d)), \
             d ^ F(a | F(a) ^ a), \
             a ^ 31337
print(a)
print(b)
print(c)
print(d)
# Second stage decryption #obtain <a> -> <d> -> <c> -> <b> obtained from first stage
# notice we will use <a>(encrypted version) in obtaining <b> at te end
# but we will over write it when obtaining <a>(decrypted version) itself
# so we store it in tempa

##Decryotion of  stage one
tempa = a
a = d ^ 31337  # 0111 1010 0110 1001
d = c ^ F(a | F(a) ^ a)
c = b ^ F(a ^ F(d) ^ (a | d))
b = tempa ^ F(a | F(c ^ F(d)) ^ F(a | c) ^ d)
print(a)
print(b)
print(c)
print(d)

##after reversing the two stages we will do it for 32 round
# then we pach the result of  <a>, <b,> <c>, <d> using the same format at unpacking
# then the flag appears and removing the redundant <#> then submit.
