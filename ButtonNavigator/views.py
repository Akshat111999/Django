from django.http import HttpResponse

def index(request):
    return HttpResponse("""<h1> Hey you click on this link </h1>  <a href="https://www.google.com"> Google </a> """)
