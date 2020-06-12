from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib import messages

from .models import FileObject
from .forms import AddFileForm


def index(request):
    return render(request, "index.html", {'files': FileObject.objects.all()})


def fileadd(request):
    html = 'genericform.html'
    form = AddFileForm()
    if request.method == "POST":
        form = AddFileForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            FileObject.objects.create(
                name=data['name'],
                parent=data['parent']
            )
            messages.info(request, "File created successfully!")
            return HttpResponseRedirect(reverse('homepage'))

    return render(request, html, {"form": form})
