# Generated by Django 4.2.3 on 2023-08-15 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailyFinancialRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('total_sales', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_expenses', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
