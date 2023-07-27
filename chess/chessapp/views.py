from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

def get_valid_moves_for_knight(position):
    # Knight can move in an L-shaped pattern (2 squares in one direction and 1 square perpendicular).
    x, y = ord(position[0]), int(position[1])
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
        if ord('A') <= x <= ord('H') and 1 <= y <= 8:
            moves.append(f"{chr(x)}{y}")

    return moves



def get_valid_moves_for_bishop(position):
    # Bishop can move diagonally in all four directions until it reaches the edge of the board or captures an opponent's piece.
    x, y = position[0], int(position[1])
    moves = []

    # Top-right diagonal
    for i in range(1, 8):
        if 'A' <= chr(ord(x) + i) <= 'H' and 1 <= y + i <= 8:
            moves.append(f"{chr(ord(x) + i)}{y + i}")
        else:
            break

    # Top-left diagonal
    for i in range(1, 8):
        if 'A' <= chr(ord(x) - i) <= 'H' and 1 <= y + i <= 8:
            moves.append(f"{chr(ord(x) - i)}{y + i}")
        else:
            break

    # Bottom-right diagonal
    for i in range(1, 8):
        if 'A' <= chr(ord(x) + i) <= 'H' and 1 <= y - i <= 8:
            moves.append(f"{chr(ord(x) + i)}{y - i}")
        else:
            break

    # Bottom-left diagonal
    for i in range(1, 8):
        if 'A' <= chr(ord(x) - i) <= 'H' and 1 <= y - i <= 8:
            moves.append(f"{chr(ord(x) - i)}{y - i}")
        else:
            break

    return moves


def get_valid_moves_for_rook(position):
    # Rook can move vertically and horizontally until it reaches the edge of the board or captures an opponent's piece.
    x, y = position[0], int(position[1])
    moves = []

    # Up
    for i in range(1, 8):
        if 1 <= y + i <= 8:
            moves.append(f"{x}{y + i}")
        else:
            break

    # Down
    for i in range(1, 8):
        if 1 <= y - i <= 8:
            moves.append(f"{x}{y - i}")
        else:
            break

    # Right
    for i in range(1, 8):
        if 'A' <= chr(ord(x) + i) <= 'H':
            moves.append(f"{chr(ord(x) + i)}{y}")
        else:
            break

    # Left
    for i in range(1, 8):
        if 'A' <= chr(ord(x) - i) <= 'H':
            moves.append(f"{chr(ord(x) - i)}{y}")
        else:
            break

    return moves


def get_valid_moves_for_queen(position):
    # Queen can move diagonally, vertically, and horizontally until it reaches the edge of the board or captures an opponent's piece.
    moves = get_valid_moves_for_bishop(position) + get_valid_moves_for_rook(position)
    return moves


class ChessPieceMovesView(APIView):
    def post(self, request, slug):
        positions = request.data.get('positions')
        valid_moves_queen = []
        valid_moves_knight = []
        valid_moves_bishop = []
        valid_moves_rook = []

        if 'Queen' in positions:
            valid_moves_queen = get_valid_moves_for_queen(positions['Queen'])
        if 'Knight' in positions:
            valid_moves_knight = get_valid_moves_for_knight(positions['Knight'])
        if 'Bishop' in positions:
            valid_moves_bishop = get_valid_moves_for_bishop(positions['Bishop'])
        if 'Rook' in positions:
            valid_moves_rook = get_valid_moves_for_rook(positions['Rook'])

        if slug == "knight":
            all_other_valid_moves = valid_moves_queen + valid_moves_bishop + valid_moves_rook
            valid_moves = [item for item in valid_moves_knight if item not in all_other_valid_moves]
        elif slug == "bishop":
            all_other_valid_moves = valid_moves_queen + valid_moves_knight + valid_moves_rook
            valid_moves = [item for item in valid_moves_bishop if item not in all_other_valid_moves]
        elif slug == "rook":
            all_other_valid_moves = valid_moves_queen + valid_moves_knight + valid_moves_bishop
            valid_moves = [item for item in valid_moves_rook if item not in all_other_valid_moves]
        elif slug == "queen":
            all_other_valid_moves = valid_moves_rook + valid_moves_knight + valid_moves_bishop
            valid_moves = [item for item in valid_moves_queen if item not in all_other_valid_moves]
        else:
            valid_moves = []

        return Response({"valid_moves": valid_moves}, status=status.HTTP_200_OK)
