# Generated by Django 5.1.3 on 2024-12-11 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fitquest", "0013_progress_start_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="order_number",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
