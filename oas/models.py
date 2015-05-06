from django.db import models

class Javaseer(models.Model):
  StudentID = models.CharField(max_length=30)
  StudentName = models.CharField(max_length=50)
  JavacCall = models.CharField(max_length=100)
  TimeStamp = models.DateTimeField()
  JavaProgram = models.TextField()
  JavaCompilerOutput = models.TextField()

  def __unicode__(self):
    return self.StudentID + ': ' + self.JavacCall + " -  " + self.TimeStamp.strftime("%m.%d.%Y %H:%M:%S")

class Chirp(models.Model):
  StudentID = models.CharField(max_length=30)
  StudentName = models.CharField(max_length=50)
  JavacCall = models.CharField(max_length=100)
  TimeStamp = models.DateTimeField()
  JavaProgram = models.TextField()
  JavaCompilerOutput = models.TextField()
  NumCompiles = models.IntegerField()

  def __unicode__(self):
    return self.StudentID + ': ' + self.JavacCall + " -  " + self.TimeStamp.strftime("%m.%d.%Y %H:%M:%S")

class ChirpRun(models.Model):
  StudentID = models.CharField(max_length=30)
  StudentName = models.CharField(max_length=50)
  ClassName = models.CharField(max_length=50)
  MethodName = models.CharField(max_length=50)
  ObjectName = models.CharField(max_length=50)
  Parameters = models.CharField(max_length=100)
  Result = models.TextField()
  TimeStamp = models.DateTimeField()

  def __unicode__(self):
    return self.StudentID + ' - ' + self.ClassName + " -  " + self.TimeStamp.strftime("%m.%d.%Y %H:%M:%S")

class PencilCodeEvent(models.Model):
  StudentID = models.CharField(max_length=30)
  Assignment = models.CharField(max_length=30)
  ProjectName = models.CharField(max_length=50)
  TimeStamp = models.DateTimeField()
  Condition = models.CharField(max_length=30) # study condition -> (block, text, hybrid)
  EditorMode = models.CharField(max_length=30) # state of droplet UI -> (blocks, text, text-with-palette)
  EventType = models.CharField(max_length=30) # (textInput, mouseInput, run, close)
  Program = models.TextField()
  FloatingBlocks = models.TextField()
  ProjectHTML = models.TextField()
  ProjectCSS = models.TextField()
  
  def __unicode__(self):
    return self.StudentID + ': ' + self.Assignment + " @ " + self.TimeStamp.strftime("%m.%d.%Y %H:%M:%S") + " - " + self.Program
