from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    paramet={'name':'Ben', 'place':'Canada'}
    return render(request, 'index.html', paramet)
