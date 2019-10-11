from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .forms import *


def index(request):
    context = {
        "all_books": Book.objects.all()
    }
    return render(request, "books_authors_app/index.html", context)


def books(request, book_id):
    context = {
        "all_books": Book.objects.get(id=book_id),
        "all_authors": Author.objects.exclude(books=book_id),
    }
    return render(request, "books_authors_app/books.html", context)


def add_book(request):
    if request.method == "POST":
        title = request.POST.get('book_title_form')
        desc = request.POST.get('book_desc_form')
        newBook = Book.objects.create(title=title, desc=desc)
        newBook.save()
    return redirect('/')

def add_author_to_book(request, book_id):
    if request.method == "POST":
        this_book = Book.objects.get(id=book_id)
        this_author_str = request.POST.get("add_an_author")
        new_author = Author.objects.get(id=this_author_str)
        this_book.authors.add(new_author)
    return redirect('/books/' + book_id)

# ------------------------------------------------------------------------------------

def authors(request):
    context = {
        "all_authors": Author.objects.all()
    }
    return render(request, "books_authors_app/authors.html", context)


def authors_profile(request, author_id):
    context = {
        "all_authors": Author.objects.get(id=author_id),
        "all_books": Book.objects.exclude(authors=author_id),
    }
    return render(request, "books_authors_app/authors_prof.html", context)


def add_author(request):
    if request.method == "POST":
        newAuthor = Author.objects.create(
            first_name=request.POST.get('first_name_form'), last_name=request.POST.get('last_name_form'), notes=request.POST.get('notes_form'))
        newAuthor.save()
    return redirect('/authors')

def add_book_to_author(request, author_id):
    if request.method == "POST":
        this_author = Author.objects.get(id=author_id)
        this_book_str = request.POST.get("add_a_book")
        new_book = Book.objects.get(id=this_book_str)
        this_author.books.add(new_book)
    return redirect('/authors/' + author_id)