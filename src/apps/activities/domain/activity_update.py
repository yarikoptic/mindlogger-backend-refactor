import uuid

from pydantic import root_validator

from apps.activities.domain.activity_base import ActivityBase
from apps.activities.domain.activity_item_base import BaseActivityItem
from apps.activities.errors import DuplicateActivityItemNameNameError
from apps.shared.domain import InternalModel


class ActivityItemUpdate(BaseActivityItem, InternalModel):
    id: uuid.UUID | None


class PreparedActivityItemUpdate(BaseActivityItem, InternalModel):
    id: uuid.UUID | None
    activity_id: uuid.UUID


class ActivityUpdate(ActivityBase, InternalModel):
    id: uuid.UUID | None
    key: uuid.UUID
    items: list[ActivityItemUpdate]

    @root_validator()
    def validate_existing_ids_for_duplicate(cls, values):
        items = values.get("items", [])

        item_names = set()
        for item in items:  # type:ActivityItemUpdate
            if item.name in item_names:
                raise DuplicateActivityItemNameNameError()
            item_names.add(item.name)
        return values
