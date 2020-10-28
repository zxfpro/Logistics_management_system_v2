from django.db import models

# Create your models here.


class transfer_station_info(models.Model):

    name = models.CharField('中转站名称',max_length=20)
    transfer_to = models.CharField('相连接中转站',max_length=100)
    user = models.CharField('用户名',max_length=20)
    password = models.CharField('密码',max_length=20)

    class Meta:
        db_table = 'ts_info'


class transfer_info(models.Model):
    the_awb= models.CharField('运单号',max_length=20)
    date= models.DateField('日期',auto_now_add=True)
    next_station = models.CharField('下一站',max_length=20)
    package_complete= models.BooleanField('包裹完整')

    class Meta:
        db_table = 'trans_info'