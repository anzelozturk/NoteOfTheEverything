# Generated by Django 3.1.4 on 2021-04-30 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20210430_1522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='registereduser',
        ),
    ]
