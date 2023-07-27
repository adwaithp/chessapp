def get_valid_moves_for_knight(position):
    # Knight can move in an L-shaped pattern (2 squares in one direction and 1 square perpendicular).
    x, y = position[0], int(position[1])
    moves = []

    potential_moves = [
        (x + 2, y + 1),
        (x + 2, y - 1),
        (x - 2, y + 1),
        (x - 2, y - 1),
        (x + 1, y + 2),
        (x + 1, y - 2),
        (x - 1, y + 2),
        (x - 1, y - 2)
    ]

    for move in potential_moves:
        x, y = move
        if 'A' <= x <= 'H' and 1 <= y <= 8:
            moves.append(f"{x}{y}")

    return moves

pos = {"postions": {"Queen": "E7", "Bishop": "B7", "Rook":"G5", "Knight": "C3"}}
get_valid_moves_for_knight(pos)