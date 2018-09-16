from django.shortcuts import render, HttpResponse

# Create your views here.
import datetime


def index(request):
    now = datetime.datetime.now()
    print(now, type(now))
    return render(request, "index.html", {"now": now})
