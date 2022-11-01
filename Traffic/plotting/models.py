# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Adjustroad(models.Model):
    name = models.CharField(primary_key=True, max_length=40)
    day = models.DateField()
    mean_month = models.IntegerField(blank=True, null=True)
    vol_month = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AdjustRoad'
        unique_together = (('name', 'day'),)


class Avgsubway(models.Model):
    day = models.DateField(primary_key=True)
    gu = models.CharField(max_length=20)
    boarding = models.IntegerField(blank=True, null=True)
    getoff = models.IntegerField(db_column='getOff', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AvgSubway'
        unique_together = (('day', 'gu'),)


class Bus(models.Model):
    day = models.DateField(primary_key=True)
    gu = models.ForeignKey('Seoulindex', models.DO_NOTHING, db_column='gu')
    boarding = models.IntegerField(blank=True, null=True)
    getoff = models.IntegerField(db_column='getOff', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Bus'
        unique_together = (('day', 'gu'),)


class Rawroadtraffic(models.Model):
    name = models.OneToOneField('Spotposition', models.DO_NOTHING, db_column='name', primary_key=True)
    day = models.DateField()
    vol = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RawRoadTraffic'
        unique_together = (('name', 'day'),)


class Seoulindex(models.Model):
    gu = models.CharField(primary_key=True, max_length=20)
    population_over12 = models.IntegerField(blank=True, null=True)
    commute_population = models.IntegerField(blank=True, null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, blank=True, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SeoulIndex'


class Spotposition(models.Model):
    name = models.CharField(primary_key=True, max_length=200)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, blank=True, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SpotPosition'


class Subway(models.Model):
    day = models.DateField(primary_key=True)
    gu = models.ForeignKey(Seoulindex, models.DO_NOTHING, db_column='gu')
    boarding = models.IntegerField(blank=True, null=True)
    getoff = models.IntegerField(db_column='getOff', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Subway'
        unique_together = (('day', 'gu'),)


class Timetowork(models.Model):
    country = models.CharField(primary_key=True, max_length=20)
    total = models.IntegerField(blank=True, null=True)
    men = models.IntegerField(blank=True, null=True)
    women = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TimeToWork'


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


class Coordinate(models.Model):
    gu = models.OneToOneField(Seoulindex, models.DO_NOTHING, db_column='gu', primary_key=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, blank=True, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coordinate'


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


class DjangoPlotlyDashDashapp(models.Model):
    id = models.BigAutoField(primary_key=True)
    instance_name = models.CharField(unique=True, max_length=100)
    slug = models.CharField(unique=True, max_length=110)
    base_state = models.TextField()
    creation = models.DateTimeField()
    update = models.DateTimeField()
    save_on_change = models.IntegerField()
    stateless_app = models.ForeignKey('DjangoPlotlyDashStatelessapp', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_plotly_dash_dashapp'


class DjangoPlotlyDashStatelessapp(models.Model):
    id = models.BigAutoField(primary_key=True)
    app_name = models.CharField(unique=True, max_length=100)
    slug = models.CharField(unique=True, max_length=110)

    class Meta:
        managed = False
        db_table = 'django_plotly_dash_statelessapp'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
