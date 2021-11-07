# Generated by Django 3.2.6 on 2021-09-17 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0027_auto_20210905_1606"),
    ]

    operations = [
        migrations.AlterField(
            model_name="coresettings",
            name="created_by",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="coresettings",
            name="modified_by",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="customfield",
            name="created_by",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="customfield",
            name="modified_by",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="globalkvstore",
            name="created_by",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="globalkvstore",
            name="modified_by",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="urlaction",
            name="created_by",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="urlaction",
            name="modified_by",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]