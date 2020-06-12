from django.shortcuts import render
from .models import FileObject


def index(request):
    return render(request, "index.html", {'files': FileObject.objects.all()})
