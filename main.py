import random

def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

def konvexe_huelle(punkte):
    pts = sorted(punkte)
    # Obere Hülle (links -> rechts)
    obere = []
    for p in pts:
        while len(obere) >= 2 and cross(obere[-2], obere[-1], p) <= 0:
            obere.pop()
        obere.append(p)
    # Untere Hülle (rechts -> links)
    untere = []
    for p in reversed(pts):
        while len(untere) >= 2 and cross(untere[-2], untere[-1], p) <= 0:
            untere.pop()
        untere.append(p)
    return obere, untere

def eingabe():
    while True:
        try:
            n = int(input("Gib die Anzahl Punkte ein (3–100): "))
            if 3 <= n <= 100:
                return n
        except ValueError:
            pass
        print("Bitte eine ganze Zahl zwischen 3 und 100 eingeben.")

def main():
    n = eingabe()
    punkte = [(random.randint(0,100), random.randint(0,100)) for _ in range(n)]

    print("\nZufällige Punkte:")
    for p in punkte:
        print(p)

    obere, untere = konvexe_huelle(punkte)
    gemeinsame = sorted(set(obere) & set(untere))

    print("\nObere Hülle (links → rechts):")
    for p in obere:
        print(p)

    print("\nUntere Hülle (rechts → links):")
    for p in untere:
        print(p)

    print("\nGemeinsame Punkte (in beiden Hüllen):")
    for p in gemeinsame:
        print(p)

if __name__ == "__main__":
    main()