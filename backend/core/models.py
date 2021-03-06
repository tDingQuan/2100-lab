"""核心功能模型"""

# pylint: disable=E1101

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils import timezone


class SoftDeletionQuerySet(models.query.QuerySet):
    """软删除查询集"""

    def delete(self):
        """软删除对象"""

        return super(SoftDeletionQuerySet, self).update(
            deleted_at=timezone.now()
        )

    def hard_delete(self):
        """硬删除对象"""

        return super(SoftDeletionQuerySet, self).delete()

    def alive(self):
        """获取未删除对象"""

        return self.filter(deleted_at=None)

    def dead(self):
        """获取已删除对象"""

        return self.exclude(deleted_at=None)


class SoftDeletionManager(models.Manager):
    def __init__(self, *args, **kwargs):
        self.alive_only = kwargs.pop('alive_only', True)
        super(SoftDeletionManager, self).__init__(*args, **kwargs)

    def get_queryset(self):
        if self.alive_only:
            return SoftDeletionQuerySet(self.model).filter(deleted_at=None)
        return SoftDeletionQuerySet(self.model)

    def hard_delete(self):
        return self.get_queryset().hard_delete()


class SoftDeletionModel(models.Model):
    """软删除模型"""

    deleted_at = models.DateTimeField(blank=True, null=True)

    objects = SoftDeletionManager()
    all_objects = SoftDeletionManager(alive_only=False)

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        """软删除对象"""

        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self):
        """硬删除对象"""

        super(SoftDeletionModel, self).delete()


class UserManager(BaseUserManager):
    """用户管理类"""

    use_in_migrations = True

    def _create_user(self, phone_number, password, **extra_fields):
        """创建用户工具函数"""

        if not phone_number:
            raise ValueError('The given phone number must be set')
        user = self.model(
            username=str(phone_number),
            phone_number=phone_number,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, password=None, **extra_fields):
        """创建普通用户"""

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone_number, password, **extra_fields)

    def create_superuser(self, phone_number, password, **extra_fields):
        """创建超级管理员"""

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone_number, password, **extra_fields)

    def get_queryset(self):
        """获取查询集"""

        return SoftDeletionQuerySet(self.model).filter(deleted_at=None)


class CustomUser(SoftDeletionModel, AbstractUser):
    """自定义用户模型"""

    phone_number = models.CharField(max_length=150, unique=True)
    avatar = models.ImageField(
        upload_to='uploads/customers/avatars/',
        default='default/customers/avatars/2100_lab.jpg'
    )
    reward_coin = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        default=0
    )
    is_vip = models.BooleanField(default=False)
    is_banned = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.username

    def as_dict(self):
        """获取字典"""

        return {
            'user_id': self.id,
            'username': self.username,
            'phone_number': self.phone_number,
            'avatar': str(self.avatar),
            'reward_coin': self.reward_coin,
            'is_vip': self.is_vip,
            'is_banned': self.is_banned,
            'date_joined': self.date_joined,
            'updated_at': self.updated_at
        }

    def as_admin_dict(self):
        """获取管理员字典"""

        return {
            'admin_id': self.id,
            'username': self.username,
            'phone_number': self.phone_number
        }

    def as_customer_dict(self):
        """获取用户字典"""

        return {
            'customer_id': self.id,
            'username': self.username,
            'phone_number': self.phone_number,
            'is_vip': self.is_vip,
            'is_banned': self.is_banned
        }
