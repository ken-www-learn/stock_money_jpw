from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "stock_money_jpy.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import stock_money_jpy.users.signals  # noqa F401
        except ImportError:
            pass
