from unittest.mock import patch

from starlette import status

from apps.authentication.domain.token import Token
from apps.authentication.router import router as auth_router
from apps.authentication.services import AuthenticationService, TokensService
from apps.shared.domain.response import Response
from apps.shared.test import BaseTest
from apps.users import UsersCRUD
from apps.users.domain import UserLoginRequest
from apps.users.router import router as user_router
from apps.users.tests import UserCreateRequestFactory
from infrastructure.database import transaction


class TestAuthentication(BaseTest):
    user_create_url = user_router.url_path_for("user_create")
    get_token_url = auth_router.url_path_for("get_token")
    delete_token_url = auth_router.url_path_for("delete_access_token")
    refresh_access_token_url = auth_router.url_path_for("refresh_access_token")

    create_request_user = UserCreateRequestFactory.build()

    @transaction.rollback
    async def test_get_token(self):
        # Creating new user
        await self.client.post(
            self.user_create_url, data=self.create_request_user.dict()
        )

        login_request_user: UserLoginRequest = UserLoginRequest(
            **self.create_request_user.dict()
        )

        # User get token
        response = await self.client.post(
            url=self.get_token_url,
            data=login_request_user.dict(),
        )

        user = await UsersCRUD().get_by_email(
            email=self.create_request_user.dict()["email"]
        )

        access_token = AuthenticationService.create_access_token(
            {"sub": str(user.id)}
        )

        refresh_token = AuthenticationService.create_refresh_token(
            {"sub": str(user.id)}
        )

        expected_result = Response(
            result=Token(
                access_token=access_token, refresh_token=refresh_token
            )
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == expected_result.dict(by_alias=True)

    @transaction.rollback
    @patch(
        "apps.authentication.services.core.TokensService.add_access_token_to_blacklist"
    )
    async def test_delete_access_token(
        self,
        mock_object_set,
    ):

        # Creating new user
        await self.client.post(
            self.user_create_url, data=self.create_request_user.dict()
        )

        login_request_user: UserLoginRequest = UserLoginRequest(
            **self.create_request_user.dict()
        )

        # User get token
        internal_response = await self.client.get_token(
            url=self.get_token_url,
            user_login_request=login_request_user,
        )

        response = await self.client.post(url=self.delete_token_url)

        assert mock_object_set is TokensService.add_access_token_to_blacklist
