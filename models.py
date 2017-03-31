from django.db import models

class student_data(models.Model):
    roll_no = models.AutoField(primary_key=True)
    stud_name = models.TextField(max_length=200)
    stud_sub1= models.FloatField()
    stud_sub2= models.FloatField()
    stud_sub3= models.FloatField()
    stud_sub4= models.FloatField()
    stud_sub5= models.FloatField()
    stud_avg= models.FloatField()
