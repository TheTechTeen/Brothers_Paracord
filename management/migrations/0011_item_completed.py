# Generated by Django 3.1.3 on 2020-11-12 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0010_itemcolor_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='completed',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]