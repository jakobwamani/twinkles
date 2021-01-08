from __future__ import unicode_literals

from django.db import models
from datetime import date
# Create your models here.

class parents(models.Model):

    father_firstname = models.CharField(max_length=100)
    father_lastname = models.CharField(max_length=100)
    father_phonenumber_one = models.IntegerField(default=0)
    father_phonenumber_two = models.IntegerField(default=0)
    mother_firstname = models.CharField(max_length=100)
    mother_lastname = models.CharField(max_length=100)
    mother_phonenumber_one = models.IntegerField(default=0)
    mother_phonenumber_two = models.IntegerField(default=0)
    address = models.CharField(max_length=100)

    # def __str__(self):
    #     return '%s %s %s %s' % (self.father_firstname, self.father_lastname,self.mother_firstname,self.mother_lastname )
        
    def __str__(self):
        return str(self.id)

class children(models.Model):
        #tutorial_category = models.ForeignKey(TutorialCategory, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
    parent = models.ForeignKey(parents,default=1,verbose_name="parent",on_delete=models.SET_DEFAULT)
    firstname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100,blank=True)
    lastname = models.CharField(max_length=100)
    classlevel = models.CharField(max_length=100)
    age = models.IntegerField(default=2)
    time_of_study = models.CharField(max_length=100)
    campus = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.firstname
    def __str__(self):
        return str(self.id)

class payments(models.Model):
    child = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    time = models.DateField(default=date.today)
    bank = models.CharField(max_length=100)
    term = models.IntegerField(default=1)
    year = models.IntegerField(default=0)
    installment = models.IntegerField(default=1)

    def __str__(self):
        return str(self.id)

# class paymentone(models.Model):
#     child = models.OneToOneField(children)
#     amount = models.IntegerField(default=0)
#     time = models.DateField(default=date.today)
#     bank = models.CharField(max_length=100)
#     term = models.IntegerField(default=1)
#     year = models.IntegerField(default=0)

#     def __str__(self):
#         return str(self.id)

# class paymenttwo(models.Model):
#     child = models.OneToOneField(children)
#     amount = models.IntegerField(default=0)
#     time = models.DateField(default=date.today)
#     bank = models.CharField(max_length=100)
#     term = models.IntegerField(default=1)
#     year = models.IntegerField(default=0)

#     def __str__(self):
#         return str(self.id)


# class paymentthree(models.Model):
#     child = models.OneToOneField(children)
#     amount = models.IntegerField(default=0)
#     time = models.DateField(default=date.today)
#     bank = models.CharField(max_length=100)
#     term = models.IntegerField(default=1)
#     year = models.IntegerField(default=0)

#     def __str__(self):
#         return str(self.id)


# class paymentfour(models.Model):
#     child = models.OneToOneField(children)
#     amount = models.IntegerField(default=0)
#     time = models.DateField(default=date.today)
#     bank = models.CharField(max_length=100)
#     term = models.IntegerField(default=1) 
#     year = models.IntegerField(default=0)

#     def __str__(self):
#         return str(self.id)

# class payment(models.Model):
#     paymentone = models.OneToOneField(paymentone)
#     paymenttwo = models.OneToOneField(paymenttwo)
#     paymentthree = models.OneToOneField(paymentthree)
    

#     def __str__(self):
#         return str(self.id)




