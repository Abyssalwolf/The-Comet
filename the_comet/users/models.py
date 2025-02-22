from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, org_name, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, org_name=org_name)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
class CustomerUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    org_name = models.CharField(max_length=255)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['org_name']
    
    def __str__(self):
        return self.email
    
class CustomerProfile(models.Model):
    user = models.OneToOneField(CustomerUser, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Profile of {self.user.email}"
