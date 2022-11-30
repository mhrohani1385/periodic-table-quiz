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
resume = True

def main():

    print(
        """
    Welcome to periodic table main elements quiz !
    https://github.com/mhrohani1385/periodic-table-quiz
         
    You can use \"quit\" as answer of a question to exit program .

-------------------------------------------------------------------
        """)
    
    list = []

    for z, name in elements.items():
        list.append((z, name,))

    def check(indexInList : int):
        global resume

        element = list[indexInList]
        name = input(str(element[0]) + " : ")
        if name == "quit" :
            print("\nYour score : " + str(len(quested)))
            resume = False
        else :
            if name == element[1] :
                print("Correct !")
                quested[indexInList] = 1
                print("----------------------------------")
            else :
                if indexInList in quested.keys():
                    quested[indexInList] += 1
                else:
                    quested[indexInList] = 1
                print("Wrong !")
                if quested[indexInList] == 2:
                    print(str(element[0]) + " : " + element[1])
                    quested.pop(indexInList)
                else:
                    check(indexInList)
                    print("----------------------------------")

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
