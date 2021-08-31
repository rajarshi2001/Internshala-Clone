# Generated by Django 3.1.2 on 2021-08-31 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20210830_2018'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('done', models.BooleanField(default=False)),
                ('apply', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.application')),
            ],
        ),
    ]