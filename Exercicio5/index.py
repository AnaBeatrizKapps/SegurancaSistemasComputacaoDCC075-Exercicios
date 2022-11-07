from BBS import BBS

bits = BBS(11897, 13597)
bits = bits.generateBits(20000)
# print(bits)

file = open("resultadoBitsBBS.txt", "a")

for bit in bits:
    file.write(str(bit))
file.close()
