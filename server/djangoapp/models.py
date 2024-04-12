# Uncomment the following imports before adding the Model code

from django.db import models

# from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


# <HINT> Create a Car Make model `class CarMake(models.Model)`:
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    # - Type (CharField with a choices argument to provide limited choices
    CAR_TYPES = [
        ("TRUCK", "Truck"),
        ("SUV", "SUV"),
        ("HATCHBACK", "Hatchback"),
        ("SEDAN", "Sedan"),
        ("WAGON", "Wagon"),
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default="SUV")
    # - Year (IntegerField) with min value 2015 and max value 2023
    year = models.IntegerField(
        default=2024,
        validators=[
            MaxValueValidator(2024),
            MinValueValidator(2012)
        ]
    )

    def __str__(self):
        return f"{self.car_make.name} {self.name}"
