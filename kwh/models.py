from django.db import models
from django.db.models import UniqueConstraint


class FemsPayload(models.Model):
    payload_id = models.AutoField(primary_key=True)
    site = models.ForeignKey('FemsTrans', related_name='siteid', on_delete=models.DO_NOTHING)
    dev_id = models.ForeignKey('FemsTrans',to_field='dev_id',related_name='devid',on_delete= models.DO_NOTHING,db_column='dev_id')
    dev_time = models.ForeignKey('FemsTrans',to_field='dev_time',related_name='devtime' ,on_delete= models.DO_NOTHING, db_column='dev_time')
    payload_data = models.TextField()

    class Meta:
        db_table = 'fems_payload'

class FemsTrans(models.Model):
    site_id = models.CharField(primary_key=True, max_length=15)
    dev_id = models.CharField(max_length=128,unique=True)
    transaction_id = models.CharField(max_length=20)
    dev_time = models.CharField(max_length=128,unique=True)
    eng_type = models.IntegerField()
    version = models.CharField(max_length=128)

    class Meta:
        db_table = 'fems_trans'
        managed = False