# Generated by Django 3.0.3 on 2020-03-06 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbaccounting', '0008_transaction_updating'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='edited',
            field=models.BooleanField(default=False),
        ),
    ]