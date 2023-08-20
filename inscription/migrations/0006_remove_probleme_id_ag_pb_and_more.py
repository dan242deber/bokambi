# Generated by Django 4.2.4 on 2023-08-13 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inscription', '0005_probleme_id_ag_pb_probleme_id_ag_pb_recept'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='probleme',
            name='id_ag_pb',
        ),
        migrations.RemoveField(
            model_name='probleme',
            name='id_ag_pb_recept',
        ),
        migrations.CreateModel(
            name='Plainte',
            fields=[
                ('id_plainte', models.AutoField(primary_key=True, serialize=False)),
                ('lib_plainte', models.CharField(max_length=255)),
                ('id_ag_pb', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inscription.agentpublic')),
                ('id_ag_pb_recept', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='problemes_receptes', to='inscription.agentpublic')),
            ],
        ),
    ]