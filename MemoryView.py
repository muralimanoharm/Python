#random bytearray
randomByteArray = bytearray('ABC', 'utf-8')

mv = memoryview(randomByteArray)

# access memory view's zeroth index
print(mv[0])

# create byte from memory view
print(bytes(mv[0:2]))

# create list from memory view
print(list(mv[0:3]))
