# Generated by Django 4.2.3 on 2023-08-28 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_remove_custompermission_permission_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="module",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="users.module",
            ),
        ),
    ]
