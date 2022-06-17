# Generated by Django 4.0.1 on 2022-06-17 11:03

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
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('content', models.TextField(null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='extenduser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='PENDING', max_length=20)),
                ('department', models.CharField(default='', max_length=100, null=True)),
                ('school', models.CharField(default='', max_length=100, null=True)),
                ('course', models.CharField(default='', max_length=100, null=True)),
                ('year', models.CharField(default='', max_length=100, null=True)),
                ('firstname', models.CharField(max_length=100)),
                ('middlename', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('extention', models.CharField(default='', max_length=100, null=True)),
                ('birthday', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('birthplace', models.CharField(max_length=100)),
                ('religion', models.CharField(default='', max_length=100, null=True)),
                ('cellphone', models.BigIntegerField(default='+63 ', null=True)),
                ('gender', models.CharField(default='', max_length=10, null=True)),
                ('age', models.CharField(default='', max_length=100, null=True)),
                ('email', models.EmailField(default='', max_length=254, null=True, unique=True)),
                ('civil', models.CharField(default='', max_length=10, null=True)),
                ('barangay', models.CharField(default='', max_length=100, null=True)),
                ('municipality', models.CharField(default='', max_length=100, null=True)),
                ('province', models.CharField(default='', max_length=100, null=True)),
                ('fname', models.CharField(default='', max_length=100, null=True)),
                ('fcontact', models.BigIntegerField(default='+63 ', null=True)),
                ('foccupation', models.CharField(default='', max_length=100, null=True)),
                ('mname', models.CharField(default='', max_length=100, null=True)),
                ('mcontact', models.BigIntegerField(default='+63 ', null=True)),
                ('moccupation', models.CharField(default='', max_length=100, null=True)),
                ('gname', models.CharField(default='', max_length=100, null=True)),
                ('gcontact', models.BigIntegerField(default='+63 ', null=True)),
                ('goccupation', models.CharField(max_length=100)),
                ('income', models.CharField(max_length=100)),
                ('picture', models.ImageField(default='', null=True, upload_to='images/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
