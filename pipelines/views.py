from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1> First page </h1>")
def removepunc(request):
    return HttpResponse("Remove punctuation")
def firstcap(request):
    return HttpResponse("Capitalize first")
def newlineRemove(request):
    return HttpResponse("Remove new line")
def spaceRemover(request):
    return HttpResponse("Space Remover")
def charcount(request):
    return HttpResponse("character counter")
