from django.http import HttpResponse

def home(request):
    # Bug: returns raw HTML string — no template inheritance
    return HttpResponse("<h1>Home</h1>")
