from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from .models import ToDoList, Item
from .forms import CreateNewList


def index(response, id):
    ls=ToDoList.objects.get(id=id)

    if response.method == "POST":
        if response.POST.get("save")

    return render(response,"main/list.html",{"ls": ls})


def home(response):
    return render(response,"main/home.html",{})
#test
def create(response):
    if response.method == "POST":
        form=CreateNewList(response.POST)
        if form.is_valid():
            n=form.cleaned_data["name"]
            t=ToDoList(name=n)
            t.save()
        return HttpResponseRedirect("/%i" %t.id)

    else:
        form = CreateNewList()
    return render(response,"main/create.html",{"form":form})
