from django.db import models
from django.contrib.auth.models import User

# Create your models here.

DIVISION_CHOOSE=(
    ('Dhaka','Dhaka'),
    ('Tangail','Tangail'),
    ('Gazipur','Gazipur'),
    ('Rangpur','Rangpur'),
    ('Khulna','Khulna'),
    ('Barisal','Barisal'),
    ('shaerpur','shaerpur'),
)

class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    division=models.CharField(choices=DIVISION_CHOOSE,max_length=50)
    distract=models.CharField(max_length=50)
    thana=models.CharField(max_length=50)
    villageroad=models.CharField(max_length=100)
    zipcoe=models.IntegerField()

    def __str__(self):
        return self.name
    


CATEGORTY_CHOOSE=(
    ('L','Lehenga'),
    ('s','Saree'),
    ('Gp','Gents Pant'),
    ('Sh','TShart'),
    ('Lp','Laptop'),
)
    

class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_prices=models.FloatField()
    discount_prices=models.FloatField()
    description=models.TextField()
    brand=models.CharField(max_length=50)
    categorty=models.CharField(choices=CATEGORTY_CHOOSE,max_length=2)
    product_image=models.ImageField(upload_to='Image')

