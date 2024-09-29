print ("hello")
a = bytearray((0x01, 0x02 , 0x03 ))
print(a.hex())


data = bytearray.fromhex("1234567890aabbccddeeff")
print(data.hex())