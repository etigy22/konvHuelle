# konvHuelle
Inkrementeller Algorithmus für die Berechnung der konvexen Hülle
von Etienne Gysling und Noé Tortomazi

## Zusammenfassung

Dieses Programm berechnet die konvexe Hülle einer zufällig erzeugten Menge von Punkten im zweidimensionalen Raum. Die Berechnung erfolgt durch Sortieren der Punkte und schrittweises Erstellen der oberen und unteren Hülle. Als Ergebnis werden die Punkte ausgegeben, die die konvexe Hülle bilden.

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

### Ausführen

```bash
python main.py
```

### Voraussetzungen

- Python 3.x
