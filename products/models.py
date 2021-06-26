from django.contrib.auth.models import User
from django.db import models

from store.models import Store


class Category(models.Model):
    """ مدل دسته بندی """
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, db_constraint=False, default=0)
    img = models.ImageField(null=True)
    icon = models.CharField(max_length=200, null=True)
    meta1 = models.CharField(max_length=200, null=True)
    meta2 = models.CharField(max_length=200, null=True)
    meta3 = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CategryFeature(models.Model):
    """ ویژگی دسته بندی  """
    name = models.CharField(max_length=200)
    filter = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CategoryFeatureValue(models.Model):
    """ مقادیر ویژگی دسته بندی """
    value = models.CharField(max_length=200)
    category_feature = models.ForeignKey(CategryFeature, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Warranty(models.Model):
    """ گارانتی محصول """
    warranty_price = models.IntegerField(default=0)
    product_store = models.ForeignKey(ProductStore, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    img = models.ImageField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    """ نظرات کاربران """
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    star = models.IntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class FeedbackField(models.Model):
    """ به چی رای بدیم؟ #نه_به_جمهوری_اسلامی_ایران """
    name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Feedback(models.Model):
    """ میزان رای ملت است امام (ره)  """
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user')
    value = models.IntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='product')
    field = models.ForeignKey(FeedbackField, on_delete=models.CASCADE,related_name='field')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Image(models.Model):
    img = models.ImageField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cover = models.BooleanField(default=False)
    alt = models.CharField(null=True,max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
