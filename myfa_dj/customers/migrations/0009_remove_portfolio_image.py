# Generated by Django 4.1.3 on 2022-11-18 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0008_portfolio_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='image',
        ),
    ]
