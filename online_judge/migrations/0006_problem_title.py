# Generated by Django 4.0.5 on 2022-06-25 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_judge', '0005_submission'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='title',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
