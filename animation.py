import random
import tkinter as tk

# -------------------------------
# Farben / Look
# -------------------------------
BG_COLOR = "#F5F5F7"        # heller, leicht grauer Hintergrund
POINT_COLOR = "#444444"     # normale Punkte (dunkelgrau)
HULL_POINT_COLOR = "#FF4C4C"  # Hüllpunkte (rot)
HULL_POINT_GLOW = "#FFB3B3"   # leichter Glow unter Hüllpunkten
LINE_COLOR = "#1E90FF"      # Hauptlinie (blau)
LINE_SHADOW = "#A0CFFF"     # „Schattenlinie“ (helles blau)


# -------------------------------
# Algorithmus (Monotone Chain)
# -------------------------------
def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def konvexe_huelle_schritte(punkte):
    pts = sorted(punkte)
    schritte = []

    obere = []
    for p in pts:
        while len(obere) >= 2 and cross(obere[-2], obere[-1], p) <= 0:
            obere.pop()
            schritte.append(obere.copy())
        obere.append(p)
        schritte.append(obere.copy())

    untere = []
    for p in reversed(pts):
        while len(untere) >= 2 and cross(untere[-2], untere[-1], p) <= 0:
            untere.pop()
            schritte.append((obere + untere).copy())
        untere.append(p)
        schritte.append((obere + untere).copy())

    huelle = obere[:-1] + untere[:-1]
    schritte.append(huelle.copy())

    return schritte


# -------------------------------
# Animation mit Start/Stop
# -------------------------------
def main():
    n = int(input("Anzahl der Punkte (8–15 empfohlen): "))

    # Zufallspunkte mit etwas Rand
    punkte = [(random.randint(60, 440), random.randint(60, 440)) for _ in range(n)]
    schritte = konvexe_huelle_schritte(punkte)

    root = tk.Tk()
    root.title("Konvexe Hülle – Animation")

    # Hintergrund für das Fenster
    root.configure(bg=BG_COLOR)

    # „Titel“-Label über dem Canvas
    title_label = tk.Label(
        root,
        text="Konvexe Hülle (inkrementeller Algorithmus)",
        bg=BG_COLOR,
        fg="#222222",
        font=("Segoe UI", 12, "bold")
    )
    title_label.pack(pady=(8, 0))

    # Canvas, auf dem alles gezeichnet wird
    canvas = tk.Canvas(
        root,
        width=500,
        height=500,
        bg=BG_COLOR,
        highlightthickness=0
    )
    canvas.pack(padx=10, pady=(5, 0))

    # Punkte einmalig zeichnen
    for (x, y) in punkte:
        canvas.create_oval(x-4, y-4, x+4, y+4, fill=POINT_COLOR, outline="")

    # Status-Text (Schritte) im Canvas
    step_text_id = canvas.create_text(
        250, 25,
        text=f"Bereit – {len(schritte)} Schritte verfügbar",
        font=("Segoe UI", 11),
        fill="#333333"
    )

    # Animationszustand
    current_step = 0
    running = False
    after_id = None

    def draw_current_step():
        nonlocal current_step, running, after_id
        if not running:
            return

        # nur die Hülle neu zeichnen, Punkte bleiben
        canvas.delete("hull")

        if current_step < len(schritte):
            huelle = schritte[current_step]

            # Schattenlinie (breiter, hell)
            if len(huelle) >= 2:
                for i in range(len(huelle)):
                    x1, y1 = huelle[i]
                    x2, y2 = huelle[(i + 1) % len(huelle)]
                    canvas.create_line(
                        x1, y1, x2, y2,
                        fill=LINE_SHADOW,
                        width=5,
                        capstyle=tk.ROUND,
                        tags="hull"
                    )
                # Hauptlinie (schmaler, kräftig blau, smooth)
                for i in range(len(huelle)):
                    x1, y1 = huelle[i]
                    x2, y2 = huelle[(i + 1) % len(huelle)]
                    canvas.create_line(
                        x1, y1, x2, y2,
                        fill=LINE_COLOR,
                        width=3,
                        smooth=True,
                        capstyle=tk.ROUND,
                        tags="hull"
                    )

            # Hüllpunkte mit leichtem Glow
            for (x, y) in huelle:
                # Glow
                canvas.create_oval(
                    x-9, y-9, x+9, y+9,
                    fill=HULL_POINT_GLOW,
                    outline="",
                    tags="hull"
                )
                # Kernpunkt
                canvas.create_oval(
                    x-5, y-5, x+5, y+5,
                    fill=HULL_POINT_COLOR,
                    outline="#AA0000",
                    width=1,
                    tags="hull"
                )

            # Schritt-Text aktualisieren
            canvas.itemconfig(
                step_text_id,
                text=f"Schritt {current_step + 1}/{len(schritte)}"
            )

            current_step += 1

            # nächster Frame oder fertig
            if current_step < len(schritte):
                after_id = root.after(700, draw_current_step)
            else:
                running = False
                after_id = None
                canvas.itemconfig(
                    step_text_id,
                    text=f"Fertig – {len(schritte)} Schritte"
                )

    def start_animation():
        nonlocal running, current_step, after_id
        if running:
            return
        if current_step >= len(schritte):
            current_step = 0
        running = True
        draw_current_step()

    def stop_animation():
        nonlocal running, after_id
        running = False
        if after_id is not None:
            root.after_cancel(after_id)
            after_id = None

    # Button-Leiste
    button_frame = tk.Frame(root, bg=BG_COLOR)
    button_frame.pack(pady=10)

    start_btn = tk.Button(
        button_frame,
        text="▶ Start",
        command=start_animation,
        font=("Segoe UI", 10),
        width=10,
        bg="#FFFFFF",
        fg="#222222",
        activebackground="#E0E0E0",
        relief="ridge",
        bd=1
    )
    stop_btn = tk.Button(
        button_frame,
        text="⏸ Stop",
        command=stop_animation,
        font=("Segoe UI", 10),
        width=10,
        bg="#FFFFFF",
        fg="#222222",
        activebackground="#E0E0E0",
        relief="ridge",
        bd=1
    )

    start_btn.pack(side="left", padx=5)
    stop_btn.pack(side="left", padx=5)

    root.mainloop()


if __name__ == "__main__":
    main()
