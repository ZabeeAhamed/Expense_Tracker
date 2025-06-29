from django.db import models

# Create your models here.
class Currentbalance(models.Model):
    currentbalance=models.FloatField(default = 0)


class TrackingHistory(models.Model):
    currentbalance=models.ForeignKey(Currentbalance,on_delete=models.CASCADE)
    amount=models.FloatField()
    choices=(('CREDIT','CREDIT'),('DEBIT','DEBIT'))
    expensestype=models.CharField(choices,max_length=200)
    description=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now=True)
    created_at=models.DateTimeField(auto_now_add=True)
