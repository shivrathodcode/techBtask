from django import forms
from .models import ToDo
class TodoForm(forms.ModelForm):
    class Meta:
        model=ToDo
        fields='__all__'

        labels={
            'team_name':'Enter Team Name',
            'captain':'Enter Captain name',
            'city':'Enter city Name',
            't_mem':'Enter Total members'



        }




