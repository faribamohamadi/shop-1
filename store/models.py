from django.contrib.auth.models import User
from django.db import models


class Store(models.Model):
    """  مدل فروشگاه  """
    name = models.CharField(max_length=200)
    title = models.TextField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=False)
    icon = models.ImageField(null=True)
    active = models.BooleanField(default=False)
    state = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Field(models.Model):
    """  اطلاعات و مدارک فروشگاه """
    name = models.CharField(max_length=200)
    title = models.TextField(null=True)
    description = models.TextField(null=True)
    type = models.CharField(default='text', max_length=200)
    null = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    """ نظرات کاربران """
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_id')
    star = models.IntegerField(default=0)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class FeedbackField(models.Model):
    """ به چی رای بدیم؟ #نه_به_جمهوری_اسلامی_ایران """
    name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Feedback(models.Model):
    """ میزان رای ملت است امام (ره)  """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.IntegerField(default=0)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    field = models.ForeignKey(FeedbackField, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)