from django.shortcuts import render
from .models import Board, Topic
from django.shortcuts import get_object_or_404, render

def home(request):
    boards = Board.objects.all()
    return render(request, 'forum/home.html', {'boards': boards})


def board_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    topics = board.topics.all() 
    return render(request, 'forum/topics.html', {'board': board, 'topics': topics})
