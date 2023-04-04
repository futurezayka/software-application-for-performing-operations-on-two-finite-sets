# 3 2 5 4 7
# 4 7 8 2 1 5








U = {1, 2, 3, 4, 5, 6, 7, 8}
A1 = {3, 2, 5, 4, 7}
B1 = {4, 7, 8, 2, 1, 5}


A = set(map(int, input("Введіть першу множину(A): ").split()))
B = set(map(int, input("Введіть другу множину(B): ").split()))
# U = set(map(int, input("Введіть універсальну множину(U): ").split()))


def checker():
    if A != A1 or B != B1 :
        print("Ви ввели некоректну множину")
        quit()
checker()

def main():
    add(A, B)
    peret(A, B)
    minus(A, B)
    dobut(A, B)
    iss(A, B)
    bitok()

def add(A, B):
    adding = set()
    for a in A:
        if a not in adding:
            adding.add(a)

    for a in B:
        if a not in adding:
            adding.add(a)

    return adding
print("\n\nОб'єднання: ", add(A, B))

def peret(A, B):
    peretin = set()
    for a in A:
        for b in B:
            if b == a:
                peretin.add(b)
        return peretin
print("Перетин: ", peret(A, B))

def minus(A, B):
    rizn1 = set()
    for a in A:
        if not a in B:
            rizn1.add(a)
        return rizn1
print("Різниця (A - B): ", minus(A, B))
print("Різниця (B - A): ", minus(B, A))
print("Доповнення множини A: ", minus(U, A))
print("Доповнення множини B: ", minus(U, B))
print("Симетична різниця: ", minus(add(A, B), peret(A, B)))

def dobut(A, B):
    dob = list()
    for a in A:
        for b in B:
            dob.append((a, b))
    return dob
print("Декартовий добуток: ", dobut(A, B), "\n\n")

def iss(A, B):
    if A == B:
        return "Множини рівні"
    else:
        print("Множини не рівні")
    c = set()
    for a in A:
        for b in B:
            if a == b:
                c.add(a)
    if c != A:
        return "не є підмножиною"
    else:
        return "є підмножиною"
print("Множина А", iss(A, B), "В")

def iss1(B, A):
    c = set()
    for b in B:
        for a in A:
            if b == a:
                c.add(a)
    if c != B:
        return "не є підмножиною"
    else:
        return "є підмножиною"
print("Множина B", iss1(B, A), "A")

def inbit(A):
    bitted = list()
    for a in range(1, 9):
        if a in A:
            bitted.append(1)
        else:
            bitted.append(0)
    return bitted
print("\n\nМножина А у вигляді бітового рядка: ", inbit(A))
print("Множина B у вигляді бітового рядка: ", inbit(B))


def bitok():
    def bitsum():
        summab = set()
        for i in range(8):
            summ = inbit(A)[i] + inbit(B)[i]
            if summ == 0:
                continue
            else:
                i += 1
                summab.add(i)
        return summab

    print("Об'єднання за допомогою бітових рядків:", bitsum())

    def bitperet():
        perab = set()
        for i in range(8):
            summ = inbit(A)[i] + inbit(B)[i]
            if summ == 0 or summ == 1:
                continue
            else:
                i += 1
                perab.add(i)
        return perab

    print("Перетин за допомогою бітових рядків:", bitperet())

    def biriz():
        rizn = set()
        for i in range(8):
            bitrizn = inbit(A)[i] - inbit(B)[i]
            if bitrizn == 1:
                i += 1
                rizn.add(i)
            else:
                continue
        return rizn

    print("Різниця за допомогою бітових рядів:", biriz())

    def simriz():
        simbriz = set()
        for i in range(8):
            summ = inbit(A)[i] + inbit(B)[i]
            if summ == 2 or summ == 0:
                continue
            else:
                i += 1
                simbriz.add(i)
        return simbriz

    print("Симетрична різниця за допомогою бітових рядків:", simriz())


if __name__ == '__main__':
    main()
