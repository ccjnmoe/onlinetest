# Generated by Django 2.2 on 2019-04-24 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0004_auto_20190421_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='cover_image',
            field=models.ImageField(blank=True, upload_to='cover/'),
        ),
    ]