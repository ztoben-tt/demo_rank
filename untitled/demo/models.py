from django.db import models


class ScoreModel(models.Model):
    user_id = models.CharField(verbose_name='客户端号', max_length=16, unique=True)
    score = models.IntegerField(verbose_name='分数', default=1)

    class Meta:
        verbose_name = '分数登记表'
        verbose_name_plural = verbose_name
