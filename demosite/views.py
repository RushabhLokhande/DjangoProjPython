from django.http import HttpResponse

def home(request):
 return HttpResponse('<h1>Hello from Django</h1>')

def about(request):
 return HttpResponse('<h1>This is About Page</h1>')

