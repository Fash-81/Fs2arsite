from django.db import models
from django.contrib.auth.models import User



class Portfolio(models.Model):
    FORMAT_CHOICES = [
        ('پوستر' , 'پوستر'),
        ('بنر' , 'بنر'),
        ('بیزینس کارت' , 'بیزینس کارت'),
        ('لوگو','لوگو'),
        ('وکتور','وکتور')
    ]
    creator= models.ForeignKey(User,related_name='Portfolios', on_delete=models.SET_NULL,null=True,blank=True )
    case = models.CharField(max_length=50, choices=FORMAT_CHOICES)
    topic = models.CharField(max_length=50)
    subject=models.CharField(max_length=50)
    content = models.TextField(null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    created_at= models.DateField(auto_now_add=True)
    p_image= models.ImageField(upload_to='p/',null=True,blank=True)

class Order(models.Model):
    FORMAT_CHOICES = [
        ('پوستر' , 'پوستر'),
        ('بنر' , 'بنر'),
        ('بیزینس کارت' , 'بیزینس کارت'),
        ('لوگو','لوگو')
    ]
    customer = models.ForeignKey(User,related_name='Orders', on_delete=models.SET_NULL, null=True,blank=True)
    case = models.CharField(max_length=50, choices=FORMAT_CHOICES)
    topic = models.CharField(max_length=50)
    subject=models.CharField(max_length=50)
    content = models.TextField(null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    created_at= models.DateField(auto_now_add=True)
    o_image= models.ImageField(upload_to='o/',null=True,blank=True)

