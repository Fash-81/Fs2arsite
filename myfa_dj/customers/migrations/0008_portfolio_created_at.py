# Generated by Django 4.1.3 on 2022-11-18 09:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0007_alter_portfolio_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
