# Generated by Django 4.1.7 on 2024-12-04 11:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_user_priviledge"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="priviledge",
        ),
    ]
