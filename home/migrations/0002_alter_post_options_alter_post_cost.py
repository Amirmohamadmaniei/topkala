# Generated by Django 4.1.6 on 2023-02-10 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'هزینه پست', 'verbose_name_plural': 'هزینه پست'},
        ),
        migrations.AlterField(
            model_name='post',
            name='cost',
            field=models.IntegerField(default=30000, verbose_name='هزینه پست ارسالی'),
        ),
    ]
