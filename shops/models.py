from django.db import models


class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Street(models.Model):
    name = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE)


class Shop(models.Model):
    name = models.CharField(max_length=50)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    home = models.PositiveIntegerField()
    open_time = models.TimeField()
    close_time = models.TimeField()

    def __str__(self):
        return self.name
