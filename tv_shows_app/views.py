from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def allshows(request):
    context={
        "all_shows": Show.objects.all()
    }
    return render(request, 'show_all.html', context)

def oneshow(request, id):
    context = {
        "show": Show.objects.get(id=id)
    }
    return render(request, 'show_one.html', context)

def edit(request, id):
    context = {
        "show": Show.objects.get(id=id),
        "date": str(Show.objects.get(id=id).release_date),
    }
    return render(request, 'edit.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):

    errors = Show.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/shows/new/")
        
    print(request.POST)
    m=Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['date'], description=request.POST['description'])
    show=Show.objects.get(id=m.id)
    return redirect(f"/shows/{show.id}/")

def delete(request, id):
    Show.objects.get(id=id).delete()
    return redirect("/shows")

def update(request, id):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/shows/{id}/edit/")
    else:
        updated = Show.objects.get(id=id)
        if request.method == "POST":
            updated.title = request.POST.get('title')
            updated.network = request.POST.get('network')
            updated.release_date = request.POST.get('release_date')
            updated.description = request.POST.get('description')
        updated.save()
        return redirect(f"/shows/{id}/")