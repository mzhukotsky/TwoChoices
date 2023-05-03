from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.

def index(request):
    main = "Welcome to my Django app!"
    context = {"main": main}
    return render(request, "twochoices/index.html", context)