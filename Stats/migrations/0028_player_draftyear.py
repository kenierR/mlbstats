# Generated by Django 4.2.5 on 2023-10-02 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stats', '0027_alter_player_fulllfmname_alter_player_initlastname'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='draftYear',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
