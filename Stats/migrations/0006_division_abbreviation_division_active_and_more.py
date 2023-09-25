# Generated by Django 4.2.5 on 2023-09-21 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Stats', '0005_league_nameshort_league_seasonstate'),
    ]

    operations = [
        migrations.AddField(
            model_name='division',
            name='abbreviation',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='division',
            name='active',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='division',
            name='hasWildCard',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='division',
            name='league',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Stats.league'),
        ),
        migrations.AddField(
            model_name='division',
            name='link',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='division',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='division',
            name='nameShort',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='division',
            name='season',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Stats.season'),
        ),
        migrations.AddField(
            model_name='division',
            name='sortOrder',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='division',
            name='sport',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Stats.sport'),
        ),
        migrations.AlterField(
            model_name='division',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
