# Generated by Django 2.2.3 on 2019-07-08 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20190708_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='birth_date'),
        ),
    ]