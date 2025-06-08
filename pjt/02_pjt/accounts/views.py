from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from boards.models import Board, Comment

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('boards:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("boards:index")
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('boards:index')


def profile(request, user_pk):
    boards = Board.objects.filter(author=user_pk)
    comments = Comment.objects.filter(author=user_pk)
    User = get_user_model()
    person = User.objects.get(pk=user_pk)
    followings = person.followings.all()
    followers = person.followers.all()
    context = {
        'boards': boards,
        'comments': comments,
        'person': person,
        'followings': followings,
        'followers': followers, 
    }

    return render(request, 'accounts/profile.html', context)

@login_required
def follow(request, user_pk):
    User = get_user_model()
    person = User.objects.get(pk=user_pk)
    if person != request.user:
        if request.user in person.followers.all():
            person.followers.remove(request.user)
        else:
            person.followers.add(request.user)
    
    return redirect('accounts:profile', person.pk)