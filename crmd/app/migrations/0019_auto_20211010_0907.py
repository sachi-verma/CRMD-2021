# Generated by Django 3.2.7 on 2021-10-10 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_alter_debate_motion'),
    ]

    operations = [
        migrations.AddField(
            model_name='debate',
            name='context',
            field=models.CharField(default=0, max_length=5000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='debate',
            name='motion',
            field=models.CharField(max_length=1000),
        ),
    ]
