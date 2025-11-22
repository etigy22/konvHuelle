# konvHuelle
Inkrementeller Algorithmus für die Berechnung der konvexen Hülle
von Etienne Gysling und Noé Tortomasi

## Zusammenfassung

Dieses Programm berechnet die konvexe Hülle einer zufällig erzeugten Menge von Punkten im zweidimensionalen Raum. Die Berechnung erfolgt durch Sortieren der Punkte und schrittweises Erstellen der oberen und unteren Hülle. Als Ergebnis werden die Punkte ausgegeben, die die konvexe Hülle bilden.

## Visualisierung und Animation der konvexen Hülle

Zur Veranschaulichung des inkrementellen Algorithmus zur Berechnung der konvexen Hülle wurden zwei verschiedene Visualisierungen umgesetzt.

In einem ersten Schritt werden mit Python zufällige Punkte im zweidimensionalen Raum erzeugt und mit Matplotlib als Streudiagramm dargestellt. Die berechnete konvexe Hülle wird anschließend als geschlossenes Polygon um diese Punktmenge gezeichnet. Dadurch lässt sich gut erkennen, welche Punkte als Eckpunkte der Hülle auf dem „Rand“ der Menge liegen.

Zusätzlich wurde eine einfache Animation mit Tkinter implementiert. Diese zeigt schrittweise, wie der Algorithmus die obere und untere Hülle aufbaut und dabei Punkte wieder verwirft, die nicht zur äußeren Hülle gehören. Die Animation hilft dabei, den Ablauf des Monotone-Chain-Algorithmus intuitiv nachzuvollziehen, auch wenn die Darstellung technisch bedingt eher schlicht ist.

## Ablauf

- Der Benutzer gibt die gewünschte Anzahl an Punkten (zwischen 3 und 100) ein.
- Es werden zufällige Punkte im Bereich (0, 0) bis (100, 100) erzeugt.
- Die erzeugten Punkte werden ausgegeben.
- Die konvexe Hülle wird berechnet, indem die Punkte sortiert und die obere sowie untere Hülle mittels Kreuzprodukt konstruiert werden.
- Die obere Hülle (von links nach rechts) wird ausgegeben.
- Die untere Hülle (von rechts nach links) wird ausgegeben.
- Gemeinsame Punkte werden ausgegeben.

## Hauptdatei

Die Hauptdatei (`main.py`) implementiert einen inkrementellen Algorithmus zur Berechnung der konvexen Hülle.

## Visualierungsdatei

Die Datei (`visualisierung.py`) gibt eine Grafik aus der Berechnung der konvexen Hülle nach dem inkrementellen Algorithmus aus.

## Animationsdatei

Die Datei (`animation.py`) öffnet ein separates Fenster und zeigt den Ablauf der Berechnung der konvexen Hülle.

### Ausführen

```bash
python main.py
```

### Voraussetzungen

- Python 3.7 oder höher
