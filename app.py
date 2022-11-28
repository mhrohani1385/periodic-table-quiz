import random

elements = {
    1   : "H",
    2   : "He",
    3   : "Li",
    4   : "Be",
    5   : "B",
    6   : "C",
    7   : "N",
    8   : "O",
    9   : "F",
    10  : "Ne",
    11  : "Na",
    12  : "Mg",
    13  : "Al",
    14  : "Si",
    15  : "P",
    16  : "S",
    17  : "Cl",
    18  : "Ar",
    19  : "K",
    20  : "Ca",
    21  : "Sc",
    22  : "Ti",
    23  : "Va",
    24  : "Cr",
    25  : "Mn",
    26  : "Fe",
    27  : "Co",
    28  : "Ni",
    29  : "Cu",
    30  : "Zn",
    31  : "Ga",
    32  : "Ge",
    33  : "As",
    34  : "Se",
    35  : "Br",
    36  : "Kr",
    37  : "Rb",
    38  : "Sr",
    49  : "In",
    50  : "Sn",
    51  : "Sb",
    52  : "Te",
    53  : "I",
    54  : "Xe",
    81  : "Tl",
    82  : "Pb",
    83  : "Bi",
    84  : "Po",
    85  : "At",
    86  : "Rn"
}

quested = {}

def main():
    
    resume = True
    list = []

    for z, name in elements.items():
        list.append((z, name,))

    def check(indexInList : int):
        global resume

        element = list[indexInList]
        name = input(str(element[0]) + " : ")
        if name == "quit" :
            print("Your score : " + str(len(quested)))
            resume = False
        else :
            if name == element[1] :
                print("Currect !")
                quested[indexInList] = 1
            else :
                if indexInList in quested.keys():
                    quested[indexInList] += 1
                else:
                    quested[indexInList] = 1
                
                if quested[indexInList] == 2:
                    print(str(element[0]) + " : " + element[1])
                    print("----------------------------------")
                    quested.pop(indexInList)
                else:
                    print("Wrong ! Try again :")
                    check(indexInList)

    while(resume) :
        allFound = True
        randindex = random.randint(0, len(list) - 1)
        if randindex not in quested.keys():
            check(randindex)
        for index in range(0, len(list)):
            if not index in quested.keys():
                allFound = False
                break
        if allFound:
            print("You answer all questions !")
            break

if __name__ == '__main__':
    main()