# Generated by Django 4.1 on 2024-01-12 10:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("kpi_server", "0006_index_parent_index"),
    ]

    operations = [
        migrations.AlterField(
            model_name="index",
            name="index_num",
            field=models.CharField(help_text="指标编号", max_length=30, unique=True),
        ),
    ]
