# Generated by Django 4.1.1 on 2022-10-14 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0005_compta_drf'),
    ]

    operations = [
        migrations.CreateModel(
            name='coord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sujet', models.CharField(max_length=1000)),
                ('date', models.DateField()),
            ],
        ),
    ]
