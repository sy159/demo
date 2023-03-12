from django.contrib.auth.models import User
from django.db import models


class Shop(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("店铺名", max_length=20, null=False, blank=False, help_text="店铺名")
    address = models.CharField("地址", max_length=100, null=True, blank=True, help_text="店铺地址")
    creat_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_constraint=False, help_text="店铺创建人")
    created = models.DateTimeField("新建时间", auto_now_add=True)
    updated = models.DateTimeField("更新时间", auto_now=True)

    # todo 根据需要加扩展字段

    class Meta:
        verbose_name = '店铺信息'
        verbose_name_plural = verbose_name
        db_table = 'shop'

    def __str__(self):
        return f'{self.id}-{self.name}'

    @property
    def create_user_name(self):
        return self.creat_user.username if self.creat_user and self.creat_user.username else ""
