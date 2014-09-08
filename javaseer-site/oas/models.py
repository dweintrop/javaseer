from django.db import models

class Javaseer(models.Model):
  StudentID = models.CharField(max_length=30)
  StudentName = models.CharField(max_length=50)
  JavacCall = models.CharField(max_length=100)
  TimeStamp = models.DateTimeField()
  JavaProgram = models.TextField()
  JavaCompilerOutput = models.TextField()
  NumRuns = models.IntegerField()

  def __unicode__(self):
    return self.StudentID + ': ' + JavacCAll + " -  " + self.TimeStamp.strftime("%m.%d.%Y %H:%M:%S")
