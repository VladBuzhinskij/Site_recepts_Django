from django.shortcuts import render
from recept.models import SubCategories,Recepts

# Create your views here.

def index (request):
 
    
    receptsList=Recepts.objects.all()[:5]

    context={
        "title":"Рецепты",
        "recepts": receptsList
       
    }

    return render(request,'main/index.html',context)

