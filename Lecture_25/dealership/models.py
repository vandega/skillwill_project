from django.db import models


class Brand(models.Model):
    brand_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.brand_name}'


class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='cars')
    car_model = models.CharField(max_length=100, default='unknown')
    speed = models.IntegerField()
    picture = models.ImageField(upload_to='car_pictures/', blank=True, null=True)  # Use ImageField for storing pictures

    def __str__(self) -> str:
        return f'{self.brand} {self.car_model}'


class Dealer(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birth_day = models.DateField()
    dealer_of = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.name} {self.surname}, dealer of {self.dealer_of}'