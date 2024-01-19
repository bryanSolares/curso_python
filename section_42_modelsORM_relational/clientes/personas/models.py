from django.db import models
from .managers import CustomerManager

# Create your models here.

class BaseData(models.Model):
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Interest(BaseData):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Customer(BaseData):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    interests = models.ManyToManyField(Interest)

    def __str__(self):
        return str(self.id) + " " + self.name + " " + self.last_name

    objects = CustomerManager()
    # CustomerManager()


class CustomerInformation(BaseData):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    country = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    age = models.PositiveIntegerField(default=0)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return str(self.id) + " " + str(self.customer) + " " + self.country + " " + self.nationality


class Specifications(BaseData):
    model = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    cost_per_day = models.FloatField(default=0)
    rent_days = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.id) + " " + self.brand + " " + self.model


class Category(BaseData):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Vehicle(BaseData):
    specifications = models.ForeignKey(Specifications, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + " " + str(self.specifications) + " " + str(self.category)


class Loan(BaseData):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    return_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.id) + " " + str(self.customer) + " " + str(self.vehicle)
