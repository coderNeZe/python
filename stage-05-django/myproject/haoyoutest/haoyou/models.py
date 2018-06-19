from django.db import models

class userInfo(models.Model):
    userID = models.IntegerField(default=0)
    uname = models.CharField(max_length=20)
    class Meta:  #在模型类中定义类Meta，用于设置元信息
        db_table='userInfo'  #改变表的名字


class guanzhuInfo(models.Model):
    friendid = models.IntegerField("关注",default=0,null=True)
    unfriendid = models.IntegerField("黑名单",default=0,null=True)
    report = models.IntegerField("举报",default=0,null=True)
    myselfID = models.ForeignKey(userInfo,on_delete=models.CASCADE,db_column='userID')
    class Meta:  #在模型类中定义类Meta，用于设置元信息
        db_table='guanzhuInfo'  #改变表的名字



