# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, render_to_response

from models import Book, Publisher, Author

def index(request):
    return HttpResponse('Books')


def searchForm(request):
    return render_to_response('search_form.html')


def search(request):
    if 'keyword' in request.GET and request.GET.get('keyword'):
        keyword = request.GET.get('keyword')
        books = Book.objects.filter(title__icontains=keyword)
        return render_to_response('search_results.html', {'books': books, 'query': keyword})
    else:
        return render_to_response('search_form.html', {'error': True})
