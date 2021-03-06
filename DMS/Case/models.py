from django.db import models


class Case(models.Model):
    """病例信息"""
    id = models.AutoField(primary_key=True, verbose_name=u'唯一主键')
    pathology = models.CharField(max_length=128, verbose_name=u'病理号', null=True, blank=True)
    diagnosis_label_doctor = models.CharField(max_length=64, verbose_name=u'医生诊断标签', null=True, blank=True)
    waveplate_source = models.CharField(max_length=64, verbose_name=u'片源', null=True, blank=True)
    making_way = models.CharField(max_length=64, verbose_name=u'切片制式', null=True, blank=True)
    check_date = models.CharField(max_length=128, verbose_name=u'采样/检查时间', blank=True, null=True)
    diagnosis_date = models.CharField(max_length=128, verbose_name=u"诊断时间", blank=True, null=True)
    last_menstruation = models.CharField(max_length=128, verbose_name=u'末次经期时间', blank=True, null=True)
    clinical_observed = models.CharField(max_length=256, verbose_name=u"临床所见", null=True, blank=True)
    diagnosis_label_doctor_filter = models.CharField(max_length=64, verbose_name=u'医生诊断标签筛选', null=True, blank=True)

    is_delete = models.BooleanField(verbose_name='是否逻辑删除', default=False)
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name=u'更新时间', auto_now=True)

    class Meta:
        db_table = 'tb_case_info'  # 自定义数据库表的名称
        verbose_name = '病例信息'  # 在后台admin中显示表的中文名
        verbose_name_plural = verbose_name

    def __str__(self):
        return '病理号为：%s, 诊断标签为：%s' % (self.pathology, self.diagnosis_label_doctor)
