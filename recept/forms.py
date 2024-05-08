from django import forms
from recept.models import Recepts,SubCategories

# creating a form

class NewRecepts(forms.ModelForm):
    # # name = forms.CharField()
    # # discription = forms.CharField()
    # # step= forms.CharField()
    # # image=forms.ImageField
    # # author= forms.CharField()
    # # subcategory= forms.CharField()
    # # subcategory = forms.ModelChoiceField(queryset=SubCategories.objects.all(),initial = 1)
    # subcategory =forms.ModelChoiceField(
        
    #     queryset=SubCategories.objects,
    #     label='Подкатегория',
    #     widget=forms.Select)
    class Meta:
        model=Recepts
        fields=(
            "name",
            "discription",
            "step",
            "image",
            "author",
            "subcategory",
        )