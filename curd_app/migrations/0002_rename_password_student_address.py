# Generated by Django 4.2 on 2023-04-17 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("curd_app", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="student",
            old_name="password",
            new_name="address",
        ),
    ]
