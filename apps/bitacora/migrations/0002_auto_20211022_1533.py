# Generated by Django 3.0.3 on 2021-10-22 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitacora', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bitacora',
            name='obj_new',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='bitacora',
            name='obj_old',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]
