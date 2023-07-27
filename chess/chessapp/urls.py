from django.urls import path
from .views import ChessPieceMovesView

urlpatterns = [
    path('chess/<slug>/', ChessPieceMovesView.as_view(), name='chess_piece_moves'),
]
