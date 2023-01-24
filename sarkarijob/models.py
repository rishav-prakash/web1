from django.db import models

class alert(models.Model):
    Alert_id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=50, default='TBA')
    Posts = models.IntegerField(default=100)
    Type = models.CharField(max_length = 40, default = 'vacancy')
    Department = models.CharField(max_length = 50, default = 'Other')
    State = models.CharField(max_length= 25, default = 'Other')
    Group = models.CharField(max_length=1, default='O')
    date_of_issue = models.DateField(default='datetime.auto_now', blank=False)
    last_date = models.DateField(default='TBA', blank=False)
    url = models.URLField(max_length=200, default="www.google.com")
    rf_gen = models.IntegerField(default=0)
    rf_obc = models.IntegerField(default=0)
    rf_scnst = models.IntegerField(default=0)
    important = models.BooleanField(default=1)
    salary = models.CharField(max_length=7 ,default='TBA')
    qualification = models.CharField(max_length=40, default="Intermediate")
    imgcode = models.CharField(max_length=8, default='none')
    
    def __str__ (self):
        return self.Title
    
