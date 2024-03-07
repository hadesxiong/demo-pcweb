# Generated by Django 4.1 on 2024-03-05 03:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("kpi_server", "0018_alter_factorconfig_factor_ext_info"),
    ]

    operations = [
        migrations.AddField(
            model_name="factorconfig",
            name="factor_logic",
            field=models.IntegerField(default=1, help_text="因子运算逻辑"),
        ),
        migrations.AlterField(
            model_name="factorconfig",
            name="factor_class",
            field=models.IntegerField(default=1, help_text="因子分类"),
        ),
    ]
