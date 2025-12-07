import os

def read_input():
    here = os.path.dirname(__file__)
    input_path = os.path.join(here, "input.txt")
    #input_path = os.path.join(here, "test_input.txt")

    # Llegim totes les línies del fitxer i fem strip() per eliminar salts de línia
    with open(input_path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f]

    return lines

def main():
    lines = read_input()
    print(f"Loaded {len(lines)} lines")

    accessible_rolls = 0

    # Recorrem totes les files
    for r in range(len(lines)):
        # Recorrem totes les columnes
        for c in range(len(lines[r])):

            # Només ens interessen les cel-les que són rotllos de paper
            if lines[r][c] == '@':

                adjacent_count = 0

                # 8 direccions al voltant d'una cel-la
                directions = [
                    (-1, -1), (-1, 0), (-1, 1),
                    (0, -1),           (0, 1),
                    (1, -1),  (1, 0),  (1, 1)
                ]

                # Recorrem totes les direccions
                for dr, dc in directions:
                    rr = r + dr   # nova fila
                    cc = c + dc   # nova columna

                    # Comprovem que rr i cc estan dins del mapa
                    if 0 <= rr < len(lines) and 0 <= cc < len(lines[0]):
                        # Si la posició veïna conté '@'
                        if lines[rr][cc] == '@':
                            adjacent_count += 1

                # si té menys de 4 adjacents '@', és accessible
                if adjacent_count < 4:
                    accessible_rolls += 1

    print(accessible_rolls)
    return accessible_rolls

if __name__ == "__main__":
    main()
