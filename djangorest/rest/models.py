from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    draft = models.BooleanField(default=False)
    read_time = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    id = models.AutoField(primary_key=True)
    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-updated", "-created"]

# model web

class Type(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField("Is Active", default=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    type_id = models.ForeignKey(Type, on_delete=models.CASCADE)
    name = models.CharField("Product Name", max_length=200)
    price = models.IntegerField("Price", default=0)
    quantity = models.IntegerField("Quantity", default=0)
    description = models.TextField("Description")    
    
    def __str__(self):
        return self.name

# model core

class FieldPlanningRun(models.Model):
    id = models.IntegerField(primary_key=True)
    last_assigned = models.DateField()
    active_run = models.BooleanField()
    area = models.FloatField()

    def __str__(self):
        return '{} - {}'.format(self.id,self.last_assigned)
        # return str(self.id) + ' ' + str(self.last_assigned)

    class Meta():
        db_table = 'field_planning_run'
