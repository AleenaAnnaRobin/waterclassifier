# Generated by Django 4.2.2 on 2023-06-25 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifier', '0006_alter_qualityanalysis_sample_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qualityanalysis',
            name='sample_id',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
