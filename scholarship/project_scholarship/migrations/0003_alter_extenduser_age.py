# Generated by Django 4.0.1 on 2022-06-17 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_scholarship', '0002_alter_extenduser_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extenduser',
            name='age',
            field=models.CharField(max_length=100, null=True),
        ),
    ]