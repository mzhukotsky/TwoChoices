from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.

def main(request):
    context = {"main": main}
    return render(request, "twochoices/main.html", context)
