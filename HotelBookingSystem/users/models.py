from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):

    USER_ROLES = [
        ('sys_admin', 'System Admin'),
        ('norm_user', 'Client')
    ]
   # username = models.CharField(max_length=12,unique=False,default="",null=True)
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    email = models.EmailField(unique=True, null=True)
    profile_pic = models.ImageField(null=True, blank=True, default='avatar.svg')
    date_of_birth = models.DateField(blank=True,null=True)
    user_role = models.CharField(max_length=20, choices=USER_ROLES, default="norm_user")

    
    
    
    def save(self, *args, **kwargs) -> None:
        self.username = f"{self.first_name}_{self.last_name}"
        if self.phone_number:
            if self.phone_number.startswith('0'):
                self.phone_number = '+26' + self.phone_number
        return super().save(*args, **kwargs)
    
    
 
