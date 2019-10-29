# Generated by Django 2.2.5 on 2019-09-05 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190904_1507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='queststep',
            name='place',
        ),
        migrations.AddField(
            model_name='quest',
            name='position',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='queststep',
            name='properties',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='queststep',
            name='type',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='beacon',
            name='beacon_id',
            field=models.CharField(max_length=300, unique=True),
        ),
        migrations.AlterField(
            model_name='queststep',
            name='quest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='main.Quest'),
        ),
    ]
