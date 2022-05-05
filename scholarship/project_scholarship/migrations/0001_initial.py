# Generated by Django 4.0.1 on 2022-05-05 06:12

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
                ('status', models.CharField(choices=[('PENDING', 'PENDING'), ('FOR REVIEW', 'FOR REVIEW'), ('APPROVED', 'APPROVED'), ('REJECTED', 'REJECTED'), ('GRADUATED', 'GRADUATED')], default='PENDING', max_length=20)),
                ('department', models.CharField(max_length=100)),
                ('school', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('middlename', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('extention', models.CharField(default='', max_length=100, null=True)),
                ('birthday', models.DateField()),
                ('birthplace', models.CharField(max_length=100)),
                ('religion', models.CharField(default='', max_length=100, null=True)),
                ('cellphone', models.BigIntegerField(null=True)),
                ('gender', models.CharField(max_length=10)),
                ('age', models.DecimalField(decimal_places=0, default='', max_digits=11)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('civil', models.CharField(max_length=10)),
                ('unit', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('barangay', models.CharField(max_length=100)),
                ('municipality', models.CharField(max_length=100)),
                ('province', models.CharField(max_length=100)),
                ('fname', models.CharField(max_length=100)),
                ('fcontact', models.BigIntegerField(null=True)),
                ('foccupation', models.CharField(max_length=100)),
                ('mname', models.CharField(max_length=100)),
                ('mcontact', models.BigIntegerField(null=True)),
                ('moccupation', models.CharField(max_length=100)),
                ('gname', models.CharField(max_length=100)),
                ('gcontact', models.BigIntegerField(null=True)),
                ('goccupation', models.CharField(max_length=100)),
                ('income', models.CharField(max_length=100)),
                ('picture', models.ImageField(upload_to='images/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
