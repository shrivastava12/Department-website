# Generated by Django 2.2.2 on 2019-10-20 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bscit', '0005_auto_20191019_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='mobile_no',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
