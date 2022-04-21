# Generated by Django 4.0.1 on 2022-04-20 21:22

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
            name='extenduser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('PENDING', 'PENDING'), ('FOR REVIEW', 'FOR REVIEW'), ('APPROVED', 'APPROVED')], default='PENDING', max_length=20)),
                ('department', models.CharField(max_length=100)),
                ('school', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('middlename', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('extention', models.CharField(max_length=100)),
                ('birthday', models.DateField()),
                ('birthplace', models.CharField(max_length=100)),
                ('religion', models.CharField(max_length=100)),
                ('cellphone', models.IntegerField()),
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
                ('fcontact', models.DecimalField(decimal_places=0, default='', max_digits=11)),
                ('foccupation', models.CharField(max_length=100)),
                ('mname', models.CharField(max_length=100)),
                ('mcontact', models.DecimalField(decimal_places=0, default='', max_digits=11)),
                ('moccupation', models.CharField(max_length=100)),
                ('gname', models.CharField(max_length=100)),
                ('gcontact', models.DecimalField(decimal_places=0, default='', max_digits=11)),
                ('goccupation', models.CharField(max_length=100)),
                ('income', models.CharField(max_length=100)),
                ('profilepic', models.ImageField(upload_to='images/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]