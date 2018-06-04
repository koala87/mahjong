from django import forms


MAX_LENGTH = 128


class CreateForm(forms.Form):
    name = forms.CharField(max_length=MAX_LENGTH)
    circle = forms.IntegerField()
    base = forms.IntegerField()
    member1 = forms.CharField(max_length=MAX_LENGTH)
    member2 = forms.CharField(max_length=MAX_LENGTH)
    member3 = forms.CharField(max_length=MAX_LENGTH)
    member4 = forms.CharField(max_length=MAX_LENGTH)