from django.db import models

# Create your models here.
class DSignUp(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    course=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    address=models.TextField()

    def __str__(self) -> str:
        return self.course
    
class DTopic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.topic_name
class DWebpage(models.Model):
    topic_name=models.ForeignKey(DTopic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.name
