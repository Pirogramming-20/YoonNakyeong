from django.shortcuts import render, HttpResponse, redirect
from .models import *

# Create your views here.
def review_list(request):
    review=Review.objects.all()
    context= {
        "review":review
    }
    return render(request,'review_list.html', context)

def review_read(request, pk):
    movie=Review.objects.get(id=pk)
    context={
        "movie":movie
    }
    return render(request,'review_read.html', context)

def review_create(request):
    return render(request, "review_create.html")

def review_create_final(request):
    if request.method=="POST":
        Review.objects.create(
            title=request.POST["title"],
            year=request.POST["year"],
            genre=request.POST["genre"],
            rating=request.POST["rating"],
            director=request.POST["director"],
            character=request.POST["character"],
            time=request.POST["time"],
            story=request.POST["story"],
        )
    return redirect("/review")

def review_update(request, pk):
    movie=Review.objects.get(id=pk)
    if request.method=="POST":
        movie.title=request.POST["title"]
        movie.year=request.POST["year"]
        movie.genre=request.POST["genre"]
        movie.rating=request.POST["rating"]
        movie.director=request.POST["director"]
        movie.character=request.POST["character"]
        movie.time=request.POST["time"]
        movie.story=request.POST["story"]
        movie.save()
        return redirect(f"/review/{pk}")
    context={
        "movie":movie
    }
    return render(request, "review_update.html",context)

def review_delete(request,pk):
    if request.method=="POST":
        movie=Review.objects.get(id=pk)
        movie.delete()
    return redirect('/review')

