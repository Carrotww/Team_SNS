<<<<<<< Updated upstream
# Generated by Django 4.1.1 on 2022-10-04 10:33
=======
# Generated by Django 4.1.1 on 2022-10-04 11:04
>>>>>>> Stashed changes

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
<<<<<<< Updated upstream
        ('user', '0001_initial'),
=======
        ("user", "0001_initial"),
>>>>>>> Stashed changes
    ]

    operations = [
        migrations.CreateModel(
<<<<<<< Updated upstream
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_img', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('userModel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
=======
            name="Photo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "user_img",
                    models.ImageField(blank=True, null=True, upload_to="images/"),
                ),
                (
                    "userModel",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
>>>>>>> Stashed changes
            ],
        ),
    ]
