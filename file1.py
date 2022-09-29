def check_equal(x, y, z):
    if x == y and y == z and x == z:
        print("All the inputs are equal")
        return 1
    elif x == y:
        print("Only x and y are equal")
        return 2
    elif y == z:
        print("Only y and z are equal")
        return 3
    elif x == z:
        print("Only x and z are equal")
        return 4
    else:
        print("They all are different.")
        return 5

tests = [(42,1,42),(1,1,-5),(5,4,-1),(5,5,5),(0,0,1), (-9,9,9),(9,8,90)]
for x, y, z in tests:
    print(check_equal(x, y, z))
    