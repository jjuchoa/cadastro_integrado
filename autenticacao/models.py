from django.db import models
from django.forms import ModelForm


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    def __str__(self):
        return self.name


class AuthGroupForm(ModelForm):
    class Meta:
        Model = AuthGroup
        fields = ('name',)


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    def __str__(self):
        return self.group


class AuthGroupPermissions (ModelForm):
    class Meta:
        Model = AuthGroupPermissions
        fields = ('group', 'permission')


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class AuthPermissionForm(ModelForm):
    class Meta:
        Model = AuthPermission
        fields = ('content_type', 'codename', 'name')


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    last_name = models.CharField(max_length=150)

    def __str__(self):
        return self.first_name


class AuthUserForm(ModelForm):
    class Meta:
        Model = AuthUser
        fields = ('password', 'last_login', 'is_superuser', 'username', 'first_name', 'email', 'is_staff',
                  'is_active', 'date_joined', 'last_name')


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    def __str__(self):
        return self.group


class AuthUserGroupsForm (ModelForm):
    class Meta:
        Model = AuthUserGroups
        fields = ('user', 'group')


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    def __str__(self):
        return self.permission


class AuthUserUserPermissionsForm (ModelForm):
    class Meta:
        Model = AuthUserUserPermissions
        fields = ('user', 'permission')


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.change_message


class DjangoAdminLogForm (ModelForm):
    class Meta:
        Model = DjangoAdminLog
        fields = ('action_time', 'object_id', 'object_repr', 'change_message', 'content_type', 'user', 'action_flag')


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    def __str__(self):
        return self.app_label


class DjangoContentTypeForm (ModelForm):
    class Meta:
        Model = DjangoContentType
        fields = ('app_label', 'model')


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    def __str__(self):
        return self.app


class DjangoMigrationsForm (ModelForm):
    class Meta:
        Model = DjangoMigrations
        fields = ('app', 'name', 'applied')


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    def __str__(self):
        return self.session_key


class DjangoSessionForm (ModelForm):
    class Meta:
        Model = DjangoSession
        fields = ('session_key', 'session_data', 'expire_date')
