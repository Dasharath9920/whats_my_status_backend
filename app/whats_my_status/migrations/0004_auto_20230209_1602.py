# Generated by Django 3.2.17 on 2023-02-09 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whats_my_status', '0003_auto_20230209_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amountspent',
            name='updatedOn',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='timespent',
            name='updatedOn',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
