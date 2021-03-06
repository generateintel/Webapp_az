# Generated by Django 3.0.8 on 2020-08-12 23:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_Us',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('message', models.CharField(max_length=10000000)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User_Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.TextField(blank=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('age', models.CharField(blank=True, max_length=255)),
                ('interest', models.CharField(blank=True, max_length=255)),
                ('mobile', models.CharField(blank=True, max_length=255)),
                ('location', models.CharField(blank=True, max_length=255)),
                ('role', models.CharField(choices=[('A', 'Admin'), ('S', 'Super'), ('U', 'User'), ('V', 'Vendor')], default='U', max_length=1)),
                ('verfication_status', models.BooleanField(default=False)),
                ('activation_Key', models.CharField(blank=True, default='', max_length=255)),
                ('user_deactive_status', models.CharField(blank=True, default='', max_length=255)),
                ('user_deactive_reason', models.CharField(blank=True, default='', max_length=255)),
                ('forget_password_key', models.TextField(blank=True)),
                ('profile_updated', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(default='0', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
