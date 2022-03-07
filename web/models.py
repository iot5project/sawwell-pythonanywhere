from django.db import models


class Cust(models.Model):
    custno = models.IntegerField(primary_key=True)
    id = models.CharField(max_length=30, blank=True, null=True)
    password = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    regdate = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'cust'


class Categori(models.Model):
    cid = models.IntegerField(primary_key=True)
    categoriname = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'categori'


class Food(models.Model):
    foodid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    regdate = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'food'


class Market(models.Model):
    marketno = models.IntegerField(primary_key=True)
    cid = models.ForeignKey(Categori, models.DO_NOTHING, db_column='cid')
    foodid = models.ForeignKey(Food, models.DO_NOTHING, db_column='foodid')
    marketname = models.CharField(max_length=100, blank=True, null=True)
    marketaddress = models.CharField(max_length=100, blank=True, null=True)
    regdate = models.DateField(blank=True, null=True)
    open = models.TimeField(blank=True, null=True)
    close = models.TimeField(blank=True, null=True)
    holiday = models.DateField(blank=True, null=True)
    hit = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'market'


class Ceo(models.Model):
    ceoid = models.IntegerField(primary_key=True)
    marketno = models.ForeignKey('Market', models.DO_NOTHING, db_column='marketno')
    id = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'ceo'


class Reply(models.Model):
    replyid = models.IntegerField(primary_key=True)
    reviewno = models.ForeignKey('Review', models.DO_NOTHING, db_column='reviewno')
    ceoid = models.ForeignKey(Ceo, models.DO_NOTHING, db_column='ceoid')
    content = models.CharField(max_length=100, blank=True, null=True)
    regdate = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'reply'


class Review(models.Model):
    reviewno = models.IntegerField(primary_key=True)
    marketno = models.ForeignKey(Market, models.DO_NOTHING, db_column='marketno')
    custno = models.ForeignKey(Cust, models.DO_NOTHING, db_column='custno')
    content = models.CharField(max_length=100, blank=True, null=True)
    star = models.FloatField(blank=True, null=True)
    regdate = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'review'



