from django import forms

from recipe_project.recipe_app.models import Recipe


class CreateModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)

    class Meta:
        model = Recipe
        fields = ['title', 'image_url', 'description', 'ingredients', 'time']

        labels = {
            'image_url': 'Image URL',
            'time': 'Time (Minutes)',
        }


class EditModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)

    class Meta:
        model = Recipe
        fields = ['title', 'image_url', 'description', 'ingredients', 'time']

        labels = {
            'image_url': 'Image URL',
            'time': 'Time (Minutes)',
        }


class DeleteModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Recipe
        fields = ['title', 'image_url', 'description', 'ingredients', 'time']

        labels = {
            'image_url': 'Image URL',
            'time': 'Time (Minutes)',
        }
