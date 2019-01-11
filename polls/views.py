from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse



def index(request):
    print(request.session.get("a"))
    if request.session.get("a"):
        request.session['a'] += 1
    else:
        request.session['a'] = 1
    print(request.session.get("a"))

    return render(request, 'polls/index.html')