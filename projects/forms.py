from django.forms import ModelForm
from django import forms
from .models import Project 

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description' , 'source_link', 'demo_link' ,'tags','featured_image'] 
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    ## WTF?????
    def __init__(self,*args , **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


      #  self.fields['title'].widget.attrs.update({'class':'input','placeholder':'Add Title'})
    #^????