# Generated by Django 2.2 on 2019-04-18 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cities',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cities',
            name='pcity',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='cities',
            name='status',
            field=models.BooleanField(),
        ),
    ]
