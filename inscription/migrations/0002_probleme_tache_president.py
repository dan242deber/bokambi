# Generated by Django 4.2.4 on 2023-08-13 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inscription', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Probleme',
            fields=[
                ('id_prob', models.IntegerField(primary_key=True, serialize=False)),
                ('lib_prob', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Tache',
            fields=[
                ('id_tache', models.IntegerField(primary_key=True, serialize=False)),
                ('lib_tache', models.CharField(max_length=255)),
                ('id_ag_pb', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inscription.agentpublic')),
            ],
        ),
        migrations.CreateModel(
            name='President',
            fields=[
                ('id_pre', models.IntegerField(primary_key=True, serialize=False)),
                ('date_nom_pre', models.DateField()),
                ('id_ag_pb', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inscription.agentpublic')),
            ],
        ),
    ]