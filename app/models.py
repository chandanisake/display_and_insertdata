from django.db import models

# Create your models here.

class Topic(models.Model):
    topicname=models.CharField(max_length=100,primary_key=True)

    def __str__(self) -> str:
        return self.topicname

class Webpage(models.Model):
    topicname=models.ForeignKey(Topic,on_delete=models.CASCADE)#this modelsname inherite by Topic(parent table)if u delete the parent table data it will delete there respect to child table data also.
    name=models.CharField(max_length=100)
    url=models.URLField()
    
    def __str__(self) -> str:
        return self.name


class AccessRecord(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date=models.DateField()
    author=models.CharField(max_length=100)


    def __str__(self) -> str:
        return self.author

