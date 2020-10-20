from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse("Hello naseef")
    return render(request, 'dashboard.html')
def login(request):
    return render(request, 'loginpage.html')
