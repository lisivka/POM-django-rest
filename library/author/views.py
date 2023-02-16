from django.shortcuts import render, redirect
from author.forms import CreateAuthor
from author.models import Author
from django.db.models import Q

from .models import Author
from rest_framework.viewsets import ModelViewSet
from .serializers import AuthorSerializer


# for API
class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


def author_item(request, author_id):
    author = Author.objects.get(pk=author_id)
    context = {'name': author.name, 'surname': author.surname, 'patronymic': author.patronymic,
               'id': author.id, 'books': author.books.all(), }
    return render(request, 'author/author_details.html', context)


def create_author_new(request, author_id=None):
    if request.method == 'GET':
        if author_id:
            author = Author.get_by_id(author_id)
            form = CreateAuthor(instance=author)
            title = 'Update author'
        else:
            form = CreateAuthor()
            title = 'Create author'

        return render(request, 'author/add_author.html', {'form': form, 'title': title})
    else:
        if not author_id:
            form = CreateAuthor(request.POST)
            title = 'Create author'
        else:
            author = Author.get_by_id(author_id)
            form = CreateAuthor(request.POST, instance=author)
            title = 'Update author'
        if form.is_valid():
            form.save()
        else:
            return render(request, 'author/add_author.html', {'form': form, 'title': title})
        return redirect('/authors')


def author_list(request):
    context = {'authors': Author.objects.all(), "search_text": ""}
    # search_name = request.POST['search_name']
    # search_id = request.POST['search_id']
    if request.POST:
        search_name = request.POST['search_name']
        search_id = request.POST['search_id']

        if search_name:
            authors = Author.objects.filter(Q(name__icontains=search_name) | Q(surname__icontains=search_name))
            # authors2 = Author.objects.filter(surname__icontains = search_name)
            context = {'authors': authors, "search_text": search_name}

        if search_id:
            authors = Author.objects.filter(id=search_id)
            context = {'authors': authors, "search_text": search_id}
            # print(search_id)
        print("search: ", search_id, search_name, )

    return render(request, 'author/author_list.html', context)


# def authors(request):
#     authors = Author.get_all()
#     return render(request, 'author/authors.html', {'authors': authors})


def delete(request, author_id=None):
    if author_id:
        Author.delete_by_id(author_id)
    authors = Author.get_all()
    return render(request, 'author/author_list.html', {'authors': authors})


def delete_author(request, author_id=None):
    if author_id:
        Author.delete_by_id(author_id)
    authors = Author.get_all()
    return render(request, 'author/author_list.html', {'authors': authors})
