from django.db import models # type: ignore


class Salary(models.Model):
    amount = models.IntegerField(blank=False, null=False)
    extra_december = models.BooleanField(default=False)
    extra_june = models.BooleanField(default=False)
    
    def __str__(self):
        return self.amount 

class Job(models.Model):
    title = models.CharField(max_length=15, blank=False, null=False)
    job_description = models.TextField(max_length=100, blank=True, null=False)
    salary = models.ForeignKey(Salary, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title  

    
class Country(models.Model):
    name = models.CharField(max_length=10, blank=False, null=False)
    country_code = models.CharField(max_length=10, blank=False, null=False)
    
    def __str__(self):
        return self.name
        

class Location(models.Model):
    city_name = models.CharField(max_length=50, blank=False, null=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.city


class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    Zip_code = models.CharField(max_length=50)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name    
    
    
class Employee(models.Model):
    id_number = models.CharField(max_length=10, blank=False,null=False, unique=True)
    name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField(max_length=30, blank=False, null=False)
    address = models.CharField(max_length=50, blank=False, null=False)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name     