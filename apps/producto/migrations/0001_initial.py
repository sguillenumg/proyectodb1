# Generated by Django 3.0.3 on 2021-10-16 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto_id', models.IntegerField()),
                ('sucursal_id', models.IntegerField()),
                ('puntos', models.IntegerField(null=True)),
            ],
            options={
                'verbose_name': 'inventarios',
                'db_table': 'inventarios',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=500)),
                ('costo', models.DecimalField(decimal_places=2, max_digits=8)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
            options={
                'verbose_name': 'productos',
                'db_table': 'productos',
            },
        ),
    ]