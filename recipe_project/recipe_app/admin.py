from django.contrib import admin

from recipe_project.recipe_app.models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title']