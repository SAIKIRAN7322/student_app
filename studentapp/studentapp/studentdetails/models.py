from django.db import models

from .utils import gradesenumtypes


class studentdetailsStudentModel(models.Model):
    gender = (("Male", "Male"),
              ('Female', 'Female'),
              ('Others', "Others"))
    Name = models.CharField(max_length=100)
    Date_Of_Birth = models.DateField()
    Gender = models.CharField(max_length=20, choices=gender)
    Image = models.ImageField(upload_to="student/image", blank=True)
    createddate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Name
    # class Meta:
    #     verbose_name = "Student Model"

class studentdetailsStudentMainMarksModel(models.Model):
    Sem = ((1, "I"), (2, "II"), (3, "III"), (4, "IV"), (5, "V"), (6, "VI"), (7, "VII"), (8, "VIII"))
    owner = models.ForeignKey(studentdetailsStudentModel, on_delete=models.CASCADE,related_name="studentdetailsstudentmainmarksModel_owner")
    Grade = models.CharField(max_length=10, choices=gradesenumtypes.choices())
    Sem = models.IntegerField(choices=Sem)
    createddate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.owner

    # class Meta:
    #     verbose_name = "Student Mark Model"
    #

class studentdetailsStudentMainModel(models.Model):
    branch = (("IT", "IT"), ("CSE", "CSE"), ("ECE", "ECE"), ("MECH", "MECH"), ("CIVIL", "CIVIL"))
    Owner = models.OneToOneField(studentdetailsStudentModel, on_delete=models.CASCADE,related_name="studentdetailsstudentmainModel_owner")
    Marks = models.ManyToManyField(studentdetailsStudentMainMarksModel)
    Branch = models.CharField(max_length=30, choices=branch)
    createddate = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     verbose_name = "Student Main Model"






