from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

class AppNameConfig(AppConfig):
    name = 'hsdrops'
    def ready(self):
        from scheduler import scheduler
        scheduler.start()