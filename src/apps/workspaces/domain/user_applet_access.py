import uuid

from pydantic import Field

from apps.applets.domain.applets import public_detail
from apps.applets.domain.base import Encryption

# from apps.applets.domain.base import Encryption
from apps.shared.domain import InternalModel, PublicModel
from apps.workspaces.domain.constants import Role

__all__ = [
    "UserAppletAccessCreate",
    "UserAppletAccess",
    "PublicUserAppletAccess",
    "UserAppletAccessItem",
    "RemoveRespondentAccess",
    "RemoveManagerAccess",
    "ManagerAccesses",
    "ManagerAppletAccess",
    "PublicRespondentAppletAccess",
]


class UserAppletAccessCreate(InternalModel):
    user_id: uuid.UUID
    applet_id: uuid.UUID
    role: Role
    owner_id: uuid.UUID
    invitor_id: uuid.UUID
    meta: dict
    is_pinned: bool


class UserAppletAccess(UserAppletAccessCreate):
    id: uuid.UUID


class PublicUserAppletAccess(PublicModel):
    """Public UserAppletAccess data model."""

    id: uuid.UUID
    user_id: uuid.UUID
    applet_id: uuid.UUID
    role: Role


class UserAppletAccessItem(InternalModel):
    """This is an UserAppletAccess representation for internal needs."""

    user_id: uuid.UUID
    applet_id: uuid.UUID
    role: Role


class RemoveManagerAccess(InternalModel):
    """Manager access removal model."""

    user_id: uuid.UUID = Field(
        description="This field represents the user id",
    )
    applet_ids: list[uuid.UUID] = Field(
        description="This field represents the applet ids",
    )


class RemoveRespondentAccess(InternalModel):
    """Respondent access removal model."""

    user_id: uuid.UUID = Field(
        description="This field represents the user id",
    )
    applet_ids: list[uuid.UUID] = Field(
        description="This field represents the applet ids",
    )
    delete_responses: bool = Field(
        description="This field represents the flag for deleting responses",
    )


class AppletUser(InternalModel):
    id: uuid.UUID
    first_name: str
    last_name: str
    roles: list[str]


class PublicAppletUser(PublicModel):
    id: uuid.UUID
    first_name: str
    last_name: str
    roles: list[str]


class RespondentAppletAccess(InternalModel):
    applet_id: uuid.UUID
    applet_name: str
    applet_image: str
    secret_user_id: str
    nickname: str
    has_individual_schedule: bool
    encryption: Encryption | None


class ManagerAppletAccess(InternalModel):
    applet_id: uuid.UUID
    applet_name: str
    applet_image: str
    roles: list[Role]


class PublicRespondentAppletAccess(PublicModel):
    applet_id: uuid.UUID
    applet_name: str
    applet_image: str
    secret_user_id: str
    nickname: str
    has_individual_schedule: bool
    encryption: public_detail.Encryption | None


class PublicManagerAppletAccess(PublicModel):
    applet_id: uuid.UUID
    applet_name: str
    applet_image: str
    roles: list[Role]


class ManagerAccess(InternalModel):
    applet_id: uuid.UUID
    roles: list[Role]
    respondents: list[uuid.UUID] | None


class ManagerAccesses(InternalModel):
    accesses: list[ManagerAccess]


class RespondentInfo(InternalModel):
    nickname: str
    secret_user_id: str
