import random
import matplotlib.pyplot as plt
from main import konvexe_huelle


def main():
    n = int(input("Anzahl der Punkte (3–100): "))
    punkte = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(n)]

    # Deine Funktion liefert obere & untere Hülle
    obere, untere = konvexe_huelle(punkte)

    # --- alle Punkte plotten ---
    xs, ys = zip(*punkte)
    plt.scatter(xs, ys, label="Punkte")

    # --- komplette konvexe Hülle bilden ---
    # obere: links → rechts
    # untere: rechts → links
    # letzter Punkt von jeder Liste entfernen (doppelt)
    huelle = obere + untere[1:-1]

    # --- Hülle schließen ---
    hx, hy = zip(*(huelle + [huelle[0]]))

    plt.plot(hx, hy, "-o", label="Konvexe Hülle", linewidth=2)

    plt.title("Visualisierung der konvexen Hülle")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    plt.axis("equal")
    plt.show()


if __name__ == "__main__":
    main()
