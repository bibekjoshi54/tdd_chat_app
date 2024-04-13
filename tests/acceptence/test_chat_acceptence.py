from tdd_chat_app.chat_client import ChatClient
from tdd_chat_app.communication_server import new_chat_server
from tdd_chat_app.repo_impl import ConnectionProperties, ProcessConnectionRepo
from pytest_mock import MockerFixture


class TestChatAcceptance:
    def test_message_exchange(self, mocker: MockerFixture):
        with new_chat_server() as _:
            connection = ProcessConnectionRepo(
                connection_properties=ConnectionProperties(
                    url=("localhost", 9090)
                )
            )
            user_1 = ChatClient("FOO", communication_repo=connection)
            user_2 = ChatClient("BAR", communication_repo=connection)
            user_1.send_message(receiver_username="BAR", message="Hello")
            message = user_2.fetch_messages()
            expected_response = [
                {
                    "sender_username": "FOO",
                    "receiver_username": "BAR",
                    "message": "Hello",
                }
            ]
            assert expected_response == message
