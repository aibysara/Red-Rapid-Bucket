# Generated by Django 4.0.3 on 2022-05-09 06:57

from django.db import migrations


def insert_admin(apps,schema_editor):
    Login1 = apps.get_model("app1", "Login")
    admin = Login1(username="admin", password="admin12345", role=1)
    admin.save()


class Migration(migrations.Migration):
    dependencies = [
        ('app1','0002_initial')
    ]

    operations = [migrations.RunPython(insert_admin)
                  ]
