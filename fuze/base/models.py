from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

User = get_user_model()
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to Django's User model
    id_user=models.IntegerField()
    bio =models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pic',default='blank-profile-picture.png')
   
    

    def __str__(self):
        return self.user.username


    
