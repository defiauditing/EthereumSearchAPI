from django.apps import AppConfig


class WebConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'web'
    def ready(self) -> None:
        from . import signals
        from . import hooks
        return super().ready()