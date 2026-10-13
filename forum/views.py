from .models import Board, Topic
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import login
from django.shortcuts import get_object_or_404, redirect, render
from .forms import SignUpForm

def home(request):
    boards = Board.objects.all()
    return render(request, 'forum/home.html', {'boards': boards})


def board_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    topics = board.topics.all() 
    return render(request, 'forum/topics.html', {'board': board, 'topics': topics})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # сразу создается сессия - пользователь вошел
            return redirect('forum:home')
    else:
        form = SignUpForm()
    return render(request, 'forum/signup.html', {'form': form})
    
