# Generated by Django 3.1.2 on 2021-08-31 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_accept'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='status1',
            field=models.BooleanField(default=False),
        ),
    ]
