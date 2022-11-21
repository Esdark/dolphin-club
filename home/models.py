import datetime
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from dolphin.settings import MEDIA_ROOT
import os
from django.core.exceptions import ValidationError
# Create your models here.
def validate_image(fieldfile_obj):
    filesize = fieldfile_obj.file.size
    megabyte_limit = 2.0
    if filesize > megabyte_limit*1024*1024:
        raise ValidationError("Max file size is %sMB" % str(megabyte_limit))



# class GalleryPageMaster(models.Model):
#     contentid = models.AutoField(primary_key=True)
#     Description = models.TextField(null=True,blank=True)
#     Datemodified =  models.DateField(auto_now_add=True)
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     display = models.CharField(max_length=1,default='Y',choices=[('Y','Y'),('N','N')])
#     displayorder = models.IntegerField(default=1)
#     upload = models.ImageField(upload_to ='uploads/',validators=[validate_image], blank=True, null=True,help_text='Maximum file size allowed is 2Mb')

#     class Meta:
#         db_table = "GalleryPageMaster"
#     def __str__(self):
#         return self.Description +' - '+str(self.displayorder)


# class MailLinkMaster(models.Model):
#     id = models.AutoField(primary_key=True)
#     url = models.TextField(null=True,blank=True)
#     class Meta:
#         db_table = "MailLinkMaster"
#     def __str__(self):
#         return 'Mail'


class MaterialMaster(models.Model):
    materialid = models.AutoField(primary_key=True)
    materialname = models.CharField(max_length =100)
    position = models.IntegerField(default=1)
    hide = models.CharField(max_length =1,default='N',choices=[('Y', 'Y'), ('N', 'N')])
    Datemodified =  models.DateField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table = "MATERIALMASTER"
    def __str__(self):
        return self.materialname

class AgeMaster(models.Model):
    ageid = models.AutoField(primary_key=True)
    description = models.CharField(max_length =100)
    position = models.IntegerField(default=1)
    hide = models.CharField(max_length =1,default='N',choices=[('Y', 'Y'), ('N', 'N')])
    Datemodified =  models.DateField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table = "AGEMASTER"
    def __str__(self):
        return self.description

class ProductMaster(models.Model):
    productid = models.CharField(primary_key=True,max_length=50)
    name = models.CharField(max_length =100)
    Description = models.TextField(null=True,blank=True)
    material =  models.ForeignKey(MaterialMaster,on_delete=models.CASCADE)
    position = models.IntegerField(default=1)
    hide = models.CharField(max_length =1,default='N',choices=[('Y', 'Y'), ('N', 'N')])
    Datemodified =  models.DateField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    productimage = models.ImageField(upload_to ='uploads/',validators=[validate_image], blank=True, null=True,help_text='Maximum file size allowed is 2Mb')
    price = models.DecimalField(max_digits=5, decimal_places=2,default=0)

    class Meta:
        db_table = "PRODUCTMASTER"
    def __str__(self):
        return self.productid+' '+self.name
    def save(self, *args, **kwargs):
        
        try:
            if self.productid:
                productid_instance = ProductMaster.objects.get(productid = self.productid)
                if productid_instance.upload != self.upload:
                    try:
                        os.remove(MEDIA_ROOT+str(productid_instance.upload))
                    except:
                        pass
        except:
            pass
        super().save(*args, **kwargs)


class ProductAgeWiseList(models.Model):
    productid = models.ForeignKey(ProductMaster,on_delete=models.CASCADE)
    age =  models.ForeignKey(AgeMaster,on_delete=models.CASCADE)
    position = models.IntegerField(default=1)
    hide = models.CharField(max_length =1,default='N',choices=[('Y', 'Y'), ('N', 'N')])
    stock = models.CharField(max_length =1,default='Y',choices=[('Y', 'Y'), ('N', 'N')])
    Datemodified =  models.DateField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    class Meta:
        db_table = "PRODUCTAGEWISELIST"
        unique_together = ('productid','age')
    def __str__(self):
        return str(self.productid)+' '+self.productid.name+" - "+ self.age.description 
    