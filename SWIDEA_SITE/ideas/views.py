from django.shortcuts import render, redirect, get_object_or_404
from .forms import IdeaForm
from .models import Idea

# Create your views here.
def main(request):
    ideas = Idea.objects.all()
    ctx={'ideas': ideas}
    return render(request, 'ideas/idea_list.html', ctx)

def create(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ideas:main')
    else:
        form = IdeaForm()
    return render(request, 'ideas/idea_create.html', {'form': form})

def detail(request, idea_id):
    idea = get_object_or_404(Idea, pk=idea_id)
    return render(request, 'ideas/idea_detail.html', {'idea': idea})

def update(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES, instance=idea)
        if form.is_valid():
            form.save()
            return redirect('ideas:detail', idea_id=pk)
        else:
            return render(request, 'ideas/idea_update.html', {'form': form, 'pk': pk})
    else:
        form = IdeaForm(instance=idea)
        return render(request, 'ideas/idea_update.html', {'form': form, 'pk': pk})

def delete(request, pk):
    if request.method=='POST':
        Idea.objects.get(id=pk).delete()
    return redirect('ideas:main')