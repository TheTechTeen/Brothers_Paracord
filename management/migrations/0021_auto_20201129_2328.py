# Generated by Django 3.1.3 on 2020-11-29 23:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0020_auto_20201126_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeebuild',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='storesale',
            name='sale',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='management.sale'),
        ),
    ]