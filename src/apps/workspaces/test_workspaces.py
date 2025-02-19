import uuid
from uuid import uuid4

from apps.shared.test import BaseTest
from apps.workspaces.domain.constants import Role
from infrastructure.database import rollback


class TestWorkspaces(BaseTest):
    fixtures = [
        "users/fixtures/users.json",
        "folders/fixtures/folders.json",
        "applets/fixtures/applets.json",
        "applets/fixtures/applet_user_accesses.json",
        "activities/fixtures/activities.json",
        "activities/fixtures/activity_items.json",
        "activity_flows/fixtures/activity_flows.json",
        "activity_flows/fixtures/activity_flow_items.json",
        "invitations/fixtures/invitations.json",
        "workspaces/fixtures/workspaces.json",
        "schedule/fixtures/periodicity.json",
        "schedule/fixtures/events.json",
        "schedule/fixtures/activity_events.json",
        "schedule/fixtures/flow_events.json",
        "schedule/fixtures/user_events.json",
        "folders/fixtures/folders_applet.json",
    ]

    login_url = "/auth/login"
    workspaces_list_url = "/workspaces"
    workspaces_detail_url = f"{workspaces_list_url}/{{owner_id}}"
    workspaces_priority_role_url = f"{workspaces_detail_url}/priority_role"
    workspace_roles_url = f"{workspaces_detail_url}/roles"
    workspace_applets_url = f"{workspaces_detail_url}/applets"
    workspace_applets_detail_url = f"{workspace_applets_url}/{{applet_id}}"
    applet_respondent_url = (
        f"{workspace_applets_detail_url}/respondents/{{respondent_id}}"
    )
    workspace_respondents_url = f"{workspaces_detail_url}/respondents"
    workspace_applet_respondents_list = (
        "/workspaces/{owner_id}/applets/{applet_id}/respondents"
    )
    workspace_respondent_applet_accesses = (
        f"{workspace_respondents_url}/{{respondent_id}}/accesses"
    )
    workspace_managers_url = f"{workspaces_detail_url}/managers"
    workspace_applet_managers_list = (
        "/workspaces/{owner_id}/applets/{applet_id}/managers"
    )
    workspace_manager_accesses_url = (
        f"{workspace_managers_url}/{{manager_id}}/accesses"
    )
    remove_manager_access = f"{workspaces_list_url}/removeAccess"
    remove_respondent_access = "/applets/removeAccess"
    workspace_respondents_pin = (
        "/workspaces/{owner_id}/respondents/{user_id}/pin"
    )
    workspace_managers_pin = "/workspaces/{owner_id}/managers/{user_id}/pin"

    @rollback
    async def test_user_workspace_list(self):
        await self.client.login(self.login_url, "lucy@gmail.com", "Test123")

        response = await self.client.get(
            self.workspaces_list_url.format(
                owner_id="7484f34a-3acc-4ee6-8a94-fd7299502fa2"
            )
        )
        assert response.status_code == 200, response.json()
        assert len(response.json()["result"]) == 2

    @rollback
    async def test_user_workspace_retrieve_without_managers(self):
        await self.client.login(self.login_url, "lucy@gmail.com", "Test123")

        response = await self.client.get(
            self.workspaces_detail_url.format(
                owner_id="7484f34a-3acc-4ee6-8a94-fd7299502fa2"
            )
        )
        assert response.status_code == 200, response.json()
        assert response.json()["result"]["name"] == "Lucy Gabel Test"
        assert response.json()["result"]["hasManagers"] is False

    @rollback
    async def test_get_users_priority_role_in_workspace(self):
        await self.client.login(self.login_url, "bob@gmail.com", "Test1234!")

        response = await self.client.get(
            self.workspaces_priority_role_url.format(
                owner_id="7484f34a-3acc-4ee6-8a94-fd7299502fa1"
            )
        )
        assert response.status_code == 200, response.json()
        assert response.json()["result"]["role"] == Role.COORDINATOR

    @rollback
    async def test_workspace_roles_retrieve(self):
        await self.client.login(self.login_url, "lucy@gmail.com", "Test123")

        response = await self.client.get(
            self.workspace_roles_url.format(
                owner_id="7484f34a-3acc-4ee6-8a94-fd7299502fa1"
            )
        )
        assert response.status_code == 200, response.json()
        data = response.json()["result"]
        roles = data.get("92917a56-d586-4613-b7aa-991f2c4b15b1", [])
        assert roles == [Role.MANAGER, Role.RESPONDENT]

    @rollback
    async def test_workspace_roles_with_super_admin_retrieve(self):
        await self.client.login(
            self.login_url, "tom@mindlogger.com", "Test1234!"
        )

        response = await self.client.get(
            self.workspace_roles_url.format(
                owner_id="7484f34a-3acc-4ee6-8a94-fd7299502fa1"
            )
        )
        assert response.status_code == 200, response.json()
        data = response.json()["result"]
        roles = data.get("92917a56-d586-4613-b7aa-991f2c4b15b1", [])
        assert roles == [Role.OWNER, Role.SUPER_ADMIN, Role.RESPONDENT]

    @rollback
    async def test_user_workspace_retrieve_with_managers(self):
        await self.client.login(
            self.login_url, "tom@mindlogger.com", "Test1234!"
        )

        response = await self.client.get(
            self.workspaces_detail_url.format(
                owner_id="7484f34a-3acc-4ee6-8a94-fd7299502fa1"
            )
        )
        assert response.status_code == 200, response.json()
        assert response.json()["result"]["name"] == "Tom Isaak Test"
        assert response.json()["result"]["hasManagers"] is True

    @rollback
    async def test_user_workspace_retrieve_without_access(self):
        await self.client.login(
            self.login_url, "tom@mindlogger.com", "Test1234!"
        )

        response = await self.client.get(
            self.workspaces_detail_url.format(
                owner_id="7484f34a-3acc-4ee6-8a94-fd7299502fa2"
            )
        )
        assert response.status_code == 403, response.json()

    @rollback
    async def test_workspace_applets_list(self):
        await self.client.login(self.login_url, "lucy@gmail.com", "Test123")

        response = await self.client.get(
            self.workspace_applets_url.format(
                owner_id="7484f34a-3acc-4ee6-8a94-fd7299502fa2"
            )
        )
        assert response.status_code == 200
        assert response.json()["count"] == 1
        assert response.json()["result"][0]["role"] == Role.OWNER

    @rollback
    async def test_workspace_applets_list_by_folder_id_filter(self):
        await self.client.login(
            self.login_url, "tom@mindlogger.com", "Test1234!"
        )

        response = await self.client.get(
            self.workspace_applets_url.format(
                owner_id="7484f34a-3acc-4ee6-8a94-fd7299502fa1"
            ),
        )
        assert response.status_code == 200
        assert response.json()["count"] == 2

        response = await self.client.get(
            self.workspace_applets_url.format(
                owner_id="7484f34a-3acc-4ee6-8a94-fd7299502fa1"
            ),
            dict(folderId=uuid.uuid4()),
        )
        assert response.status_code == 200
        assert response.json()["count"] == 0

    @rollback
    async def test_workspace_applets_detail(self):
        await self.client.login(self.login_url, "lucy@gmail.com", "Test123")

        # check access not exists
        response = await self.client.get(
            self.workspace_applets_detail_url.format(
                owner_id=uuid4(),
                applet_id="92917a56-d586-4613-b7aa-991f2c4b15b1",
            )
        )
        assert response.status_code == 404

        response = await self.client.get(
            self.workspace_applets_detail_url.format(
                owner_id="7484f34a-3acc-4ee6-8a94-fd7299502fa2",
                applet_id="92917a56-d586-4613-b7aa-991f2c4b15b1",
            )
        )
        assert response.status_code == 200

    @rollback
    async def test_workspace_applets_respondent_update(self):
        await self.client.login(
            self.login_url, "tom@mindlogger.com", "Test1234!"
        )

        response = await self.client.post(
            self.applet_respondent_url.format(
                owner_id="7484f34a-3acc-4ee6-8a94-fd7299502fa1",
                applet_id="92917a56-d586-4613-b7aa-991f2c4b15b1",
                respondent_id="7484f34a-3acc-4ee6-8a94-fd7299502fa2",
            ),
            dict(
                nickname="New respondent",
                secret_user_id="f0dd4996-e0eb-461f-b2f8-ba873a674710",
            ),
        )
        assert response.status_code == 200

        response = await self.client.get(
            self.workspace_applet_respondents_list.format(
                owner_id="7484f34a-3acc-4ee6-8a94-fd7299502fa1",
                applet_id="92917a56-d586-4613-b7aa-991f2c4b15b1",
            ),
            dict(
                role="respondent",
            ),
        )
        assert response.json()["count"] == 2
        assert "New respondent" in response.json()["result"][0]["nicknames"]
        assert (
            "f0dd4996-e0eb-461f-b2f8-ba873a674710"
            in response.json()["result"][0]["secretIds"]
        )

    @rollback
    async def test_wrong_workspace_applets_list(self):
        await self.client.login(self.login_url, "lucy@gmail.com", "Test123")

        response = await self.client.get(
            self.workspace_applets_url.format(
                owner_id="00000000-0000-0000-0000-000000000000"
            )
        )
        assert response.status_code == 404

    @rollback
    async def test_get_workspace_respondents(self):
        await self.client.login(
            self.login_url, "tom@mindlogger.com", "Test1234!"
        )
        response = await self.client.get(
            self.workspace_respondents_url.format(
                owner_id="7484f34a-3acc-4ee6-8a94-fd7299502fa1"
            ),
        )

        assert response.status_code == 200, response.json()
        data = response.json()
        assert data["count"] == 2
        assert data["result"][0]["nicknames"]
        assert data["result"][0]["secretIds"]

        # test search
        search_params = {
            "f0dd4996-e0eb-461f-b2f8-ba873a674788": [
                "jane",
                "b2f8-ba873a674788",
            ],
            "f0dd4996-e0eb-461f-b2f8-ba873a674789": [
                "john",
                "f0dd4996-e0eb-461f-b2f8-ba873a674789",
            ],
        }
        for access_id, params in search_params.items():
            for val in params:
                response = await self.client.get(
                    self.workspace_respondents_url.format(
                        owner_id="7484f34a-3acc-4ee6-8a94-fd7299502fa1"
                    ),
                    dict(search=val),
                )
                assert response.status_code == 200
                data = response.json()
                assert set(data.keys()) == {"count", "result"}
                assert data["count"] == 1
                result = data["result"]
                assert len(result) == 1
                access_ids = {
                    detail["accessId"] for detail in result[0]["details"]
                }
                assert access_id in access_ids

    @rollback
    async def test_get_workspace_applet_respondents(self):
        await self.client.login(
            self.login_url, "tom@mindlogger.com", "Test1234!"
        )
        response = await self.client.get(
            self.workspace_applet_respondents_list.format(
                owner_id="7484f34a-3acc-4ee6-8a94-fd7299502fa1",
                applet_id="92917a56-d586-4613-b7aa-991f2c4b15b1",
            ),
        )

        assert response.status_code == 200, response.json()
        data = response.json()
        assert data["count"] == 2
        assert data["result"][0]["nicknames"]
        assert data["result"][0]["secretIds"]

        # test search
        search_params = {
            "f0dd4996-e0eb-461f-b2f8-ba873a674788": [
                "jane",
                "b2f8-ba873a674788",
            ],
            "f0dd4996-e0eb-461f-b2f8-ba873a674789": [
                "john",
                "f0dd4996-e0eb-461f-b2f8-ba873a674789",
            ],
        }
        for access_id, params in search_params.items():
            for val in params:
                response = await self.client.get(
                    self.workspace_applet_respondents_list.format(
                        owner_id="7484f34a-3acc-4ee6-8a94-fd7299502fa1",
                        applet_id="92917a56-d586-4613-b7aa-991f2c4b15b1",
                    ),
                    dict(search=val),
                )
                assert response.status_code == 200
                data = response.json()
                assert set(data.keys()) == {"count", "result"}
                assert data["count"] == 1
                result = data["result"]
                assert len(result) == 1
                access_ids = {
                    detail["accessId"] for detail in result[0]["details"]
                }
                assert access_id in access_ids

    @rollback
    async def test_get_workspace_respondent_accesses(self):
        await self.client.login(
            self.login_url, "tom@mindlogger.com", "Test1234!"
        )
        response = await self.client.get(
            self.workspace_respondent_applet_accesses.format(
                owner_id="7484f34a-3acc-4ee6-8a94-fd7299502fa1",
                respondent_id="7484f34a-3acc-4ee6-8a94-fd7299502fa2",
            )
        )

        assert response.status_code == 200, response.json()
        assert response.json()["count"] == 1

    @rollback
    async def test_get_workspace_managers(self):
        await self.client.login(
            self.login_url, "tom@mindlogger.com", "Test1234!"
        )
        response = await self.client.get(
            self.workspace_managers_url.format(
                owner_id="7484f34a-3acc-4ee6-8a94-fd7299502fa1"
            ),
        )

        assert response.status_code == 200, response.json()
        assert response.json()["count"] == 5

        # test search
        search_params = {
            "7484f34a-3acc-4ee6-8a94-fd7299502fa2": [
                "lucy",
                "gabe",
                "lucy@gmail",
            ],
        }
        for id_, params in search_params.items():
            for val in params:
                response = await self.client.get(
                    self.workspace_managers_url.format(
                        owner_id="7484f34a-3acc-4ee6-8a94-fd7299502fa1"
                    ),
                    dict(
                        search=val,
                    ),
                )

                assert response.status_code == 200
                data = response.json()
                assert set(data.keys()) == {"count", "result"}
                assert data["count"] == 1
                result = data["result"]
                assert len(result) == 1
                assert result[0]["id"] == id_

    @rollback
    async def test_get_workspace_applet_managers(self):
        await self.client.login(
            self.login_url, "tom@mindlogger.com", "Test1234!"
        )
        response = await self.client.get(
            self.workspace_applet_managers_list.format(
                owner_id="7484f34a-3acc-4ee6-8a94-fd7299502fa1",
                applet_id="92917a56-d586-4613-b7aa-991f2c4b15b1",
            ),
        )

        assert response.status_code == 200, response.json()
        assert response.json()["count"] == 5

        # test search
        search_params = {
            "7484f34a-3acc-4ee6-8a94-fd7299502fa2": [
                "lucy",
                "gabe",
                "lucy@gmail",
            ],
        }
        for id_, params in search_params.items():
            for val in params:
                response = await self.client.get(
                    self.workspace_applet_managers_list.format(
                        owner_id="7484f34a-3acc-4ee6-8a94-fd7299502fa1",
                        applet_id="92917a56-d586-4613-b7aa-991f2c4b15b1",
                    ),
                    dict(
                        search=val,
                    ),
                )

                assert response.status_code == 200
                data = response.json()
                assert set(data.keys()) == {"count", "result"}
                assert data["count"] == 1
                result = data["result"]
                assert len(result) == 1
                assert result[0]["id"] == id_

    @rollback
    async def test_get_workspace_manager_accesses(self):
        await self.client.login(
            self.login_url, "tom@mindlogger.com", "Test1234!"
        )
        response = await self.client.get(
            self.workspace_manager_accesses_url.format(
                owner_id="7484f34a-3acc-4ee6-8a94-fd7299502fa1",
                manager_id="7484f34a-3acc-4ee6-8a94-fd7299502fa2",
            )
        )

        assert response.status_code == 200, response.json()
        assert response.json()["count"] == 1
        assert (
            response.json()["result"][0]["appletId"]
            == "92917a56-d586-4613-b7aa-991f2c4b15b1"
        )
        assert response.json()["result"][0]["roles"][0] == "manager"

    @rollback
    async def test_set_workspace_manager_accesses(self):
        await self.client.login(
            self.login_url, "tom@mindlogger.com", "Test1234!"
        )
        response = await self.client.post(
            self.workspace_manager_accesses_url.format(
                owner_id="7484f34a-3acc-4ee6-8a94-fd7299502fa1",
                manager_id="7484f34a-3acc-4ee6-8a94-fd7299502fa2",
            ),
            dict(
                accesses=[
                    {
                        "applet_id": "92917a56-d586-4613-b7aa-991f2c4b15b4",
                        "roles": ["manager", "coordinator"],
                    },
                    {
                        "applet_id": "92917a56-d586-4613-b7aa-991f2c4b15b1",
                        "roles": ["coordinator", "editor", "reviewer"],
                        "respondents": [
                            "7484f34a-3acc-4ee6-8a94-fd7299502fa1",
                            "7484f34a-3acc-4ee6-8a94-fd7299502fa2",
                        ],
                    },
                ]
            ),
        )

        assert response.status_code == 200, response.json()

        response = await self.client.get(
            self.workspace_manager_accesses_url.format(
                owner_id="7484f34a-3acc-4ee6-8a94-fd7299502fa1",
                manager_id="7484f34a-3acc-4ee6-8a94-fd7299502fa2",
            )
        )

        assert response.status_code == 200, response.json()
        assert response.json()["count"] == 2
        assert (
            response.json()["result"][0]["appletId"]
            == "92917a56-d586-4613-b7aa-991f2c4b15b1"
        )
        assert response.json()["result"][0]["roles"][0] == "coordinator"
        assert response.json()["result"][0]["roles"][1] == "editor"

        assert (
            response.json()["result"][1]["appletId"]
            == "92917a56-d586-4613-b7aa-991f2c4b15b4"
        )
        assert response.json()["result"][1]["roles"][0] == "manager"

    @rollback
    async def test_pin_workspace_respondents(self):
        await self.client.login(
            self.login_url, "tom@mindlogger.com", "Test1234!"
        )
        response = await self.client.get(
            self.workspace_applet_respondents_list.format(
                owner_id="7484f34a-3acc-4ee6-8a94-fd7299502fa1",
                applet_id="92917a56-d586-4613-b7aa-991f2c4b15b1",
            ),
        )

        assert response.status_code == 200, response.json()

        user_id = response.json()["result"][-1]["id"]

        # Pin access wrong owner
        response = await self.client.post(
            self.workspace_respondents_pin.format(
                owner_id=uuid4(), user_id=user_id
            ),
        )

        assert response.status_code == 404

        # Pin access wrong access_id
        response = await self.client.post(
            self.workspace_respondents_pin.format(
                owner_id="7484f34a-3acc-4ee6-8a94-fd7299502fa1",
                user_id=uuid4(),
            ),
        )

        assert response.status_code == 403

        # Pin access
        response = await self.client.post(
            self.workspace_respondents_pin.format(
                owner_id="7484f34a-3acc-4ee6-8a94-fd7299502fa1",
                user_id=user_id,
            ),
        )

        assert response.status_code == 204

        response = await self.client.get(
            self.workspace_applet_respondents_list.format(
                owner_id="7484f34a-3acc-4ee6-8a94-fd7299502fa1",
                applet_id="92917a56-d586-4613-b7aa-991f2c4b15b1",
            ),
        )
        assert response.json()["result"][0]["id"] == user_id
        assert response.json()["result"][0]["isPinned"] is True
        assert response.json()["result"][1]["isPinned"] is False

        # Unpin access
        response = await self.client.post(
            self.workspace_respondents_pin.format(
                owner_id="7484f34a-3acc-4ee6-8a94-fd7299502fa1",
                user_id=user_id,
            ),
        )

        assert response.status_code == 204

        response = await self.client.get(
            self.workspace_applet_respondents_list.format(
                owner_id="7484f34a-3acc-4ee6-8a94-fd7299502fa1",
                applet_id="92917a56-d586-4613-b7aa-991f2c4b15b1",
            ),
        )
        assert response.json()["result"][-1]["id"] == user_id

    @rollback
    async def test_pin_workspace_managers(self):
        await self.client.login(
            self.login_url, "tom@mindlogger.com", "Test1234!"
        )
        response = await self.client.get(
            self.workspace_applet_managers_list.format(
                owner_id="7484f34a-3acc-4ee6-8a94-fd7299502fa1",
                applet_id="92917a56-d586-4613-b7aa-991f2c4b15b1",
            ),
        )

        assert response.status_code == 200, response.json()

        user_id = response.json()["result"][-1]["id"]

        # Pin access wrong owner
        response = await self.client.post(
            self.workspace_managers_pin.format(
                owner_id=uuid4(), user_id=user_id
            ),
        )

        assert response.status_code == 404

        # Pin access wrong access_id
        response = await self.client.post(
            self.workspace_managers_pin.format(
                owner_id="7484f34a-3acc-4ee6-8a94-fd7299502fa1",
                user_id=uuid4(),
            ),
        )

        assert response.status_code == 403

        # Pin access
        response = await self.client.post(
            self.workspace_managers_pin.format(
                owner_id="7484f34a-3acc-4ee6-8a94-fd7299502fa1",
                user_id=user_id,
            ),
        )

        assert response.status_code == 204

        response = await self.client.get(
            self.workspace_applet_managers_list.format(
                owner_id="7484f34a-3acc-4ee6-8a94-fd7299502fa1",
                applet_id="92917a56-d586-4613-b7aa-991f2c4b15b1",
            ),
        )
        assert response.json()["result"][0]["id"] == user_id
        assert response.json()["result"][0]["isPinned"] is True
        assert response.json()["result"][1]["isPinned"] is False

        # Unpin access
        response = await self.client.post(
            self.workspace_managers_pin.format(
                owner_id="7484f34a-3acc-4ee6-8a94-fd7299502fa1",
                user_id=user_id,
            ),
        )

        assert response.status_code == 204

        response = await self.client.get(
            self.workspace_applet_managers_list.format(
                owner_id="7484f34a-3acc-4ee6-8a94-fd7299502fa1",
                applet_id="92917a56-d586-4613-b7aa-991f2c4b15b1",
            ),
        )
        assert response.json()["result"][-1]["id"] == user_id

    @rollback
    async def test_workspace_remove_manager_access(self):
        await self.client.login(
            self.login_url, "tom@mindlogger.com", "Test1234!"
        )
        response = await self.client.get(
            self.workspace_managers_url.format(
                owner_id="7484f34a-3acc-4ee6-8a94-fd7299502fa1"
            )
        )

        assert response.status_code == 200

        managers_count = response.json()["count"]

        data = {
            "user_id": "7484f34a-3acc-4ee6-8a94-fd7299502fa2",
            "applet_ids": [
                "92917a56-d586-4613-b7aa-991f2c4b15b1",
            ],
            # "role": Role.MANAGER,
        }

        response = await self.client.post(
            self.remove_manager_access, data=data
        )

        assert response.status_code == 200

        response = await self.client.get(
            self.workspace_managers_url.format(
                owner_id="7484f34a-3acc-4ee6-8a94-fd7299502fa1"
            )
        )

        assert response.status_code == 200
        assert response.json()["count"] == managers_count - 1

    @rollback
    async def test_workspace_remove_respondent_access(self):
        await self.client.login(
            self.login_url, "tom@mindlogger.com", "Test1234!"
        )

        data = {
            "user_id": "7484f34a-3acc-4ee6-8a94-fd7299502fa2",
            "applet_ids": [
                "92917a56-d586-4613-b7aa-991f2c4b15b1",
            ],
            "delete_responses": True,
        }

        response = await self.client.post(
            self.remove_respondent_access, data=data
        )
        assert response.status_code == 200
