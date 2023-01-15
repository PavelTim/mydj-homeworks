from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Book


class DatePag():

    def __init__(self, date):
        self.date = date
        self.result = None

    def books(self):
        return Book.objects.filter(pub_date=self.date)

    def has_next(self):
        self.result = Book.objects.filter(pub_date__gt=self.date).order_by('pub_date').first()
        return bool(self.result)

    def has_previous(self):
        self.result = Book.objects.filter(pub_date__lt=self.date).order_by('pub_date').last()
        return bool(self.result)

    # гениально
    def next_page_number(self):
        return self.result.pub_date

    def previous_page_number(self):
        return self.result.pub_date

def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, template, context)

def books_views(request, date=None):
    print('!'*50, '\n', date, '!'*50, '\n')
    template = 'books/books_list_date.html'
    page = DatePag(date)

    # pag = Paginator(book, 10)
    # page = pag(1)
    # print(dir(page))
    # print(book.pub_date)

    context = {
        'books': page.books(),
        'page': page
    }
    return render(request, template, context)
