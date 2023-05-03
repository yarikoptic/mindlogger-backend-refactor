from typing import Iterable, Type

import sentry_sdk
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.routing import APIRouter

import apps.activities.router as activities
import apps.alerts.router as alerts
import apps.answers.router as answers
import apps.applets.router as applets
import apps.authentication.router as auth
import apps.file.router as files
import apps.folders.router as folders
import apps.healthcheck.router as healthcheck
import apps.invitations.router as invitations
import apps.logs.router as logs
import apps.schedule.router as schedule
import apps.test_data.router as test_data
import apps.themes.router as themes
import apps.transfer_ownership.router as transfer_ownership
import apps.users.router as users
import apps.workspaces.router as workspaces
import middlewares as middlewares_
from apps.shared.exception import BaseError
from config import settings
from middlewares.exception import _pydantic_validation_errors_handler, \
    _custom_base_errors_handler, _python_base_error_handler

# Declare your routers here
routers: Iterable[APIRouter] = (
    healthcheck.router,
    activities.router,
    activities.public_router,
    auth.router,
    applets.router,
    applets.public_router,
    users.router,
    themes.router,
    invitations.router,
    logs.router,
    schedule.router,
    schedule.public_router,
    schedule.user_router,
    folders.router,
    answers.router,
    workspaces.router,
    workspaces.applet_router,
    transfer_ownership.router,
    alerts.router,
    test_data.router,
    files.router,
)

# Declare your middlewares here
middlewares: Iterable[tuple[Type[middlewares_.Middleware], dict]] = (
    (middlewares_.CORSMiddleware, middlewares_.cors_options),
)


def create_app():
    # Create base FastAPI application
    app = FastAPI(
        description=f"Commit id: <b>{settings.commit_id}"
        f"</b><br>Version: <b>{settings.version}</b>"
    )
    if settings.sentry.dsn:
        sentry_sdk.init(dsn=settings.sentry.dsn, traces_sample_rate=1.0)

    # Include routers
    for router in routers:
        app.include_router(router)

    # Include middlewares
    for middleware, options in middlewares:
        app.add_middleware(middleware, **options)

    app.add_exception_handler(RequestValidationError, _pydantic_validation_errors_handler)
    app.add_exception_handler(BaseError, _custom_base_errors_handler)
    app.add_exception_handler(Exception, _python_base_error_handler)

    return app
