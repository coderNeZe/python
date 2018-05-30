from django.db import models

#自定义一个manager,可以对检查的结果进行一个过滤 还可以快速的创建信息
class BookInfoManager(models.Manager):
    def get_queryset(self):
        return super(BookInfoManager,self).get_queryset().filter(isDelete=False)

    def create(self,btitle,bpub_date):
        b = BookInfo()
        b.btitle = btitle
        b.bpub_date = bpub_date
        b.bread = 0
        b.bcommet = 0
        b.isDelete = False
        return b


class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField(db_column='pub_date')
    bread = models.IntegerField(default=0)
    bcommet = models.IntegerField(null=False)
    isDelete = models.BooleanField(default=False)
    class Meta:
        db_table='bookinfo'

    #可以有多个管理器
    book1 = models.Manager()
    book2 = BookInfoManager()

class HeroInfo(models.Model):
    hname=models.CharField(max_length=10)
    hgender = models.BooleanField(default=True)
    hcontent = models.CharField(max_length=1000)
    isDelete = models.BooleanField(default=False)
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)



