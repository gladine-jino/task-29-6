from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
import random
import string



# Create your models here.
class User(AbstractUser): 
    phone_regex = RegexValidator(regex=r'^[6789]\d{9}$', message="Please enter a valid mobile in 10 digit format")    
    email=models.EmailField(unique=True,null=True,blank=True)
    contact_number=models.CharField(validators=[phone_regex],max_length=17,null=True,unique=True,blank=True)
    address=models.TextField(null=True,blank=True)
    username=models.CharField(max_length=200,blank=True,null=True)
    code = models.CharField(max_length=7, unique=True)

    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def generate_unique_code(cls):
        characters = string.ascii_letters + string.digits  # A-Z, a-z, 0-9
        while True:
            code = ''.join(random.choice(characters) for _ in range(7))
            if not User.objects.filter(code=code).exists():
                return code