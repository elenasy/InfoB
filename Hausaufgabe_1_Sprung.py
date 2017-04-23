# Lösen der Aufgabe des Rösselsprungs
# Finde den kürzesten Weg vom Knoten (2,3) (Schachbrett) zu jeden anderen Punkt!

# Funktion zur Berechnung der erreichbaren Knoten von einem Ausgangsknoten
def find_knots(startknot):
    '''Funktion berechnet anhand des übergebenen Startknoten alle erreichbaren Knoten'''
    # Entpacken der beiden Variablenbestandteile in einzelne Variablen
    x_coord,y_coord=startknot

    # Berechnung aller möglichen Knoten
    found_knots=[(x_coord+1,y_coord+2),(x_coord-1,y_coord+2),(x_coord+1,y_coord-2),
                 (x_coord-1,y_coord-2),(x_coord+2,y_coord+1),(x_coord-2,y_coord+1),
                 (x_coord+2,y_coord-1),(x_coord-2,y_coord-1)]

    # Entfernen ungültiger Knoten
    for (x,y) in found_knots:
        if (x <= 0 or x >= 9) or (y <= 0 or y >= 9):
            found_knots.remove((x,y))

    # Alternativee Lösungsweg #1
    # 1.: Gefundenes den Anforderungen entsprechendes Knoten
    # 2.: Knoten aus der Liste found_knots
    # 3.: Liste aus dem die einzelnen Knotentupel bezogen werden
    #valid_knots=[(x,y) for (x,y) in found_knots if not (x <= 0 or x >= 9) or (y <= 0 or y >= 9)]

    # Alternativer Lösungsweg #2
    #def is_valid(knot):
    #    return not (knot[0] <= 0 or knot[0] >= 9) or (knot[1] <= 0 or knot[1] >= 9)
    #valid_knots = filter(is_valid, found_knots)

    # Alternativer Lösungsweg #3
    #valid_knots=filter(lambda knot: not (knot[0] <= 0 or knot[0] >= 9) or (knot[1] <= 0 or knot[1] >= 9),found_knots)

    return found_knots

# Berechnung der Weglänge
def step_length(endknot):
    '''Funktion berechnet die Weglänge zwischen Start- und Zielknoten'''
    # Festlegen der Warteliste und der Liste mit den bereits besuchten Knoten
    queue=[(2,3,0)]
    visited=[]

    #
    while len(queue) > 0:
        current_element=queue.pop(0)
        if (current_element[0],current_element[1]) == endknot:
            return current_element[2]

        # Element aus der queue wird in visited eingefügt
        visited.append(current_element)

        # Hinzufügen von Knotenpunkten zur Warteliste, wenn sie noch nicht besucht wurden
        new_elements=find_knots((current_element[0],current_element[1]))
        valid_elements=[(valid_unvisited_knot[0],valid_unvisited_knot[1],current_element[2]+1) for valid_unvisited_knot in new_elements
                        if valid_unvisited_knot not in visited and valid_unvisited_knot not in queue]
        queue+=valid_elements


if __name__ == '__main__':
    results = []
    for y in range(8,0,-1):
        for x in range(1,9):
            results.append(step_length((x,y)))

    for (i,x) in enumerate(results):
        if (i % 8 is 0):
            print("")
        print(str(x) + " ", end="")
