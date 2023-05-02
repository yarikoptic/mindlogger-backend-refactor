from gettext import gettext as _

from apps.shared.exception import NotFoundError, ValidationError, \
    InternalServerError


class ThemeNotFoundError(NotFoundError):
    message = _("No such theme with {key}={value}.")


class ThemesError(InternalServerError):
    message = _("Themes service error")


class ThemeAlreadyExist(ValidationError):
    message = _("Theme already exist")
