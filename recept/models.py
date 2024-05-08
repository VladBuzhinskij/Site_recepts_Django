from django.db import models
from django.utils.text import slugify
from services.utils import unique_slugify

class Categories(models.Model):
    name=models.CharField( max_length=150, unique=True
                          ,verbose_name="Название")
    slug=models.SlugField(max_length=200,blank=True,unique=True,verbose_name="URL")
   
    def __str__(self):
        return self.name
    class Meta:
        db_table = "categories"
        verbose_name="Категория"
        verbose_name_plural="Категории"



class SubCategories (models.Model):
    name=models.CharField( max_length=150, unique=False,verbose_name="Названее")
    slug=models.SlugField(max_length=200,blank=True,unique=True,verbose_name="URL")
    category=models.ForeignKey(to=Categories, verbose_name=("Категория"), on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "subcategory"
        verbose_name="Податегория"
        verbose_name_plural="Подкатегории"

class Recepts(models.Model):
    name=models.CharField( max_length=150, unique=True
                          ,verbose_name="Названее")
    slug=models.SlugField(max_length=200,blank=True,unique=True,verbose_name="URL")
    discription=models.TextField(blank=True,null=True, verbose_name="Описание")
    step=models.TextField(verbose_name="Шаги")
    image=models.ImageField(upload_to="receptss",blank=True,null=True, verbose_name="Изображение")
    author=models.CharField( max_length=150, verbose_name="Автор")
    subcategory=models.ForeignKey(to=SubCategories, verbose_name=("Податегория"), on_delete=models.CASCADE)

    

    def save(self, *args, **kwargs):
        """
        Сохранение полей модели при их отсутствии заполнения
        """
        if not self.slug:
            self.slug = unique_slugify(self, self.name)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name

    def get_price(self):
        return self.price

    class Meta:
        db_table = "recept"
        verbose_name="Рецепт"
        verbose_name_plural="Рецепты"
        ordering=("id",)