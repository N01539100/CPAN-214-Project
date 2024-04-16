from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from books.forms import BookForm
from books.models import Book


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            return HttpResponse('User not found')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('Invalid login')

    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('home')


def home(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'books': books})


def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'book_detail.html', {'book': book})


@login_required(login_url='/login/')
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.instance.posted_by = request.user
            form.save()
            return redirect('home')
    else:
        form = BookForm()

    return render(request, 'modify_book.html', {'form': form})


@login_required(login_url='/login/')
def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)

    if book.posted_by != request.user:
        return HttpResponse('You are not allowed to edit this post', status=404)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', book_id=book_id)
    else:
        form = BookForm(instance=book)

    return render(request, 'modify_book.html', {'form': form, 'book': book})


@login_required(login_url='/login/')
def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)

    if book.posted_by != request.user:
        return HttpResponse('You are not allowed to edit this post', status=404)

    if request.method == 'POST':
        book.delete()
        return redirect('home')

    return render(request, 'delete_book.html', {'book': book})
