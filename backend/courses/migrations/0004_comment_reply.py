# Generated by Django 2.1 on 2018-08-25 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20180825_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='reply',
            field=models.ManyToManyField(blank=True, related_name='_comment_reply_+', to='courses.Comment'),
        ),
    ]
