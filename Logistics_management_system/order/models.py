from django.db import models

# Create your models here.
class sender_information(models.Model):
    name = models.CharField('姓名',max_length=5)
    telephone = models.CharField('电话',max_length=12)
    city = models.CharField('城市/区域',max_length=20)
    detailed_address = models.CharField('详细地址',max_length=50)
    name_of_company = models.CharField('公司名称',max_length=20)
    order_number = models.CharField('订单号',max_length=12)
    recipient_sender = models.BooleanField('收发件人判断')

    @classmethod
    def add_info(self,recipient_sender,name='',telephone='',city='',detailed_address='',name_of_company='',order_number=''):
        sender_information.objects.create(name=name,telephone=telephone,city=city,detailed_address=detailed_address,
                                          name_of_company=name_of_company,recipient_sender=recipient_sender)



    def __str__(self):
        return '姓名'+ self.name+'电话'+self.telephone+'城市/区域'+self.city+'详细地址'\
               +self.detailed_address+'公司名称'+self.name_of_company+'订单号'+self.order_number+'收发件人判断'+self.recipient_sender

    class Meta:
        db_table = 'rs_info'
        # verbose_name = '收发件人信息'
        # verbose_name_piural = '收发件人信息'

class goods_info(models.Model):
    order_number = models.CharField('订单号', max_length=12)
    specific_goods = models.CharField('具体物品',max_length=20)
    goods_type = models.CharField('物品类别',max_length=5)
    transport_mileage = models.FloatField('运送里程')
    transport_type = models.CharField('运送类别',max_length=5)
    transport_weight = models.FloatField('运送重量')
    transport_volume = models.FloatField('运送体积')

    def __str__(self):
        return '订单号'+ self.order_number+'具体物品'+self.specific_goods+'物品类别'+self.goods_type+'运送里程'\
               +self.transport_mileage+'运送类别'+self.transport_type+'运送重量'+self.transport_weight+'运送体积'+self.transport_volume

    class Meta:
        db_table = 'goods_info'
        # verbose_name = '商品信息'
        # verbose_name_piural = '商品信息'




class transform_info(models.Model):
    the_awb = models.CharField('运单号', max_length=20)
    is_tradition = models.BooleanField('是否交付')
    tradition_id = models.CharField('交付人',max_length=5)
    is_distribution = models.BooleanField('是否确认接收配送')
    distribution_id = models.CharField('接收人',max_length=5)

    def __str__(self):
        return '运单号' + self.the_awb + '是否交付' + self.is_tradition + '交付人' + self.tradition_id + '是否确认接收配送' \
               + self.is_distribution + '接收人' + self.distribution_id
    class Meta:
        db_table = 'tf_info'
        # verbose_name = '运单信息'
        # verbose_name_piural = '运单信息'