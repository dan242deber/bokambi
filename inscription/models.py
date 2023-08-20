from datetime import date
from django.db import models




class Ministere(models.Model):
    id_ministere = models.AutoField(primary_key=True)
    lib_ministere = models.CharField(max_length=255)
    adresse_ministere = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.lib_ministere

    
class Departement(models.Model):
    id_depart = models.AutoField(primary_key=True)
    lib_depart = models.CharField(max_length=255)
    adresse_depart = models.CharField(max_length=255, null=True, blank=True)
    id_ministere = models.ForeignKey(Ministere, on_delete=models.SET_NULL, null=True, blank=True)


class PosteTravail(models.Model):
    id_post_trav = models.AutoField(primary_key=True)
    lib_post_trav = models.CharField(max_length=255)

    def __str__(self):
        return self.lib_post_trav 
    
class Candidature(models.Model):
    id_cand = models.AutoField(primary_key=True)
    lib_cand = models.TextField()
    date_cand = models.DateField(null=True, blank=True)
    id_depart = models.ForeignKey(Departement, on_delete=models.SET_NULL, null=True, blank=True)
    id_post_trav = models.ForeignKey(PosteTravail, on_delete=models.SET_NULL, null=True, blank=True)
    id_ministere = models.ForeignKey(Ministere, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.lib_cand


class Categorie(models.Model):
    id_categorie = models.AutoField(primary_key=True)
    lib_categorie = models.IntegerField()

    def __str__(self):
        return str(self.lib_categorie)


class Echelon(models.Model):
    id_echelon = models.AutoField(primary_key=True)
    lib_echelon = models.IntegerField()
    id_categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.lib_echelon)

#########################################


class Personne(models.Model):
    id_pers = models.AutoField(primary_key=True)
    nom_pers = models.CharField(max_length=255)
    prenom_pers = models.CharField(max_length=255)
    date_nais_pers = models.DateField()
    pays_nais_pers = models.CharField(max_length=255)
    ville_nais_pers = models.CharField(max_length=255)
    adresse_pers = models.CharField(max_length=255)
    telephone_pers = models.CharField(max_length=20)
    email_pers = models.CharField(max_length=255)
    genre_pers = models.CharField(max_length=1)
    dossier_cand_pers = models.CharField(max_length=255, null=True, blank=True)
    id_cand = models.ForeignKey(Candidature, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.nom_pers} {self.prenom_pers}"


class AgentPublic(models.Model):
    id_ag_pb = models.AutoField(primary_key=True)
    nom_ag_pb = models.CharField(max_length=255)
    prenom_ag_pb = models.CharField(max_length=255)
    ville_nais_ag_pb = models.CharField(max_length=255)
    pays_nais_ag_pb = models.CharField(max_length=255)
    date_nais_ag_pb = models.DateField()
    date_nomination_ag_pb = models.DateField()
    adresse_ag_pb = models.CharField(max_length=255)
    telephone_ag_pb = models.CharField(max_length=20)
    email_ag_pb = models.CharField(max_length=255)
    pass_ag_pb = models.CharField(max_length=255)
    statut_ag_pb = models.CharField(max_length=255)
    genre_ag_pb = models.CharField(max_length=1)
    id_cand = models.ForeignKey(Candidature, on_delete=models.SET_NULL, null=True, blank=True)
    # id_categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True, blank=True)
    # id_echelon = models.ForeignKey(Echelon, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def calculer_age(self,date_naissance):
        today = date.today()
        age = today.year - date_naissance.year - ((today.month, today.day) < (date_naissance.month, date_naissance.day))
        return age

    def __str__(self):
        return f"{self.nom_ag_pb} {self.prenom_ag_pb}"



    


class ChefDepart(models.Model):
    id_chef_depart = models.AutoField(primary_key=True)
    date_nom_cd = models.DateField()
    id_ag_pb = models.ForeignKey(AgentPublic, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Chef Département {self.id_chef_depart}"


class President(models.Model):
    id_pre = models.AutoField(primary_key=True)
    id_ag_pb = models.ForeignKey(AgentPublic, on_delete=models.SET_NULL, null=True, blank=True)
    date_nom_pre = models.DateField()

    def __str__(self):
        return f"Président {self.id_pre}"




class Probleme(models.Model):
    id_prob = models.AutoField(primary_key=True)
    lib_prob = models.CharField(max_length=255)
    
    def __str__(self):
        return self.lib_prob

class Plainte(models.Model):
    id_ag_pb = models.ForeignKey(AgentPublic, on_delete=models.SET_NULL, null=True, blank=True)
    id_plainte = models.AutoField(primary_key=True)
    id_prob = models.ForeignKey(Probleme, on_delete=models.SET_NULL, null=True, blank=True)
    id_ag_pb_recept = models.ForeignKey(AgentPublic, on_delete=models.SET_NULL, null=True, blank=True, related_name='problemes_receptes')

    def __str__(self):
        return self.lib_plainte 




class Diplome(models.Model):
    id_diplome = models.AutoField(primary_key=True)
    lib_diplome = models.CharField(max_length=255)

    def __str__(self):
        return self.lib_diplome

class Dossier(models.Model):
    id_dos = models.AutoField(primary_key=True)
    lib_dos = models.CharField(max_length=255)
    fiche_renseign = models.CharField(max_length=255, null=True, blank=True)
    piece_just = models.CharField(max_length=255, null=True, blank=True)
    acte_civil = models.CharField(max_length=255, null=True, blank=True)
    acte_modif = models.CharField(max_length=255, null=True, blank=True)
    inscri_env = models.CharField(max_length=255, null=True, blank=True)
    acte_form = models.CharField(max_length=255, null=True, blank=True)
    recomp_envt = models.CharField(max_length=255, null=True, blank=True)
    sanc_etab = models.CharField(max_length=255, null=True, blank=True)
    recours_admini = models.CharField(max_length=255, null=True, blank=True)
    id_ag_pb = models.ForeignKey(AgentPublic, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.lib_dos





class FpMinis(models.Model):
    id_fp_mi = models.AutoField(primary_key=True)
    date_nom_m = models.DateField()
    id_ag_pb = models.ForeignKey(AgentPublic, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Formation Ministère {self.id_fp_mi}"


class Minis(models.Model):
    id_mi = models.AutoField(primary_key=True)
    date_nom_m = models.DateField()
    id_ag_pb = models.ForeignKey(AgentPublic, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Ministère {self.id_mi}"
    

class NoteService(models.Model):
    id_note_serv = models.AutoField(primary_key=True)
    lib_serv = models.CharField(max_length=255)
    id_pers = models.ForeignKey(Personne, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.lib_serv
    
class Tache(models.Model):
    id_tache = models.AutoField(primary_key=True)
    lib_tache = models.CharField(max_length=255)
    id_ag_pb = models.ForeignKey(AgentPublic, on_delete=models.SET_NULL, null=True, blank=True)
    id_chef_depart = models.ForeignKey(ChefDepart, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.lib_tache







