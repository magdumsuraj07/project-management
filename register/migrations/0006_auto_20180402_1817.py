# Generated by Django 2.0.3 on 2018-04-02 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_auto_20180402_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='project',
            field=models.ManyToManyField(blank=True, to='projects.Project'),
        ),
    ]
