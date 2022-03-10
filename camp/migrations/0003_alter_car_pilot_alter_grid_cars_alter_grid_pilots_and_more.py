# Generated by Django 4.0.3 on 2022-03-01 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('camp', '0002_grid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='pilot',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='camp.pilot'),
        ),
        migrations.AlterField(
            model_name='grid',
            name='cars',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='camp.car'),
        ),
        migrations.AlterField(
            model_name='grid',
            name='pilots',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='camp.pilot'),
        ),
        migrations.AlterField(
            model_name='grid',
            name='teams',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='camp.team'),
        ),
        migrations.AlterField(
            model_name='team',
            name='car',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='camp.car'),
        ),
        migrations.AlterField(
            model_name='team',
            name='pilot',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='camp.pilot'),
        ),
    ]
