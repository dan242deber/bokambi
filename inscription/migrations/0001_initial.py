# Generated by Django 4.2.4 on 2023-08-13 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgentPublic',
            fields=[
                ('id_ag_pb', models.IntegerField(primary_key=True, serialize=False)),
                ('nom_ag_pb', models.CharField(max_length=255)),
                ('prenom_ag_pb', models.CharField(max_length=255)),
                ('ville_nais_ag_pb', models.CharField(max_length=255)),
                ('pays_nais_ag_pb', models.CharField(max_length=255)),
                ('date_nomination_ag_pb', models.CharField(max_length=255)),
                ('adresse_ag_pb', models.CharField(max_length=255)),
                ('telephone_ag_pb', models.CharField(max_length=20)),
                ('email_ag_pb', models.CharField(max_length=255)),
                ('pass_ag_pb', models.CharField(max_length=255)),
                ('statut_ag_pb', models.CharField(max_length=255)),
                ('etat_ag_pb', models.CharField(max_length=255)),
                ('genre_ag_pb', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Candidature',
            fields=[
                ('id_cand', models.IntegerField(primary_key=True, serialize=False)),
                ('lib_cand', models.CharField(max_length=255)),
                ('date_cand', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id_categorie', models.IntegerField(primary_key=True, serialize=False)),
                ('lib_categorie', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Diplome',
            fields=[
                ('id_diplome', models.IntegerField(primary_key=True, serialize=False)),
                ('lib_diplome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Ministere',
            fields=[
                ('id_ministere', models.IntegerField(primary_key=True, serialize=False)),
                ('lib_ministere', models.CharField(max_length=255)),
                ('adresse_ministere', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PosteTravail',
            fields=[
                ('id_post_trav', models.IntegerField(primary_key=True, serialize=False)),
                ('lib_post_trav', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Personne',
            fields=[
                ('id_pers', models.IntegerField(primary_key=True, serialize=False)),
                ('nom_pers', models.CharField(max_length=255)),
                ('prenom_pers', models.CharField(max_length=255)),
                ('date_nais_pers', models.DateField()),
                ('pays_nais_pers', models.CharField(max_length=255)),
                ('ville_nais_pers', models.CharField(max_length=255)),
                ('adresse_pers', models.CharField(max_length=255)),
                ('telephone_pers', models.CharField(max_length=20)),
                ('email_pers', models.CharField(max_length=255)),
                ('genre_pers', models.CharField(max_length=1)),
                ('dossier_cand_pers', models.CharField(blank=True, max_length=255, null=True)),
                ('id_cand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inscription.candidature')),
            ],
        ),
        migrations.CreateModel(
            name='NoteService',
            fields=[
                ('id_note_serv', models.IntegerField(primary_key=True, serialize=False)),
                ('lib_serv', models.CharField(max_length=255)),
                ('id_pers', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inscription.personne')),
            ],
        ),
        migrations.CreateModel(
            name='Minis',
            fields=[
                ('id_mi', models.IntegerField(primary_key=True, serialize=False)),
                ('date_nom_m', models.DateField()),
                ('id_ag_pb', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inscription.agentpublic')),
            ],
        ),
        migrations.CreateModel(
            name='FpMinis',
            fields=[
                ('id_fp_mi', models.IntegerField(primary_key=True, serialize=False)),
                ('date_nom_m', models.DateField()),
                ('id_ag_pb', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inscription.agentpublic')),
            ],
        ),
        migrations.CreateModel(
            name='Echelon',
            fields=[
                ('id_echelon', models.IntegerField(primary_key=True, serialize=False)),
                ('lib_echelon', models.IntegerField()),
                ('id_categorie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inscription.categorie')),
            ],
        ),
        migrations.CreateModel(
            name='Dossier',
            fields=[
                ('id_dos', models.IntegerField(primary_key=True, serialize=False)),
                ('lib_dos', models.CharField(max_length=255)),
                ('fiche_renseign', models.CharField(blank=True, max_length=255, null=True)),
                ('piece_just', models.CharField(blank=True, max_length=255, null=True)),
                ('acte_civil', models.CharField(blank=True, max_length=255, null=True)),
                ('acte_modif', models.CharField(blank=True, max_length=255, null=True)),
                ('inscri_env', models.CharField(blank=True, max_length=255, null=True)),
                ('acte_form', models.CharField(blank=True, max_length=255, null=True)),
                ('recomp_envt', models.CharField(blank=True, max_length=255, null=True)),
                ('sanc_etab', models.CharField(blank=True, max_length=255, null=True)),
                ('recours_admini', models.CharField(blank=True, max_length=255, null=True)),
                ('id_ag_pb', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inscription.agentpublic')),
            ],
        ),
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id_depart', models.IntegerField(primary_key=True, serialize=False)),
                ('lib_depart', models.CharField(max_length=255)),
                ('adresse_depart', models.CharField(blank=True, max_length=255, null=True)),
                ('id_ministere', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inscription.ministere')),
            ],
        ),
        migrations.CreateModel(
            name='ChefDepart',
            fields=[
                ('id_chef_depart', models.IntegerField(primary_key=True, serialize=False)),
                ('date_nom_cd', models.DateField()),
                ('id_ag_pb', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inscription.agentpublic')),
            ],
        ),
        migrations.AddField(
            model_name='candidature',
            name='id_depart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inscription.departement'),
        ),
        migrations.AddField(
            model_name='candidature',
            name='id_ministere',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inscription.ministere'),
        ),
        migrations.AddField(
            model_name='candidature',
            name='id_post_trav',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inscription.postetravail'),
        ),
    ]
