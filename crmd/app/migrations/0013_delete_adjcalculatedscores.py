# Generated by Django 3.2.7 on 2021-10-08 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_debate_motion'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AdjCalculatedScores',
        ),
    ]