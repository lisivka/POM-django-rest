from django.shortcuts import render, redirect

# from book.forms import BookForm
from book.models import Book

from .forms import BookForm
from rest_framework import viewsets
from .serializers import BookSerializer


# for API
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


def index(request):
    data = Book.objects.all().order_by('?')[:3]
    context = {"books": data}
    print(data)
    return render(request, 'book/index.html', context=context)


def books_find(request):
    context = {'books': Book.objects.all(), "search_text": ""}
    if request.POST:
        search_name = request.POST['search_name']
        search_id = request.POST['search_id']

        if search_name:
            books = Book.objects.filter(name__icontains=search_name)
            context = {'books': books, "search_text": search_name}

        if search_id:
            books = Book.objects.filter(id=search_id)
            context = {'books': books, "search_text": search_id}
            print(search_id)
        print(search_id, search_name, )
    # else:
    #     context = {'books': Book.objects.all()}
    return context


def books(request):
    # context = {'books': Book.objects.all()}
    # if request.POST:
    #     search_name = request.POST['search_name']
    #     search_id = request.POST['search_id']
    #
    #     if search_name:
    #         books = Book.objects.filter(name=search_name)
    #         context = {'books': books}
    #
    #     if search_id:
    #         books = Book.objects.filter(id=search_id)
    #         context = {'books': books}
    #         print(search_id)
    # else:
    #     context = {'books': Book.objects.all()}

    context = books_find(request)
    return render(request, 'book/books.html', context)


def books_list(request):
    # context = {'books': Book.objects.all()}
    # if request.POST:
    #     search_name = request.POST['search_name']
    #     search_id = request.POST['search_id']
    #
    #     if search_name:
    #         books = Book.objects.filter(name=search_name)
    #         context = {'books': books}
    #
    #     if search_id:
    #         books = Book.objects.filter(id=search_id)
    #         context = {'books': books}
    #         print(search_id)
    # else:
    #     context = {'books': Book.objects.all()}
    context = books_find(request)
    return render(request, 'book/books_list.html', context)


def book_item(request, book_id):
    book = Book.objects.get(pk=book_id)
    print(book)
    context = {'book': book, 'title': book.name, 'id': book.id, 'authors': book.authors.all(),
               'count': book.count, 'name': book.name, 'description': book.description,
               'year': book.year, }

    return render(request, 'book/book_details.html', context)


def delete_book(request, pk):
    Book.delete_by_id(pk)
    return redirect('/book/books_list')


def create_book(request):
    # context = {}
    error = ''
    new_book = Book()
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        count = request.POST['count']

        new_book = new_book.create(name, description, count)
        book_id = str(new_book.id)
        return redirect('/books/' + book_id)
        # return redirect('/books/')

    context = {'book': new_book, 'error': error}
    return render(request, 'book/create_book.html', context)
    # return render(request, 'book/books.html', context)


def add_book(request, book_id=0):
    if request.method == 'GET':
        if book_id == 0:
            form = BookForm()
        else:
            book = Book.objects.get(pk=book_id)
            form = BookForm(instance=book)
        return render(request, 'book/add_book.html', {'form': form})
    else:
        if book_id == 0:
            form = BookForm(request.POST)
        else:
            book = Book.objects.get(pk=book_id)
            form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect(f'/books/')
        return redirect(f'/books/books/{book_id}')
