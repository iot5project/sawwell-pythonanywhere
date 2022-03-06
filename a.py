# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Categori(models.Model):
    cid = models.IntegerField(primary_key=True)
    categoriname = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categori'


class Ceo(models.Model):
    ceoid = models.IntegerField(primary_key=True)
    marketno = models.ForeignKey('Market', models.DO_NOTHING, db_column='marketno')
    id = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ceo'


class Cust(models.Model):
    custno = models.IntegerField(primary_key=True)
    id = models.CharField(max_length=30, blank=True, null=True)
    password = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    regdate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cust'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Food(models.Model):
    foodid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    regdate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
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
        managed = False
        db_table = 'market'


class Reply(models.Model):
    replyid = models.IntegerField(primary_key=True)
    reviewno = models.ForeignKey('Review', models.DO_NOTHING, db_column='reviewno')
    ceoid = models.ForeignKey(Ceo, models.DO_NOTHING, db_column='ceoid')
    content = models.CharField(max_length=100, blank=True, null=True)
    regdate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reply'


class Review(models.Model):
    reviewno = models.IntegerField(primary_key=True)
    marketno = models.ForeignKey(Market, models.DO_NOTHING, db_column='marketno')
    custno = models.ForeignKey(Cust, models.DO_NOTHING, db_column='custno')
    content = models.CharField(max_length=100, blank=True, null=True)
    star = models.FloatField(blank=True, null=True)
    regdate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review'
