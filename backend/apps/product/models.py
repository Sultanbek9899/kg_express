
from django.db import models

from backend.apps.accounts.models import User


# Create your models here.
# PRODUCT MODELS

class Category(models.Model):
    name = models.CharField("Название", max_length=50, unique=True)
    slug = models.SlugField("Слаг", max_length=60, unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['name']
    
    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE,
        related_name="subcategories"
    )
    name = models.CharField("Название", max_length=70, unique=True)
    slug = models.SlugField("Слаг", max_length=80, unique=True)

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"
        ordering = ['category', 'name']


    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField("Название", max_length=255)
    description = models.TextField("Описание")
    price = models.DecimalField(
        "Цена", 
        max_digits=10, 
        decimal_places=2
        )
    image = models.ImageField("Фото", upload_to="product_images/")
    category = models.ForeignKey(
        Category, 
        on_delete=models.PROTECT,
        related_name="products"
        )
    subcategory = models.ForeignKey(
        SubCategory, 
        on_delete=models.PROTECT,
        related_name="products"
        )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField("Активный", default=True)
    
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['-created']
    
    def __str__(self):
        return self.name





class Product(models.Model):
    name = models.CharField()
    category = models.ManyToManyField(
        Category,related_name="products")
    SubCategory = models.ManyToManyField(SubCategory)