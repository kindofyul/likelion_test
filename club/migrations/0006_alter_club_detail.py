# Generated by Django 4.2.2 on 2023-07-03 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0005_alter_club_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='detail',
            field=models.CharField(max_length=100),
        ),
    ]
