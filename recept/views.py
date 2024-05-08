from django.shortcuts import render
from recept.forms import NewRecepts
from recept.models import Categories,SubCategories,Recepts
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def Categorie(request):
    categories=Categories.objects.all()
    subcategories=SubCategories.objects.all()
    context={
        "title":"Категории",
        "categories": categories,
        "subcategories":subcategories
    }
   
    return render(request,'recept/categories.html',context)

def ReceptsList(request,subcategory_slug):
    subcat_id=SubCategories.objects.filter(slug=subcategory_slug)
    
    receptsList=Recepts.objects.filter(subcategory=subcat_id[0])

    context={
        "title":"Рецепты",
        "recepts": receptsList
       
    }
   
    return render(request,'recept/receptlist.html',context)

def Recept(request,recept_slug):
    recept=Recepts.objects.get(slug=recept_slug)
    
    context={
        "title":"Рецептик",
        "recept":recept
    }
    return render(request,'recept/recept.html',context)

def NewRecept(request):
    subcategories=SubCategories.objects.all()
    if request.method=='POST':
        form = NewRecepts(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form=NewRecepts()
    
    context={
        'title':'Новый рецепт',
        'form':form,
        
    }
    return render(request, 'recept/new_recept.html', context)
