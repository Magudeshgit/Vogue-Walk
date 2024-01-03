from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import VogueUser
from django.forms.utils import ErrorList
from django.utils.safestring import mark_safe

class formsignup(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class vogueuser(AuthenticationForm):
    class Meta:
        models = VogueUser
        fields = '__all__'

class DivErrorList(ErrorList):
     def __str__(self):
         return self.as_divs()
     def as_divs(self):
         if not self: return ''
         return mark_safe('<div class="errorl">%s</div>' % ''.join(['<div class="erroror">%s</div>' % e for e in self]))