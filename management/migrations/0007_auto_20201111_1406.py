# Generated by Django 3.1.3 on 2020-11-11 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0006_auto_20201111_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='due_date',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='sale',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='management.sale'),
        ),
    ]