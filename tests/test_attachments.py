import json

import allure
from allure import attachment_type


def test_attachments():
    allure.attach("Text content", name="Content from text", attachment_type=attachment_type.TEXT)
    allure.attach("<h1>Hello World</h1>", name="HTML", attachment_type=attachment_type.HTML)
    allure.attach(json.dumps({"first": 1, "second": 2}), name='json', attachment_type=attachment_type.JSON)