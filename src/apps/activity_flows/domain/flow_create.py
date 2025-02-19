import uuid

from apps.activity_flows.domain.base import FlowBase
from apps.shared.domain import InternalModel


class FlowItemCreate(InternalModel):
    activity_key: uuid.UUID


class PreparedFlowItemCreate(InternalModel):
    activity_flow_id: uuid.UUID
    activity_id: uuid.UUID


class FlowCreate(FlowBase, InternalModel):
    items: list[FlowItemCreate]
