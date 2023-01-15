from django.db import models

# Create your models here.
class Customer(models.Model):
    cid = models.CharField(max_length=100, null=True, blank=True, unique=True)
    ctitle = models.CharField(max_length=4)
    cname = models.CharField(max_length=255)
    cclub = models.CharField(max_length=255)
    ccno = models.CharField(max_length=8, default='04359862')
    ccexp = models.CharField(max_length=5, default='02/27')
    cdiscount = models.BooleanField(default=False)

    def __str__(self):
        return self.cname
