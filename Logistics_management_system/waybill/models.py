from django.db import models

# Create your models here.

class waybill(models.Model):
    the_awb= models.CharField('运单号',max_length=20)
    provenance= models.CharField('发出地',max_length=20)
    the_goods_to= models.CharField('收货地',max_length=20)
    goods_type= models.CharField('物品类别',max_length=5)
    next_transfer_station= models.CharField('下一中转站',max_length=20)
    date= models.DateField('日期',auto_now=True)
    complete_delivery= models.BooleanField('完整送达')
