from django.db import models

# Create your models here.
class AdmissionEnquiry(models.Model):
    student_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=40,default='')
    phone=models.CharField(max_length=10,default='')
    email=models.CharField(max_length=50,default='')
    For_choice=models.CharField(max_length=15,default='')
    course=models.CharField(max_length=50,default='')
    university=models.CharField(max_length=50,default='')
    address=models.CharField(max_length=100,default='')
    city=models.CharField(max_length=20,default='')
    state=models.CharField(max_length=40, default='')
    zip=models.CharField(max_length=9,default='')

    def __str__(self):
        return self.For_choice+" "+ self.name + " " + self.phone + " " + self.course + ' '+ self.state + ' ' + self.email
