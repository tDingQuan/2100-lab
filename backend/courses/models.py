import datetime

from django.db import models
from django.utils import timezone
from django.conf import settings

from core.models import SoftDeletionModel


class Course(SoftDeletionModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    up_votes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='course_up_vote_customer')
    codename = models.CharField(max_length=10, unique=True)
    price = models.DecimalField(decimal_places=2, max_digits=12, default=0)
    reward_percent = models.DecimalField(decimal_places=2, max_digits=2, default=0)
    thumbnail = models.ImageField(upload_to='uploads/courses/thumbnails/', blank=True)
    audio = models.FileField(upload_to='uploads/courses/audios/', blank=True)
    expire_duration = models.DurationField(default=datetime.timedelta())
    can_comment = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Image(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    image_path = models.ImageField(upload_to='uploads/courses/images/')
    load_time = models.IntegerField(default=0)


class Comment(SoftDeletionModel):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    content = models.TextField()
    up_votes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='comment_up_vote_customer')
    down_votes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='comment_down_vote_customer')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        if len(self.content) < 50:
            return self.content
        else:
            return self.content[:50] + '...'