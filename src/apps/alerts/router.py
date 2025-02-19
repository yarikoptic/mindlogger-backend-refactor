from fastapi.routing import APIRouter
from starlette import status

from apps.alerts.api.alert import (
    alert_get_all_by_applet_id,
    alert_update_status_by_id,
    alerts_create,
)
from apps.alerts.api.alert_config import (
    alert_config_create,
    alert_config_get_all_by_applet_id,
    alert_config_get_by_id,
    alert_config_update,
)
from apps.alerts.domain.alert import Alert, AlertPublic
from apps.alerts.domain.alert_config import AlertsConfigPublic
from apps.shared.domain import Response, ResponseMulti
from apps.shared.domain.response import DEFAULT_OPENAPI_RESPONSE

router = APIRouter(prefix="/alerts", tags=["Alerts"])

# Alert configuration create
router.post(
    "/config",
    description="""This endpoint using for adding new configuration
                for alert notified""",
    response_model_by_alias=True,
    response_model=Response[AlertsConfigPublic],
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {"model": Response[AlertsConfigPublic]},
        **DEFAULT_OPENAPI_RESPONSE,
    },
)(alert_config_create)

# Alert configuration update
router.put(
    "/config/{alert_config_id}",
    description="""This endpoint using for update configuration
                for alert notified""",
    response_model_by_alias=True,
    response_model=Response[AlertsConfigPublic],
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {"model": Response[AlertsConfigPublic]},
        **DEFAULT_OPENAPI_RESPONSE,
    },
)(alert_config_update)

# Alert configuration get by id
router.get(
    "/config/{alert_config_id}",
    description="""This endpoint using for get specific alert
                configuration by id""",
    response_model_by_alias=True,
    response_model=Response[AlertsConfigPublic],
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {"model": Response[AlertsConfigPublic]},
        **DEFAULT_OPENAPI_RESPONSE,
    },
)(alert_config_get_by_id)

# Alerts configurations get all for specific applet
router.get(
    "/configs/{applet_id}",
    description="""This endpoint using for get all alerts
                configuration for specific applet id""",
    response_model_by_alias=True,
    response_model=ResponseMulti[AlertsConfigPublic],
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {"model": ResponseMulti[AlertsConfigPublic]},
        **DEFAULT_OPENAPI_RESPONSE,
    },
)(alert_config_get_all_by_applet_id)

# Alerts create
router.post(
    "",
    description="""This endpoint using for create alerts and using
                after create answer. This endpoint is designed according
                to his principle and uses the same data model""",
    status_code=status.HTTP_201_CREATED,
    responses={
        **DEFAULT_OPENAPI_RESPONSE,
    },
)(alerts_create)

# Alerts get all
router.get(
    "/{applet_id}",
    description="""This endpoint using for get all alerts
                for specific applet id""",
    response_model_by_alias=True,
    response_model=ResponseMulti[AlertPublic],
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {"model": ResponseMulti[AlertPublic]},
        **DEFAULT_OPENAPI_RESPONSE,
    },
)(alert_get_all_by_applet_id)

# Update alert status at is_watched true
router.put(
    "/{alert_id}",
    description="""This endpoint using for update alert status
                at is_watched true""",
    response_model_by_alias=True,
    response_model=Response[Alert],
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {"model": Response[Alert]},
        **DEFAULT_OPENAPI_RESPONSE,
    },
)(alert_update_status_by_id)
