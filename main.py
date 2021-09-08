def f(x, y, z, w):
    return int( (((not x) or y) == ( (not y) or (not z) )) and (y or w))

print("x y z w     f")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                print(x, y, z, w, "   " ,f(x, y, z, w))


