from django.db import models  
class Employee(models.Model):  
    eid = models.CharField(max_length=25)  
    ename = models.CharField(max_length=250)  
    eemail = models.CharField(max_length=250)  
    econtact = models.CharField(max_length=250) 
    edistri = models.CharField(max_length=250)
    ecolor = models.CharField(max_length=250)

    def __str__(self):
        return "%s " %(self.ename) 
    class Meta:  
        db_table = "employee"  