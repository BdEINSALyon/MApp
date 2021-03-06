# Generated by Django 2.2 on 2019-05-23 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('active_members', '0009_auto_20190406_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='subteam',
            name='recruit_open',
            field=models.BooleanField(default=False),
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
