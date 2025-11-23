import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from typing import List, Dict, Any, Tuple


# -----------------------------
# Geometriefunktionen
# -----------------------------

def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def konvexe_huelle(punkte):
    pts = sorted(punkte)

    # Obere Hülle (links -> rechts)
    obere = []
    for p in pts:
        # WICHTIG: Jetzt >= 0 statt <= 0
        while len(obere) >= 2 and cross(obere[-2], obere[-1], p) >= 0:
            obere.pop()
        obere.append(p)

    # Untere Hülle (rechts -> links)
    untere = []
    for p in reversed(pts):
        while len(untere) >= 2 and cross(untere[-2], untere[-1], p) >= 0:
            untere.pop()
        untere.append(p)

    return obere, untere


# -----------------------------
# Schrittspeicherung für Animation
# (erst alle Schritte der oberen Hülle, dann alle der unteren)
# -----------------------------

def konvexe_huelle_schritte(punkte) -> List[Dict[str, Any]]:
    pts = sorted(punkte)
    obere: List[Tuple[int, int]] = []
    untere: List[Tuple[int, int]] = []
    schritte: List[Dict[str, Any]] = []

    # Obere Hülle (links -> rechts)
    for p in pts:
        while len(obere) >= 2 and cross(obere[-2], obere[-1], p) >= 0:
            obere.pop()
            schritte.append({
                "obere": list(obere),
                "untere": list(untere),
                "punkt": p,
                "phase": "obere"
            })

        obere.append(p)
        schritte.append({
            "obere": list(obere),
            "untere": list(untere),
            "punkt": p,
            "phase": "obere"
        })

    # Untere Hülle (rechts -> links)
    for p in reversed(pts):
        while len(untere) >= 2 and cross(untere[-2], untere[-1], p) >= 0:
            untere.pop()
            schritte.append({
                "obere": list(obere),
                "untere": list(untere),
                "punkt": p,
                "phase": "untere"
            })

        untere.append(p)
        schritte.append({
            "obere": list(obere),
            "untere": list(untere),
            "punkt": p,
            "phase": "untere"
        })

    return schritte


# -----------------------------
# Animation
# -----------------------------

def animiere_konvexe_huelle(punkte):
    schritte = konvexe_huelle_schritte(punkte)

    xs = [p[0] for p in punkte]
    ys = [p[1] for p in punkte]

    fig, ax = plt.subplots()
    ax.set_title("Animation der konvexen Hülle (Monotone Chain)")
    ax.set_xlim(min(xs) - 5, max(xs) + 5)
    ax.set_ylim(min(ys) - 5, max(ys) + 5)
    ax.set_aspect("equal", adjustable="box")
    ax.grid(True)

    # Alle Punkte
    ax.scatter(xs, ys, s=30)

    (linie_obere,) = ax.plot([], [], linewidth=2)   # obere Hülle
    (linie_untere,) = ax.plot([], [], linewidth=2)  # untere Hülle
    (aktueller_punkt_plot,) = ax.plot([], [], "o", markersize=10)

    text_phase = ax.text(
        0.02, 0.98, "",
        transform=ax.transAxes,
        verticalalignment="top"
    )

    def update(frame):
        schritt = schritte[frame]

        obere = schritt.get("obere", [])
        untere = schritt.get("untere", [])
        p = schritt.get("punkt")
        phase = schritt.get("phase", "")

        # Obere Hülle updaten
        if obere:
            linie_obere.set_data(
                [pt[0] for pt in obere],
                [pt[1] for pt in obere]
            )
        else:
            linie_obere.set_data([], [])

        # Untere Hülle updaten
        if untere:
            linie_untere.set_data(
                [pt[0] for pt in untere],
                [pt[1] for pt in untere]
            )
        else:
            linie_untere.set_data([], [])

        # Aktueller Punkt
        if p is not None:
            aktueller_punkt_plot.set_data([p[0]], [p[1]])

        text_phase.set_text(f"Phase: {phase} | Punkt: {p}")

        return linie_obere, linie_untere, aktueller_punkt_plot, text_phase

    ani = FuncAnimation(
        fig,
        update,
        frames=len(schritte),
        interval=500,   # ms zwischen Frames
        blit=True,
        repeat=False
    )

    plt.show()


# -----------------------------
# Ein- und Ausgabe
# -----------------------------

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
    punkte = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(n)]

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

    animiere_konvexe_huelle(punkte)


if __name__ == "__main__":
    main()