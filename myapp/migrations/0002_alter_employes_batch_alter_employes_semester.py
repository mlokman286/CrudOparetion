# Generated by Django 4.2.5 on 2023-10-03 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employes',
            name='batch',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='employes',
            name='semester',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
