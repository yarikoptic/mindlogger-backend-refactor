import datetime
import uuid
from typing import Any

from pydantic import Field

from apps.activities.domain.activity_full import PublicActivityItemFull
from apps.activities.domain.response_type_config import ResponseType
from apps.shared.domain import InternalModel, PublicModel


class Text(InternalModel):
    value: str
    should_identify_response: bool = False


class SingleSelection(InternalModel):
    value: uuid.UUID
    additional_text: str | None


class MultipleSelection(InternalModel):
    value: list[uuid.UUID]
    additional_text: str | None


class Slider(InternalModel):
    value: float
    additional_text: str | None


AnswerTypes = SingleSelection | Slider | MultipleSelection | Text

ANSWER_TYPE_MAP: dict[ResponseType, Any] = {
    ResponseType.TEXT: Text,
    ResponseType.SINGLESELECT: SingleSelection,
    ResponseType.MULTISELECT: MultipleSelection,
    ResponseType.SLIDER: Slider,
}


class ActivityItemAnswerCreate(InternalModel):
    activity_item_id: uuid.UUID
    answer: AnswerTypes


class AnsweredActivityItem(InternalModel):
    activity_item_history_id: str
    answer: str


class AppletAnswerCreate(InternalModel):
    applet_id: uuid.UUID
    version: str
    flow_id: uuid.UUID | None = None
    activity_id: uuid.UUID
    answers: list[ActivityItemAnswerCreate]
    created_at: int | None


class AnswerDate(InternalModel):
    created_at: datetime.datetime
    answer_id: uuid.UUID


class AnsweredAppletActivity(InternalModel):
    id: uuid.UUID
    name: str
    answer_dates: list[AnswerDate] = Field(default_factory=list)


class PublicAnswerDate(PublicModel):
    created_at: datetime.datetime
    answer_id: uuid.UUID


class PublicAnsweredAppletActivity(PublicModel):
    id: uuid.UUID
    name: str
    answer_dates: list[PublicAnswerDate] = Field(default_factory=list)


class PublicAnswerDates(PublicModel):
    dates: list[datetime.date]


class ActivityItemAnswer(InternalModel):
    type: ResponseType
    activity_item: PublicActivityItemFull
    answer: AnswerTypes


class ActivityAnswer(InternalModel):
    activity_item_answers: list[ActivityItemAnswer] = Field(
        default_factory=list
    )


class ActivityItemAnswerPublic(PublicModel):
    type: ResponseType
    activity_item: PublicActivityItemFull
    answer: AnswerTypes


class ActivityAnswerPublic(PublicModel):
    activity_item_answers: list[ActivityItemAnswerPublic] = Field(
        default_factory=list
    )


class AnswerNote(InternalModel):
    note: str


class NoteOwner(InternalModel):
    first_name: str
    last_name: str


class AnswerNoteDetail(InternalModel):
    id: uuid.UUID
    user: NoteOwner
    note: str
    created_at: datetime.datetime


class NoteOwnerPublic(PublicModel):
    first_name: str
    last_name: str


class AnswerNoteDetailPublic(PublicModel):
    id: uuid.UUID
    user: NoteOwnerPublic
    note: str
    created_at: datetime.datetime
