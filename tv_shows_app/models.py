from django.db import models
from django.forms import ModelForm

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=10)
    release_date = models.DateField()
    description = models.CharField(max_length=255)

class ShowForm(ModelForm):
    class Meta:
        model = Show
        fields = [
            'title',
            'network',
            'release_date',
            'description',
        ]