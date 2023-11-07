from django.db import models

# Create your models here.
class studentsection(models.Model):
    num=models.AutoField(primary_key=True)
    registration=models.CharField(max_length=20)
    stage1=models.CharField(max_length=20)
    stage2=models.CharField(max_length=20)
    stage3=models.CharField(max_length=20)
    stage4=models.CharField(max_length=20)
    stage5=models.CharField(max_length=20)

    def __str__(self):
        return self.registration+"----------"+self.stage1+"----------" +self.stage2+"----------" +self.stage3+"----------" +self.stage4+"----------" +self.stage5
    