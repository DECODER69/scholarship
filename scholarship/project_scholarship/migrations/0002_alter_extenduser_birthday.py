# Generated by Django 4.0.1 on 2022-06-09 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_scholarship', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extenduser',
            name='birthday',
            field=models.DateField(null=True),
        ),
    ]