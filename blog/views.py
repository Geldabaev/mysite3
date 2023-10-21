from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def index(request):
    return render(request, "blog/index.html", {})


def category(request, catid):
    return HttpResponse(f"<h1>Cats{catid}</h1>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Странциа не найдена</h1>")

