from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name = '名称')
    desc = models.CharField(max_length=100, verbose_name = '描述')
    pic = models.ImageField(upload_to='./product', verbose_name = '图片')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '产品'
        verbose_name_plural = '产品'

class CompanyIntro(models.Model):
    desc = models.CharField(max_length=50,verbose_name = '描述')
    pic1 = models.ImageField(upload_to='./companyintro', verbose_name = '图片1')
    pic2 = models.ImageField(upload_to='./companyintro',verbose_name = '图片2')

class HomeBanner(models.Model):
    pic = models.ImageField(upload_to='./homeBanner', verbose_name = '图片')

class SuccessCase(models.Model):
    title = models.CharField(max_length=50, verbose_name = '名称')
    desc = models.CharField(max_length=100, verbose_name = '描述')
    pic = models.ImageField(upload_to='./successcase', verbose_name = '图片')