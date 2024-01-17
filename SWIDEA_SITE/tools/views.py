from django.shortcuts import render, redirect,get_object_or_404
from .forms import ToolForm
from .models import Tool

# Create your views here.
def tool(request):
    tools = Tool.objects.all()
    ctx={'tools': tools}
    return render(request, 'tools/tool_list.html', ctx)

def detail(request, pk):
    tool = get_object_or_404(Tool, pk=pk)
    ctx= {'tool': tool}
    return render(request, 'tools/tool_detail.html',ctx)

def create(request):
    if request.method == 'POST':
        form = ToolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tools:tool')
    else:
        form = ToolForm()
    return render(request, 'tools/tool_create.html', {'form': form})

def delete(request, pk):
    if request.method=='POST':
        Tool.objects.get(pk=pk).delete()
    return redirect('tools:tool')

def update(request, pk):
    tool = get_object_or_404(Tool, pk=pk)
    if request.method == 'POST':
        form = ToolForm(request.POST, request.FILES, instance=tool)
        if form.is_valid():
            form.save()
            return redirect('tools:detail', pk=pk)
        else:
            ctx={'form': form, 'pk': pk}
            return render(request, 'tools/tool_update.html', ctx)
    else:
        form = ToolForm(instance=tool)
        ctx={'form': form, 'pk': pk}
        return render(request, 'tools/tool_update.html', ctx)
