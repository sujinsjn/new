# Generated by Django 4.0.2 on 2022-07-05 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_rewards_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rewards',
            name='referral_member',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
