from django.contrib.sessions.models import Session
from django.utils import timezone
from datetime import date



def calculer_age(date_naissance):
    today = date.today()
    age = today.year - date_naissance.year - ((today.month, today.day) < (date_naissance.month, date_naissance.day))
    return age


def get_online_users():
    # Récupère la liste des sessions actives
    active_sessions = Session.objects.filter(expire_date__gte=timezone.now())
    
    # Extrait les identifiants d'utilisateur des sessions actives
    user_ids = [session.get_decoded().get('_auth_user_id') for session in active_sessions]
    
    # Filtre les identifiants d'utilisateur non vides
    online_user_ids = [user_id for user_id in user_ids if user_id is not None]
    
    # Compte le nombre d'utilisateurs en ligne
    online_user_count = len(set(online_user_ids))
    
    return online_user_count
