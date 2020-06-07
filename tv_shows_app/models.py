from django.db import models
from django.forms import ModelForm

class ShowManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}

        if len(post_data['title'])<2:
            errors['title'] = "Show title must be at least 2 characters"
        
        if len(post_data['network'])<2:
            errors['network'] = "Network name must be at least 3 characters"
        
        if len(post_data['description'])<2:
            errors['description'] = "Description must be at least 10 characters"

        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=10)
    release_date = models.DateField()
    description = models.CharField(max_length=255)

    objects = ShowManager()

class ShowForm(ModelForm):
    class Meta:
        model = Show
        fields = [
            'title',
            'network',
            'release_date',
            'description',
        ]