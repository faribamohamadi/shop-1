from django.contrib.auth.models import User
from django.db import models

from store.models import Store


class Category(models.Model):
    """ مدل دسته بندی """
    name = models.CharField(max_length=200)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, db_constraint=False,default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CategryFeature(models.Model):
    """ ویژگی دسته بندی  """
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class CategoryFeatureValue(models.Model):
    """ مقادیر ویژگی دسته بندی """
    value = models.CharField(max_length=200)
    category_feature = models.ForeignKey(CategryFeature, on_delete=models.CASCADE)


class Product(models.Model):
    """ مدل محصولات """
    name = models.CharField(max_length=200)
    title = models.TextField()
    description = models.TextField(null=True)
    main_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, related_name='category_id')
    view = models.IntegerField(default=0)
    meta1 = models.CharField(max_length=200, null=True)
    meta2 = models.CharField(max_length=200, null=True)
    meta3 = models.CharField(max_length=200, null=True)
    like = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    has_color = models.BooleanField(default=False)


class ProductStore(models.Model):
    """ محصولات مرتبط به فروشگاه """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField(default=0)


class Color(models.Model):
    """ رنگ محصول """
    color = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    product_store = models.ForeignKey(ProductStore, on_delete=models.CASCADE)
    color_price = models.IntegerField(default=0)
    quantity = models.IntegerField()


class Warranty(models.Model):
    """ گارانتی محصول """
    warranty_price = models.IntegerField(default=0)
    product_store = models.ForeignKey(ProductStore, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    icon = models.ImageField(null=True)


class Comment(models.Model):
    """ نظرات کاربران """
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    star = models.IntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
