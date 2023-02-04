# Generated by Django 4.1.6 on 2023-02-04 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_remove_product_is_warranty'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='key',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='TitleProperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='title_properties', to='product.product')),
            ],
        ),
        migrations.AlterField(
            model_name='property',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='product.titleproperty'),
        ),
    ]