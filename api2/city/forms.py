#-*- coding: utf-8 -*-
from django import forms

class CForm(forms.Form):
    cname = forms.CharField(max_length = 100)
    CHOICES = [('1','Raves'),('0','DRave')]
    rstatus = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
