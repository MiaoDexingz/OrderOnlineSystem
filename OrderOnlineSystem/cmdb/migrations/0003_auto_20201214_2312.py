# Generated by Django 3.1.3 on 2020-12-14 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0002_remove_usr_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usr',
            name='stage',
            field=models.CharField(choices=[('C', '顾客'), ('M', '商家'), ('D', '送餐员')], max_length=20, verbose_name='身份'),
        ),
    ]