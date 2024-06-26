# Generated by Django 4.1.1 on 2022-10-05 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0003_passation'),
    ]

    operations = [
        migrations.CreateModel(
            name='compta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.DecimalField(decimal_places=2, max_digits=10)),
                ('beneficiaire', models.CharField(max_length=100)),
                ('datefact', models.DateField()),
                ('numfact', models.CharField(max_length=100)),
                ('motif', models.CharField(max_length=100)),
                ('imf', models.CharField(max_length=100)),
                ('net', models.DecimalField(decimal_places=2, max_digits=10)),
                ('modepay', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='static/')),
            ],
        ),
    ]
