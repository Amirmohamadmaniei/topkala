# Generated by Django 4.1.6 on 2023-02-10 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_view'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='color',
            name='title_en',
        ),
    ]
