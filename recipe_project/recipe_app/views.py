from django.shortcuts import render, redirect

from recipe_project.recipe_app.forms import CreateModelForm, DeleteModelForm
from recipe_project.recipe_app.models import Recipe


def home(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes,
    }
    return render(request, 'index.html', context)


def create(request):
    if request.method == 'POST':

        form = CreateModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:

        form = CreateModelForm()

    context = {
        'form': form,
    }
    return render(request, 'create.html', context)


def edit(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':

        form = CreateModelForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:

        form = CreateModelForm(instance=recipe)

    context = {
        'form': form,
        'recipe': recipe,
    }
    return render(request, 'edit.html', context)


def delete(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':

        form = DeleteModelForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:

        form = DeleteModelForm(instance=recipe)

    context = {
        'form': form,
        'recipe': recipe,
    }
    return render(request, 'delete.html', context)


def details(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ingredients_string = recipe.ingredients
    ingredients_list = ingredients_string.split(',')
    context = {
        'recipe': recipe,
        'ingredients_list': ingredients_list,
    }
    return render(request, 'details.html', context)
