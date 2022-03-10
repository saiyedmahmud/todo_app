from dataclasses import fields
from django import forms
from django import forms
from django.forms import ModelForm
from todo.models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name','priority','description','completed']
        widgets ={
            'name':forms.TextInput(attrs={'class':"form-control", "placeholder":"Add Task"}),
            'priority':forms.Select(attrs={"class":"form-control"}),
            'description':forms.Textarea(attrs={"class":"form-control","rows":8, "placeholder":"Enter Message.."}),
            'completed':forms.CheckboxInput(attrs={"type":"checkbox", "class":"form-check-input" })
        }