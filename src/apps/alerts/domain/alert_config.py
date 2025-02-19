import uuid

from pydantic import BaseModel, Field

from apps.shared.domain import InternalModel, PublicModel

__all__ = [
    "AlertsConfigCreateRequest",
    "AlertsConfigPublic",
    "AlertConfigCreate",
    "AlertConfig",
    "AlertConfigGet",
    "AlertsConfigUpdateRequest",
    "AlertConfigUpdate",
]


class _AlertsConfigBase(BaseModel):
    """This model used for internal needs
    as a base model for request and response
    """

    applet_id: uuid.UUID = Field(
        description="This field represents the specific applet id"
    )
    activity_item_histories_id_version: str = Field(
        description="This field represents the specific activity item "
        "histories id version in applet"
    )
    specific_answer: str = Field(
        description="This field represents the specific answer "
        "upon selection of which an alert will be created"
    )


class AlertsConfigCreateRequest(_AlertsConfigBase, PublicModel):
    """This model represents the request for create configuration
    alerts for specific applet and activity item,
    you can only have one alert per one possible answer
    """

    alert_message: str = Field(
        description="This field represents the alert message "
        "which will be shown"
    )
    viewed: bool = Field(
        description="This is a boolean field that represents "
        "whether the alerts will be shown to the user",
        default=True,
    )


class AlertsConfigPublic(AlertsConfigCreateRequest):
    """This model represents the response for configuration
    alerts for specific applet and activity item
    """

    id: uuid.UUID = Field(
        description="This field represents the id "
        "for specific alert configuration"
    )


class AlertConfigCreate(_AlertsConfigBase, InternalModel):
    """This model represents the alerts config for
    specific activity items answer for save in database
    """

    alert_message: str = Field(
        description="This field represents the alert message "
        "which will be shown"
    )
    viewed: bool = Field(
        description="This is a boolean field that represents "
        "whether the alerts will be shown to the user",
        default=True,
    )


class AlertConfig(AlertConfigCreate):
    """This model represents the alert config"""

    id: uuid.UUID = Field(
        description="This field represents the id "
        "for specific alert configuration"
    )


class AlertConfigGet(_AlertsConfigBase, PublicModel):
    """This model used for internal needs
    to get the specific alert config from database
    """


class _AlertsConfigUpdateBase(BaseModel):
    """This model used for internal needs
    as a base model for request and response
    """

    applet_id: uuid.UUID = Field(
        description="This field represents the specific applet id"
    )
    specific_answer: str = Field(
        description="This field represents the specific answer "
        "upon selection of which an alert will be created"
    )
    alert_message: str = Field(
        description="This field represents the alert message "
        "which will be shown"
    )
    viewed: bool = Field(
        description="This is a boolean field that represents "
        "whether the alerts will be shown to the user",
        default=True,
    )


class AlertsConfigUpdateRequest(_AlertsConfigUpdateBase, PublicModel):
    """This model represents the request for update configuration
    alerts for specific applet
    """


class AlertConfigUpdate(_AlertsConfigUpdateBase, InternalModel):
    """This model represents the alerts config for
    update in database
    """
