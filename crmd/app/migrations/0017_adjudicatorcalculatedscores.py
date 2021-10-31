# Generated by Django 3.2.7 on 2021-10-08 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_delete_adjcalculatedscores'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdjudicatorCalculatedScores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dnum', models.PositiveIntegerField()),
                ('prop', models.CharField(max_length=5)),
                ('opp', models.CharField(max_length=5)),
                ('adjudicator', models.CharField(max_length=20)),
                ('adjscore', models.FloatField()),
            ],
        ),
    ]
