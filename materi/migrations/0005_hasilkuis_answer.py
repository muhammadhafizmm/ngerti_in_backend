# Generated by Django 3.2.7 on 2021-12-04 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materi', '0004_auto_20211204_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='hasilkuis',
            name='answer',
            field=models.JSONField(default=''),
        ),
    ]