# Generated by Django 2.2.4 on 2019-10-26 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0008_auto_20191026_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentmethod',
            name='promotion',
            field=models.CharField(default='', max_length=50, verbose_name='promotion'),
            preserve_default=False,
        ),
    ]
