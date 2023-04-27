from django.db import models  
class Employee(models.Model):  
    epaciente = models.CharField(max_length=250)  
    efechahora = models.DateTimeField()  
    emedico = models.CharField(max_length=250) 
    edistri = models.CharField(max_length=250)
    ecolor = models.CharField(max_length=250)
    eid = models.CharField(max_length=50)

    def __str__(self):
        return "%s " %(self.epaciente) 
    class Meta:  
        db_table = "citas"  