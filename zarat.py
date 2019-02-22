from random import*
for i in range(0,2):
    a = randrange(1, 7)
    print("+---------+")
    if (a == 1):
        print("|         |")
        print("|    *    |")
        print("|         |")
    elif (a == 2):
        print("|  *      |")
        print("|         |")
        print("|      *  |")
    elif (a == 3):
        print("| *       |")
        print("|    *    |")
        print("|       * |")
    elif (a == 4):
        print("| *     * |")
        print("|         |")
        print("| *     * |")
    elif (a == 5):
        print("| *     * |")
        print("|    *    |")
        print("| *     * |")
    elif (a == 6):
        print("| *  *  * |")
        print("|         |")
        print("| *  *  * |")
    print("+---------+")
    print()