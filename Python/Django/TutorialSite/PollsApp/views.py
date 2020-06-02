from django.http import HttpResponse

def index(request):
    site = "Hello World! You're at the polls index"

    return HttpResponse(site)
