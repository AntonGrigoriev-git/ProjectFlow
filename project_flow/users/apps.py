from django.apps import AppConfig
from django.db.models.signals import post_migrate

def create_user_groups(sender, **kwargs):
    from django.contrib.auth.models import Group, Permission
    groups = ['Администратор', 'Менеджер Проекта', 'Участник', 'Наблюдатель']
    for group_name in groups:
        Group.objects.get_or_create(name=group_name)

class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        post_migrate.connect(create_user_groups, sender=self)
