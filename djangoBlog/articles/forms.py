from django import form
from . import models

class CreateArticle(forms.ModelForm):
    class Meta:
        form = models.Article
        fields = ['title','slug','body','image']
        