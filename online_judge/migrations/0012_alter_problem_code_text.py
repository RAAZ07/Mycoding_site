# Generated by Django 4.0.5 on 2022-08-29 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_judge', '0011_problem_code_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='code_text',
            field=models.TextField(max_length=10000),
        ),
    ]