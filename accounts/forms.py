from django import forms
from .models import User

class UserCreattionForm (forms.Form):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password']
        
        
    def data_validate(self, *args, **kwargs):
        pass