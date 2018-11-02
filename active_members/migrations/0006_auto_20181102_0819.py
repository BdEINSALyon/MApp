# Generated by Django 2.1.3 on 2018-11-02 08:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('active_members', '0005_auto_20181101_2007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='genre',
            new_name='gender',
        ),
        migrations.AlterField(
            model_name='member',
            name='birthdate',
            field=models.DateField(blank=True, default=datetime.date.today, verbose_name='Date de naissance'),
        ),
        migrations.AlterField(
            model_name='team',
            name='responsable_bde_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='active_members.BdeSecurityGroup'),
        ),
        migrations.AlterField(
            model_name='team',
            name='responsable_insa_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='active_members.InsaSecurityGroup'),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_bde_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='active_members.BdeSecurityGroup'),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_insa_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='active_members.InsaSecurityGroup'),
        ),
    ]
