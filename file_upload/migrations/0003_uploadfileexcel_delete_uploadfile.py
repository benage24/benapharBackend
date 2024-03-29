# Generated by Django 4.2.3 on 2023-12-29 16:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("file_upload", "0002_alter_uploadfile_file"),
    ]

    operations = [
        migrations.CreateModel(
            name="UploadFileExcel",
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
                ("sheet_name", models.CharField(max_length=255)),
                ("column_data", models.JSONField()),
            ],
        ),
        migrations.DeleteModel(
            name="UploadFile",
        ),
    ]
