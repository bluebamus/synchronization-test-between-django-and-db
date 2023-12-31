# Generated by Django 4.2.7 on 2023-12-07 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sync', '0001_initial'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='items',
            name='items_group_idx',
        ),
        migrations.AddField(
            model_name='items',
            name='item_expiration',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddIndex(
            model_name='items',
            index=models.Index(fields=['item_expiration'], name='item_expiration_idx'),
        ),
    ]
