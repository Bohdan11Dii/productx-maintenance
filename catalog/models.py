from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator

class Category(models.Model):
    name = models.CharField(max_length=256)
    
    class Meta:
        ordering = ("name",)
        
    def __str__(self) -> str:
        return self.name
    
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    image = models.ImageField(upload_to='gallery/')
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products"
    )
    quantity = models.IntegerField(default=1)
    
    class Meta:
        ordering = ("name", )
    
    
    def __str__(self) -> str:
        return f"{self.name}"
    
    
    @property
    def is_str(self):
        return range(1, self.quantity + 1)
    
class ProjectUser(AbstractUser):
    pass


class Order(models.Model):
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    phone = models.IntegerField(default=0)
    department = models.TextField(default="")
    order_cart = models.CharField(max_length=256, blank=True, null=True)
    total_amount = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    
    def __str__(self) -> str:
        return f"Замовлення {self.id}"