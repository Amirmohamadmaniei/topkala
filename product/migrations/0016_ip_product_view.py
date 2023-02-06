# Generated by Django 4.1.6 on 2023-02-06 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_subcategory_slug_subset_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='IP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField()),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='view',
            field=models.ManyToManyField(to='product.ip'),
        ),
    ]