from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User(models.Model):
    """ username = models.CharField(max_length=30, verbose_name="Nombre de usuario")
    last_name = models.CharField(max_length=30,verbose_name="Apellido paterno",blank=True, null=True,default = "")    
    password = models.CharField(max_length=40, verbose_name="Contraseña")
    email = models.EmailField(verbose_name = "Correo electrónico") """
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,default = None)
    age = models.IntegerField(blank=True, null=True, verbose_name="Edad", default = 0)
    ci = models.CharField(max_length=30,default="")
    # para la parte de los videos
    last_video_color = models.IntegerField(default = 0)

    has_been_tested_color = models.BooleanField(default = False,blank=True, null=True)

    last_video_abc = models.IntegerField(default = 0)

    has_been_tested_abc = models.BooleanField(default = False)
    last_video_simple_phrases = models.IntegerField(default = 0)


    has_been_tested_simple_phrases = models.BooleanField(default = False)

    last_video_simple_words = models.IntegerField(default = 0)

    has_been_tested_simple_words = models.BooleanField(default = False)

    #Planes

    plan = models.IntegerField(default = 0)