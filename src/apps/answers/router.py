from fastapi.routing import APIRouter
from starlette import status

from apps.answers.api import (
    applet_activities_list,
    applet_answer_retrieve,
    create_answer,
    note_add,
    note_list,
)
from apps.answers.domain import (
    ActivityAnswerPublic,
    PublicAnsweredAppletActivity, AnswerNoteDetailPublic,
)
from apps.shared.domain import Response, ResponseMulti, \
    AUTHENTICATION_ERROR_RESPONSES
from apps.shared.domain.response import DEFAULT_OPENAPI_RESPONSE

router = APIRouter(prefix="/answers", tags=["Answers"])

# Answers for activity item create
router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    responses={
        **DEFAULT_OPENAPI_RESPONSE,
        **AUTHENTICATION_ERROR_RESPONSES,
    },
)(create_answer)

router.get(
    "/applet/{id_}/activities",
    status_code=status.HTTP_200_OK,
    response_model=ResponseMulti[PublicAnsweredAppletActivity],
    responses={
        **DEFAULT_OPENAPI_RESPONSE,
        **AUTHENTICATION_ERROR_RESPONSES,
    },
)(applet_activities_list)

router.get(
    "/applet/{applet_id}/answers/{answer_id}",
    status_code=status.HTTP_200_OK,
    response_model=Response[ActivityAnswerPublic],
    responses={
        **DEFAULT_OPENAPI_RESPONSE,
        **AUTHENTICATION_ERROR_RESPONSES,
    },
)(applet_answer_retrieve)

router.post(
    "/applet/{applet_id}/answers/{answer_id}/notes",
    status_code=status.HTTP_201_CREATED,
    responses={
        **DEFAULT_OPENAPI_RESPONSE,
        **AUTHENTICATION_ERROR_RESPONSES,
    },
)(note_add)

router.get(
    "/applet/{applet_id}/answers/{answer_id}/notes",
    status_code=status.HTTP_200_OK,
    response_model=ResponseMulti[AnswerNoteDetailPublic],
    responses={
        **DEFAULT_OPENAPI_RESPONSE,
        **AUTHENTICATION_ERROR_RESPONSES,
    },
)(note_list)
