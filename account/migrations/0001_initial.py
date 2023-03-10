# Generated by Django 4.1.6 on 2023-02-09 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('phone', models.CharField(max_length=11, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('card_number', models.CharField(blank=True, max_length=16, null=True)),
                ('f_name', models.CharField(blank=True, max_length=65, null=True)),
                ('l_name', models.CharField(blank=True, max_length=65, null=True)),
                ('birth_day', models.DateField(blank=True, null=True)),
                ('image', models.ImageField(default='user.svg', upload_to='user/profile/')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=4)),
                ('phone', models.CharField(max_length=11)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
