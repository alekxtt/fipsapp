# Generated by Django 3.2.9 on 2021-11-05 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ipitem', '0005_alter_item_type_of_item'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['number']},
        ),
    ]
