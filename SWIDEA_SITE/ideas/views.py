from django.shortcuts import render, redirect, get_object_or_404
from .forms import IdeaForm
from .models import Idea

# Create your views here.
def main(request):
    ideas = Idea.objects.all()
    ctx={'ideas': ideas}
    return render(request, 'ideas/idea_list.html', ctx)
    #return render(request, 'base.html')

# def create(request):
#     if request.method == 'GET':
#         idea = IdeaForm()
#         ctx = {'idea': idea}
#         return render(request , 'idea_create.html', ctx)
    
def create(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ideas:main')
    else:
        form = IdeaForm()
    return render(request, 'ideas/idea_create.html', {'form': form})

# def detail(request, idea_id):
#     idea = get_object_or_404(Idea, pk=idea_id)
#     return render(request, 'idea_detail.html', {'idea': idea})

# def detail(request, pk):
#   idea = Idea.objects.get(id=pk)
#   return render(request, 'idea_detail.html')
def detail(request, idea_id):
    idea = get_object_or_404(Idea, pk=idea_id)
    return render(request, 'ideas/idea_detail.html', {'idea': idea})

# def update(request, pk):
#     idea=Idea.objects.get(id=pk)
#     if request.method=='GET':
#         form=IdeaForm(instance=idea)
#         ctx={'idea':idea, 'pk':pk}
#         return render(request, 'ideas/idea_update.html',ctx)
        
#     form = IdeaForm(request.POST, request.FILES, instance=idea)
#     if form.is_valid():
#         form.save()
#     return redirect('ideas:detail', idea_id=pk)
def update(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES, instance=idea)
        if form.is_valid():
            form.save()
            return redirect('ideas:detail', idea_id=pk)
        else:
            # If the form is not valid, re-render the page with the form errors
            return render(request, 'ideas/idea_update.html', {'form': form, 'pk': pk})
    else:
        # GET request: instantiate a form with the current idea instance
        form = IdeaForm(instance=idea)
        return render(request, 'ideas/idea_update.html', {'form': form, 'pk': pk})


def delete(request, pk):
    if request.method=='POST':
        Idea.objects.get(id=pk).delete()
    return redirect('ideas:main')