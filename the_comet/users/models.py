from django.db import models
from django.conf import settings
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

class Event(models.Model):
    eventid = models.AutoField(primary_key=True)
    email = models.EmailField()
    title = models.CharField(max_length=255)
    description = models.TextField()

    collaborator_email_1 = models.EmailField(blank=True, null=True)
    collaborator_email_2 = models.EmailField(blank=True, null=True)

    venue = models.CharField(max_length=255)  
    location = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    registration_fee = models.TextField(blank=True, null=True)

    sponsor_1_title = models.CharField(max_length=255, blank=True, null=True)
    sponsor_1_name = models.CharField(max_length=255, blank=True, null=True)
    sponsor_1_image = models.ImageField(upload_to='sponsor_images/', blank=True, null=True)

    sponsor_2_title = models.CharField(max_length=255, blank=True, null=True)
    sponsor_2_name = models.CharField(max_length=255, blank=True, null=True)
    sponsor_2_image = models.ImageField(upload_to='sponsor_images/', blank=True, null=True)

    sponsor_3_title = models.CharField(max_length=255, blank=True, null=True)
    sponsor_3_name = models.CharField(max_length=255, blank=True, null=True)
    sponsor_3_image = models.ImageField(upload_to='sponsor_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.date}"
