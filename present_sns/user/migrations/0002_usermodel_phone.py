# Generated by Django 4.1.1 on 2022-10-02 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='phone',
            field=models.CharField(max_length=256, null=True, unique=True),
        ),
    ]