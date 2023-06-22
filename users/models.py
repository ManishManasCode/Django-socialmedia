from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class UsersProfileModel(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name="user_profile_model_user")
    first_name = models.CharField(max_length=100,null=True,blank=True)
    last_name= models.CharField(max_length=100,null=True,blank=True)
    profile_pic=models.ImageField(upload_to="user-profile/",null=True,blank=True)
    bio = models.TimeField(null=True,blank=True)
    date_of_birth=models.DateTimeField(null=True,blank=True)

    facebook = models.URLField(null=True, blank=True) 
    linkedin = models.URLField(null=True, blank=True)
    whatapp = models.URLField(null=True, blank=True)
    email = models.EmailField(max_length=100,null=True,blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name