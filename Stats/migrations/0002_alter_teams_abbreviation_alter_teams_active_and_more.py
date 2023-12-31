# Generated by Django 4.2.5 on 2023-10-22 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teams',
            name='abbreviation',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='teams',
            name='active',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='teams',
            name='allStarStatus',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='teams',
            name='clubName',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='teams',
            name='fileCode',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='teams',
            name='firstYearOfPlay',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='teams',
            name='franchiseName',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='teams',
            name='link',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='teams',
            name='locationName',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='teams',
            name='parentOrgId',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='teams',
            name='parentOrgName',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='teams',
            name='shortName',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='teams',
            name='teamCode',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='teams',
            name='teamName',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
