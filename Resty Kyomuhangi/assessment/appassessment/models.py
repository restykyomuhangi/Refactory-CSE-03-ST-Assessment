from django.db import models
from django.core.validators import MinLengthValidator
from django.utils import timezone

# Create your models here.
class Registration(models.Model):
    firstname = models.CharField(max_length=50, validators=[MinLengthValidator(3)])
    lastname = models.CharField(max_length=50, validators=[MinLengthValidator(3)])
    course = models.CharField(max_length=100, choices=(('Cetificate in Health Science','Cetificate in Health Science'),('Certificate in Applied Technology','Certificate in Applied Technology'),('Bachelor of Information Technology','Bachelor of Information Technology'), ('Bachelors in Business Technology','Bachelors in Business Technology'),('Master of Public Health','Master of Public Health')))
    entryscheme = models.CharField(max_length=100 , choices=(('A-Level certificate','A-Level certificate'), ('Adult/Mature Learning','Adult/Mature Learning'),('Certificate','Certificate'),('Diploma','Diploma'),('Bachelors','Bachelors')))
    intake = models.CharField(max_length=50, choices=(('January Intake','January Intake'),('May Intake','May Intake'),('August Intake','August Intake')))
    sponsorship = models.CharField(max_length=50, choices=(('Private','Public'),('Government',' Government'),('Bursary','Bursary')))
    gender = models.CharField(max_length=10, choices=(('Male','Male'),('Female','Female')))
    dob = models.DateField(default=timezone.now)
    residence = models.CharField(max_length=255,validators=[MinLengthValidator(2)] )

    def __str__(self):
        return self.firstname + " " + self.lastname
