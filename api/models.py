from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.name)


class Car(models.Model):
    vin_number = models.CharField(max_length=17)
    registration = models.CharField(max_length=10)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    service_date = models.DateField()
    owner = models.CharField(max_length=50)
    owner_phone_number = models.CharField(max_length=13)

    def __str__(self):
        return f"{self.make} {self.model} {self.year} {self.owner} {self.registration}"


class History(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    repair_log = models.TextField()
    date_of_repair = models.DateField()

    def __str__(self):
        return f"{self.employee} {self.date_of_repair}"
