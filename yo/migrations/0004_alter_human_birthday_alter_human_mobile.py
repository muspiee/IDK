# Generated by Django 5.0.1 on 2024-02-05 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yo', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='human',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='human',
            name='mobile',
            field=models.PositiveIntegerField(max_length=50),
        ),
    ]
