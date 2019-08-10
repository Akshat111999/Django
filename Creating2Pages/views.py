from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1> hey you ")
def about(request):
    return HttpResponse("about us")
