# Generated by Django 4.2.6 on 2023-10-24 17:24

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("webapp", "0008_alter_comunicado_entidad"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comunicado",
            old_name="entidad",
            new_name="ROLE",
        ),
    ]
