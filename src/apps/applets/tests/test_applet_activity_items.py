import uuid

from apps.shared.test import BaseTest
from infrastructure.database import rollback


class TestActivityItems(BaseTest):
    fixtures = [
        "users/fixtures/users.json",
        "themes/fixtures/themes.json",
        "folders/fixtures/folders.json",
        "applets/fixtures/applets.json",
        "applets/fixtures/applet_histories.json",
        "applets/fixtures/applet_user_accesses.json",
        "activities/fixtures/activities.json",
        "activities/fixtures/activity_items.json",
        "activity_flows/fixtures/activity_flows.json",
        "activity_flows/fixtures/activity_flow_items.json",
    ]

    login_url = "/auth/login"
    applet_list_url = "applets"
    applet_create_url = "workspaces/{owner_id}/applets"
    applet_detail_url = f"{applet_list_url}/{{pk}}"
    activity_detail_url = "activities/{activity_id}"

    @rollback
    async def test_creating_applet_with_activity_items(self):
        await self.client.login(
            self.login_url, "tom@mindlogger.com", "Test1234!"
        )
        create_data = dict(
            display_name="User daily behave",
            encryption=dict(
                public_key=uuid.uuid4().hex,
                prime=uuid.uuid4().hex,
                base=uuid.uuid4().hex,
                account_id=str(uuid.uuid4()),
            ),
            description=dict(
                en="Understand users behave",
                fr="Comprendre le comportement des utilisateurs",
            ),
            about=dict(
                en="Understand users behave",
                fr="Comprendre le comportement des utilisateurs",
            ),
            activities=[
                dict(
                    name="Morning activity",
                    key="577dbbda-3afc-4962-842b-8d8d11588bfe",
                    description=dict(
                        en="Understand morning feelings.",
                        fr="Understand morning feelings.",
                    ),
                    items=[
                        dict(
                            name="activity_item_text",
                            question=dict(
                                en="How had you slept?",
                                fr="How had you slept?",
                            ),
                            response_type="text",
                            response_values=None,
                            config=dict(
                                max_response_length=200,
                                correct_answer_required=False,
                                correct_answer=None,
                                numerical_response_required=False,
                                response_data_identifier=False,
                                response_required=False,
                                remove_back_button=False,
                                skippable_item=True,
                            ),
                        ),
                        dict(
                            name="activity_item_message",
                            question={"en": "What is your name?"},
                            response_type="message",
                            response_values=None,
                            config=dict(
                                remove_back_button=False,
                                timer=1,
                            ),
                        ),
                        dict(
                            name="activity_item_number_selection",
                            question={"en": "What is your name?"},
                            response_type="numberSelect",
                            response_values=dict(
                                min_value=0,
                                max_value=10,
                            ),
                            config=dict(
                                additional_response_option={
                                    "text_input_option": False,
                                    "text_input_required": False,
                                },
                                remove_back_button=False,
                                skippable_item=False,
                            ),
                        ),
                        dict(
                            name="activity_item_time_range",
                            question={"en": "What is your name?"},
                            response_type="timeRange",
                            response_values=None,
                            config=dict(
                                additional_response_option={
                                    "text_input_option": False,
                                    "text_input_required": False,
                                },
                                remove_back_button=False,
                                skippable_item=False,
                                timer=1,
                            ),
                        ),
                        dict(
                            name="activity_item_time_range_2",
                            question={"en": "What is your name?"},
                            response_type="time",
                            response_values=None,
                            config=dict(
                                additional_response_option={
                                    "text_input_option": False,
                                    "text_input_required": False,
                                },
                                remove_back_button=False,
                                skippable_item=False,
                                timer=1,
                            ),
                        ),
                        dict(
                            name="activity_item_geolocation",
                            question={"en": "What is your name?"},
                            response_type="geolocation",
                            response_values=None,
                            config=dict(
                                additional_response_option={
                                    "text_input_option": False,
                                    "text_input_required": False,
                                },
                                remove_back_button=False,
                                skippable_item=False,
                            ),
                        ),
                        dict(
                            name="activity_item_photo",
                            question={"en": "What is your name?"},
                            response_type="photo",
                            response_values=None,
                            config=dict(
                                additional_response_option={
                                    "text_input_option": False,
                                    "text_input_required": False,
                                },
                                remove_back_button=False,
                                skippable_item=False,
                            ),
                        ),
                        dict(
                            name="activity_item_video",
                            question={"en": "What is your name?"},
                            response_type="video",
                            response_values=None,
                            config=dict(
                                additional_response_option={
                                    "text_input_option": False,
                                    "text_input_required": False,
                                },
                                remove_back_button=False,
                                skippable_item=False,
                            ),
                        ),
                        dict(
                            name="activity_item_date",
                            question={"en": "What is your name?"},
                            response_type="date",
                            response_values=None,
                            config=dict(
                                additional_response_option={
                                    "text_input_option": False,
                                    "text_input_required": False,
                                },
                                remove_back_button=False,
                                skippable_item=False,
                            ),
                        ),
                        dict(
                            name="activity_item_drawing",
                            question={"en": "What is your name?"},
                            response_type="drawing",
                            response_values=dict(
                                drawing_background="https://www.w3schools.com/css/img_5terre_wide.jpg",  # noqa E501
                                drawing_example="https://www.w3schools.com/css/img_5terre_wide.jpg",  # noqa E501
                            ),
                            config=dict(
                                additional_response_option={
                                    "text_input_option": False,
                                    "text_input_required": False,
                                },
                                remove_back_button=False,
                                skippable_item=False,
                                timer=1,
                                remove_undo_button=False,
                                navigation_to_top=False,
                            ),
                        ),
                        dict(
                            name="activity_item_audio",
                            question={"en": "What is your name?"},
                            response_type="audio",
                            response_values=dict(max_duration=200),
                            config=dict(
                                additional_response_option={
                                    "text_input_option": False,
                                    "text_input_required": False,
                                },
                                remove_back_button=False,
                                skippable_item=False,
                                timer=1,
                            ),
                        ),
                        dict(
                            name="activity_item_audioplayer",
                            question={"en": "What is your name?"},
                            response_type="audioPlayer",
                            response_values=dict(
                                file="https://www.w3schools.com/html/horse.mp3",  # noqa E501
                            ),
                            config=dict(
                                remove_back_button=False,
                                skippable_item=False,
                                additional_response_option={
                                    "text_input_option": False,
                                    "text_input_required": False,
                                },
                                play_once=False,
                            ),
                        ),
                        dict(
                            name="activity_item_sliderrows",
                            question={"en": "What is your name?"},
                            response_type="sliderRows",
                            response_values=dict(
                                rows=[
                                    {
                                        "label": "label1",
                                        "min_label": "min_label1",
                                        "max_label": "max_label1",
                                        "min_value": 0,
                                        "max_value": 10,
                                        "min_image": None,
                                        "max_image": None,
                                        "score": None,
                                        "alerts": [
                                            dict(
                                                min_value=1,
                                                max_value=4,
                                                alert="alert1",
                                            ),
                                        ],
                                    }
                                ]
                            ),
                            config=dict(
                                remove_back_button=False,
                                skippable_item=False,
                                add_scores=False,
                                set_alerts=True,
                                timer=1,
                            ),
                        ),
                        dict(
                            name="activity_item_multiselectionrows",
                            question={"en": "What is your name?"},
                            response_type="multiSelectRows",
                            response_values=dict(
                                rows=[
                                    {
                                        "id": "17e69155-22cd-4484-8a49-364779ea9df1",  # noqa E501
                                        "row_name": "row1",
                                        "row_image": None,
                                        "tooltip": None,
                                    },
                                    {
                                        "id": "17e69155-22cd-4484-8a49-364779ea9df2",  # noqa E501
                                        "row_name": "row2",
                                        "row_image": None,
                                        "tooltip": None,
                                    },
                                ],
                                options=[
                                    {
                                        "id": "17e69155-22cd-4484-8a49-364779ea9de1",  # noqa E501
                                        "text": "option1",
                                        "image": None,
                                        "tooltip": None,
                                    },
                                    {
                                        "id": "17e69155-22cd-4484-8a49-364779ea9de2",  # noqa E501
                                        "text": "option2",
                                        "image": None,
                                        "tooltip": None,
                                    },
                                ],
                                data_matrix=[
                                    {
                                        "row_id": "17e69155-22cd-4484-8a49-364779ea9df1",  # noqa E501
                                        "options": [
                                            {
                                                "option_id": "17e69155-22cd-4484-8a49-364779ea9de1",  # noqa E501
                                                "score": 1,
                                                "alert": None,
                                            },
                                            {
                                                "option_id": "17e69155-22cd-4484-8a49-364779ea9de2",  # noqa E501
                                                "score": 2,
                                                "alert": None,
                                            },
                                        ],
                                    },
                                    {
                                        "row_id": "17e69155-22cd-4484-8a49-364779ea9df2",  # noqa E501
                                        "options": [
                                            {
                                                "option_id": "17e69155-22cd-4484-8a49-364779ea9de1",  # noqa E501
                                                "score": 3,
                                                "alert": None,
                                            },
                                            {
                                                "option_id": "17e69155-22cd-4484-8a49-364779ea9de2",  # noqa E501
                                                "score": 4,
                                                "alert": None,
                                            },
                                        ],
                                    },
                                ],
                            ),
                            config=dict(
                                remove_back_button=False,
                                skippable_item=False,
                                add_scores=False,
                                set_alerts=False,
                                timer=1,
                                add_tooltip=False,
                            ),
                        ),
                        dict(
                            name="activity_item_singleselectionrows",
                            question={"en": "What is your name?"},
                            response_type="singleSelectRows",
                            response_values=dict(
                                rows=[
                                    {
                                        "id": "17e69155-22cd-4484-8a49-364779ea9df1",  # noqa E501
                                        "row_name": "row1",
                                        "row_image": None,
                                        "tooltip": None,
                                    },
                                    {
                                        "id": "17e69155-22cd-4484-8a49-364779ea9df2",  # noqa E501
                                        "row_name": "row2",
                                        "row_image": None,
                                        "tooltip": None,
                                    },
                                ],
                                options=[
                                    {
                                        "id": "17e69155-22cd-4484-8a49-364779ea9de1",  # noqa E501
                                        "text": "option1",
                                        "image": None,
                                        "tooltip": None,
                                    },
                                    {
                                        "id": "17e69155-22cd-4484-8a49-364779ea9de2",  # noqa E501
                                        "text": "option2",
                                        "image": None,
                                        "tooltip": None,
                                    },
                                ],
                                data_matrix=[
                                    {
                                        "row_id": "17e69155-22cd-4484-8a49-364779ea9df1",  # noqa E501
                                        "options": [
                                            {
                                                "option_id": "17e69155-22cd-4484-8a49-364779ea9de1",  # noqa E501
                                                "score": 1,
                                                "alert": "alert1",
                                            },
                                            {
                                                "option_id": "17e69155-22cd-4484-8a49-364779ea9de2",  # noqa E501
                                                "score": 2,
                                                "alert": None,
                                            },
                                        ],
                                    },
                                    {
                                        "row_id": "17e69155-22cd-4484-8a49-364779ea9df2",  # noqa E501
                                        "options": [
                                            {
                                                "option_id": "17e69155-22cd-4484-8a49-364779ea9de1",  # noqa E501
                                                "score": 3,
                                                "alert": None,
                                            },
                                            {
                                                "option_id": "17e69155-22cd-4484-8a49-364779ea9de2",  # noqa E501
                                                "score": 4,
                                                "alert": None,
                                            },
                                        ],
                                    },
                                ],
                            ),
                            config=dict(
                                remove_back_button=False,
                                skippable_item=False,
                                add_scores=False,
                                set_alerts=True,
                                timer=1,
                                add_tooltip=False,
                            ),
                        ),
                        dict(
                            name="activity_item_singleselect",
                            question={"en": "What is your name?"},
                            response_type="singleSelect",
                            response_values=dict(
                                palette_name="palette1",
                                options=[
                                    {
                                        "text": "option1",
                                        "value": 1,
                                        "alert": "alert1",
                                    },
                                    {
                                        "text": "option2",
                                        "value": 2,
                                        "alert": "alert2",
                                    },
                                ],
                            ),
                            config=dict(
                                remove_back_button=False,
                                skippable_item=False,
                                add_scores=False,
                                set_alerts=True,
                                timer=1,
                                add_tooltip=False,
                                set_palette=False,
                                randomize_options=False,
                                additional_response_option={
                                    "text_input_option": False,
                                    "text_input_required": False,
                                },
                            ),
                        ),
                        dict(
                            name="activity_item_multiselect",
                            question={"en": "What is your name?"},
                            response_type="multiSelect",
                            response_values=dict(
                                palette_name="palette1",
                                options=[
                                    {"text": "option1"},
                                    {"text": "option2"},
                                ],
                            ),
                            config=dict(
                                remove_back_button=False,
                                skippable_item=False,
                                add_scores=False,
                                set_alerts=False,
                                timer=1,
                                add_tooltip=False,
                                set_palette=False,
                                randomize_options=False,
                                additional_response_option={
                                    "text_input_option": False,
                                    "text_input_required": False,
                                },
                            ),
                        ),
                        dict(
                            name="activity_item_slideritem",
                            question={"en": "What is your name?"},
                            response_type="slider",
                            response_values=dict(
                                min_value=0,
                                max_value=10,
                                min_label="min_label",
                                max_label="max_label",
                                min_image=None,
                                max_image=None,
                                scores=None,
                                alerts=[
                                    dict(
                                        min_value=1,
                                        max_value=4,
                                        alert="alert1",
                                    ),
                                ],
                            ),
                            config=dict(
                                remove_back_button=False,
                                skippable_item=False,
                                add_scores=False,
                                set_alerts=True,
                                timer=1,
                                show_tick_labels=False,
                                show_tick_marks=False,
                                continuous_slider=True,
                                additional_response_option={
                                    "text_input_option": False,
                                    "text_input_required": False,
                                },
                            ),
                        ),
                        dict(
                            name="activity_item_slideritem_another",
                            question={"en": "What is your name?"},
                            response_type="slider",
                            response_values=dict(
                                min_value=0,
                                max_value=10,
                                min_label="min_label",
                                max_label="max_label",
                                min_image=None,
                                max_image=None,
                                scores=None,
                                alerts=[
                                    dict(
                                        value="1",
                                        alert="alert1",
                                    ),
                                ],
                            ),
                            config=dict(
                                remove_back_button=False,
                                skippable_item=False,
                                add_scores=False,
                                set_alerts=True,
                                timer=1,
                                show_tick_labels=False,
                                show_tick_marks=False,
                                continuous_slider=False,
                                additional_response_option={
                                    "text_input_option": False,
                                    "text_input_required": False,
                                },
                            ),
                        ),
                        dict(
                            name="activity_item_flanker",
                            question=dict(
                                en="flanker question?",
                                fr="flanker question?",
                            ),
                            response_type="flanker",
                            response_values=None,
                            config=dict(
                                general=dict(
                                    instruction="instruction",
                                    buttons=[
                                        dict(
                                            name="button 1",
                                            image="image button 1",
                                        ),
                                        dict(
                                            name="button 2",
                                            image="image button 2",
                                        ),
                                    ],
                                    fixation=dict(
                                        image="image fixation",
                                        duration=10,
                                    ),
                                    stimulusTrials=[
                                        {
                                            "id": "1",
                                            "image": "image stimulus_trials 1",
                                            "correctPress": "left",
                                        },
                                        {
                                            "id": "2",
                                            "image": "image stimulus_trials 2",
                                            "correctPress": "left",
                                        },
                                    ],
                                ),
                                practice=dict(
                                    instruction="instruction",
                                    blocks=[
                                        {
                                            "order": ["1", "2"],
                                            "name": "name order 1",
                                        },
                                        {
                                            "order": ["2", "1"],
                                            "name": "name order 2",
                                        },
                                    ],
                                    stimulusDuration=20,
                                    threshold=15,
                                    randomizeOrder=True,
                                    showFeedback=True,
                                    showSummary=True,
                                ),
                                test=dict(
                                    instruction="instruction",
                                    blocks=[
                                        {
                                            "order": ["1", "2"],
                                            "name": "name order 1",
                                        },
                                        {
                                            "order": ["2", "1"],
                                            "name": "name order 2",
                                        },
                                    ],
                                    stimulusDuration=20,
                                    randomizeOrder=True,
                                    showFeedback=True,
                                    showSummary=True,
                                ),
                            ),
                        ),
                        dict(
                            name="activity_item_gyroscope",
                            question=dict(
                                en="gyroscope question?",
                                fr="gyroscope question?",
                            ),
                            response_type="gyroscope",
                            response_values=None,
                            config=dict(
                                name="name",
                                description="description",
                                isHidden=False,
                                general={
                                    "instruction": "gyroscope instruction",
                                    "number_of_trials": 3,
                                    "length_of_test": 3,
                                    "lambda_slope": 3,
                                },
                                practice={
                                    "instruction": "gyroscope practice "
                                    "instruction",
                                },
                                test={
                                    "instruction": "gyroscope test "
                                    "instruction",
                                },
                            ),
                        ),
                        dict(
                            name="activity_item_touch",
                            question=dict(
                                en="touch question?",
                                fr="touch question?",
                            ),
                            response_type="touch",
                            response_values=None,
                            config=dict(
                                name="name",
                                description="description",
                                isHidden=False,
                                general={
                                    "instruction": "touch instruction",
                                    "number_of_trials": 3,
                                    "length_of_test": 3,
                                    "lambda_slope": 3,
                                },
                                practice={
                                    "instruction": "touch practice "
                                    "instruction",
                                },
                                test={
                                    "instruction": "touch test instruction",
                                },
                            ),
                        ),
                        dict(
                            name="activity_item_ab_trails_ipad",
                            question=dict(
                                en="ab_trails_ipad question?",
                                fr="ab_trails_ipad question?",
                            ),
                            response_type="ABTrailsIpad",
                            response_values=None,
                            config=dict(
                                name="name",
                                description="description",
                                isHidden=False,
                                imagePlaceholder="image placeholder",
                            ),
                        ),
                        dict(
                            name="activity_item_ab_trails_mobile",
                            question=dict(
                                en="ab_trails_mobile question?",
                                fr="ab_trails_mobile question?",
                            ),
                            response_type="ABTrailsMobile",
                            response_values=None,
                            config=dict(
                                name="name",
                                description="description",
                                isHidden=False,
                                imagePlaceholder="image placeholder",
                            ),
                        ),
                    ],
                ),
            ],
            activity_flows=[
                dict(
                    name="Morning questionnaire",
                    description=dict(
                        en="Understand how was the morning",
                        fr="Understand how was the morning",
                    ),
                    items=[
                        dict(
                            activity_key="577dbbda-3afc-"
                            "4962-842b-8d8d11588bfe"
                        )
                    ],
                )
            ],
        )
        response = await self.client.post(
            self.applet_create_url.format(
                owner_id="7484f34a-3acc-4ee6-8a94-fd7299502fa1"
            ),
            data=create_data,
        )
        assert response.status_code == 201, response.json()

        response = await self.client.get(
            self.applet_detail_url.format(pk=response.json()["result"]["id"])
        )
        assert response.status_code == 200

    @rollback
    async def test_creating_applet_with_activity_items_condition(self):
        await self.client.login(
            self.login_url, "tom@mindlogger.com", "Test1234!"
        )
        create_data = dict(
            display_name="User daily behave",
            encryption=dict(
                public_key=uuid.uuid4().hex,
                prime=uuid.uuid4().hex,
                base=uuid.uuid4().hex,
                account_id=str(uuid.uuid4()),
            ),
            description=dict(
                en="Understand users behave",
                fr="Comprendre le comportement des utilisateurs",
            ),
            about=dict(
                en="Understand users behave",
                fr="Comprendre le comportement des utilisateurs",
            ),
            activities=[
                # Activity with conditional logic
                dict(
                    name="Morning activity with conditional logic",
                    key="577dbbdd-3afc-4962-842b-8d8d11588bfe",
                    description=dict(
                        en="Understand morning feelings.",
                        fr="Understand morning feelings.",
                    ),
                    subscale_setting=dict(
                        calculate_total_score="sum",
                        total_scores_table_data=[
                            dict(
                                raw_score="1",
                                optional_text="optional_text",
                            ),
                            dict(
                                raw_score="2",
                                optional_text="optional_text2",
                            ),
                        ],
                        subscales=[
                            dict(
                                name="subscale1",
                                scoring="sum",
                                items=[
                                    "activity_item_singleselect",
                                ],
                                subscale_table_data=[
                                    dict(
                                        score="1.2342~1231",
                                        raw_score="1",
                                        age=15,
                                        sex="F",
                                        optional_text="optional_text",
                                    ),
                                    dict(
                                        score="1.2342~1231.12333",
                                        raw_score="1~6",
                                        age=10,
                                        sex="M",
                                        optional_text="optional_text12",
                                    ),
                                    dict(
                                        score=1,
                                        raw_score=1,
                                        age=15,
                                        sex="M",
                                        optional_text="optional_text13",
                                    ),
                                ],
                            ),
                        ],
                    ),
                    scores_and_reports=dict(
                        generateReport=True,
                        showScoreSummary=True,
                        scores=[
                            dict(
                                name="score1",
                                id="score1_activity1",
                                calculationType="sum",
                                minScore=0,
                                maxScore=3,
                                itemsScore=["activity_item_singleselect"],
                                showMessage=True,
                                message="Hello",
                                printItems=True,
                                itemsPrint=[
                                    "activity_item_singleselect",
                                    "activity_item_multiselect",
                                    "activity_item_slideritem",
                                    "activity_item_text",
                                ],
                                conditionalLogic=[
                                    dict(
                                        name="score1_condition1",
                                        id="score1_condition1_id",
                                        flagScore=True,
                                        showMessage=True,
                                        message="Hello2",
                                        printItems=False,
                                        match="any",
                                        conditions=[
                                            dict(
                                                item_name="score1",
                                                type="GREATER_THAN",
                                                payload=dict(
                                                    value=1,
                                                ),
                                            ),
                                            dict(
                                                item_name="score1",
                                                type="GREATER_THAN",
                                                payload=dict(
                                                    value=2,
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                        ],
                        sections=[
                            dict(
                                name="section1",
                                showMessages=True,
                                messages="Hello from the other side",
                                printItems=True,
                                itemsPrint=[
                                    "activity_item_singleselect",
                                    "activity_item_multiselect",
                                    "activity_item_slideritem",
                                    "activity_item_text",
                                ],
                                conditionalLogic=dict(
                                    name="section1_condition1",
                                    id="section1_condition1_id",
                                    message="Hello2",
                                    showMessage=True,
                                    printItems=False,
                                    match="all",
                                    conditions=[
                                        dict(
                                            item_name="score1",
                                            type="GREATER_THAN",
                                            payload=dict(
                                                value=1,
                                            ),
                                        ),
                                        dict(
                                            item_name="activity_item_singleselect",  # noqa E501
                                            type="EQUAL_TO_OPTION",
                                            payload=dict(
                                                option_id="25e69155-22cd-4484-8a49-364779ea9de1"  # noqa E501
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                        ],
                    ),
                    items=[
                        dict(
                            name="activity_item_singleselect",
                            question={"en": "What is your name?"},
                            response_type="singleSelect",
                            response_values=dict(
                                palette_name="palette1",
                                options=[
                                    {
                                        "text": "option1",
                                        "score": 1,
                                        "id": "25e69155-22cd-4484-8a49-364779ea9de1",  # noqa E501
                                    },
                                    {
                                        "text": "option2",
                                        "score": 2,
                                        "id": "26e69155-22cd-4484-8a49-364779ea9de1",  # noqa E501
                                    },
                                ],
                            ),
                            config=dict(
                                remove_back_button=False,
                                skippable_item=False,
                                add_scores=True,
                                set_alerts=False,
                                timer=1,
                                add_tooltip=False,
                                set_palette=False,
                                randomize_options=False,
                                additional_response_option={
                                    "text_input_option": False,
                                    "text_input_required": False,
                                },
                            ),
                        ),
                        dict(
                            name="activity_item_multiselect",
                            question={"en": "What is your name?"},
                            response_type="multiSelect",
                            response_values=dict(
                                palette_name="palette1",
                                options=[
                                    {
                                        "text": "option1",
                                        "id": "27e69155-22cd-4484-8a49-364779ea9de1",  # noqa E501
                                    },
                                    {
                                        "text": "option2",
                                        "id": "28e69155-22cd-4484-8a49-364779ea9de1",  # noqa E501
                                    },
                                ],
                            ),
                            config=dict(
                                remove_back_button=False,
                                skippable_item=False,
                                add_scores=False,
                                set_alerts=False,
                                timer=1,
                                add_tooltip=False,
                                set_palette=False,
                                randomize_options=False,
                                additional_response_option={
                                    "text_input_option": False,
                                    "text_input_required": False,
                                },
                            ),
                        ),
                        dict(
                            name="activity_item_slideritem",
                            question={"en": "What is your name?"},
                            response_type="slider",
                            response_values=dict(
                                min_value=0,
                                max_value=10,
                                min_label="min_label",
                                max_label="max_label",
                                min_image=None,
                                max_image=None,
                                scores=None,
                            ),
                            config=dict(
                                remove_back_button=False,
                                skippable_item=False,
                                add_scores=False,
                                set_alerts=False,
                                timer=1,
                                show_tick_labels=False,
                                show_tick_marks=False,
                                continuous_slider=False,
                                additional_response_option={
                                    "text_input_option": False,
                                    "text_input_required": False,
                                },
                            ),
                        ),
                        dict(
                            name="activity_item_text",
                            question=dict(
                                en="How had you slept?",
                                fr="How had you slept?",
                            ),
                            response_type="text",
                            response_values=None,
                            config=dict(
                                max_response_length=200,
                                correct_answer_required=False,
                                correct_answer=None,
                                numerical_response_required=False,
                                response_data_identifier=False,
                                response_required=False,
                                remove_back_button=False,
                                skippable_item=True,
                            ),
                            conditional_logic=dict(
                                match="any",
                                conditions=[
                                    dict(
                                        item_name="activity_item_singleselect",
                                        type="EQUAL_TO_OPTION",
                                        payload=dict(
                                            option_id="25e69155-22cd-4484-8a49-364779ea9de1"  # noqa E501
                                        ),
                                    ),
                                    dict(
                                        item_name="activity_item_multiselect",
                                        type="INCLUDES_OPTION",
                                        payload=dict(
                                            option_id="27e69155-22cd-4484-8a49-364779ea9de1"  # noqa E501
                                        ),
                                    ),
                                    dict(
                                        item_name="activity_item_slideritem",
                                        type="GREATER_THAN",
                                        payload=dict(
                                            value=5,
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        dict(
                            name="activity_item_time_range_2",
                            question={"en": "What is your name?"},
                            response_type="time",
                            response_values=None,
                            config=dict(
                                additional_response_option={
                                    "text_input_option": False,
                                    "text_input_required": False,
                                },
                                remove_back_button=False,
                                skippable_item=False,
                                timer=1,
                            ),
                            conditional_logic=dict(
                                match="all",
                                conditions=[
                                    dict(
                                        item_name="activity_item_singleselect",
                                        type="EQUAL_TO_OPTION",
                                        payload=dict(
                                            option_id="25e69155-22cd-4484-8a49-364779ea9de1"  # noqa E501
                                        ),
                                    ),
                                    dict(
                                        item_name="activity_item_multiselect",
                                        type="INCLUDES_OPTION",
                                        payload=dict(
                                            option_id="27e69155-22cd-4484-8a49-364779ea9de1"  # noqa E501
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        dict(
                            name="activity_item_audio",
                            question={"en": "What is your name?"},
                            response_type="audio",
                            response_values=dict(max_duration=200),
                            config=dict(
                                additional_response_option={
                                    "text_input_option": False,
                                    "text_input_required": False,
                                },
                                remove_back_button=False,
                                skippable_item=False,
                                timer=1,
                            ),
                        ),
                    ],
                ),
            ],
            activity_flows=[
                dict(
                    name="Morning questionnaire",
                    description=dict(
                        en="Understand how was the morning",
                        fr="Understand how was the morning",
                    ),
                    items=[
                        dict(
                            activity_key="577dbbdd-3afc-4962-842b-8d8d11588bfe"  # noqa E501
                        )
                    ],
                )
            ],
        )
        response = await self.client.post(
            self.applet_create_url.format(
                owner_id="7484f34a-3acc-4ee6-8a94-fd7299502fa1"
            ),
            data=create_data,
        )
        assert response.status_code == 201, response.json()
        assert (
            type(
                response.json()["result"]["activities"][0]["items"][3][
                    "conditionalLogic"
                ]
            )
            == dict
        )
        assert (
            type(
                response.json()["result"]["activities"][0]["scoresAndReports"]
            )
            == dict
        )
        assert (
            type(response.json()["result"]["activities"][0]["subscaleSetting"])
            == dict
        )
        response = await self.client.get(
            self.applet_detail_url.format(pk=response.json()["result"]["id"])
        )
        assert response.status_code == 200

        activity_id = response.json()["result"]["activities"][0]["id"]
        response = await self.client.get(
            self.activity_detail_url.format(activity_id=activity_id)
        )
        assert response.status_code == 200
        assert (
            type(response.json()["result"]["items"][3]["conditionalLogic"])
            == dict
        )
