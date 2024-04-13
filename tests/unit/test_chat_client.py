from tdd_chat_app.chat_client import ChatClient
from pytest_mock import MockerFixture

from tdd_chat_app.irepo import ICommunicationRepo


class TestChatClientUnit:
    def test_chat_client(self, mocker: MockerFixture):
        communication_repo = mocker.Mock(ICommunicationRepo)
        client = ChatClient(
            user_name="Bibek", communication_repo=communication_repo
        )

        assert client.user_name == "Bibek"

    def test_chat_send_message(self, mocker: MockerFixture):
        communication_repo = mocker.Mock(ICommunicationRepo)
        broadcast_spy = mocker.spy(obj=communication_repo, name="broadcast")

        sender, receiver, message = "FOO", "BAR", "HELLO"

        sender_client = ChatClient(
            user_name=sender, communication_repo=communication_repo
        )
        sender_client.send_message(receiver_username=receiver, message=message)
        broadcast_spy.assert_called_once_with(
            sender_username=sender, receiver_username=receiver, message=message
        )

    def test_fetch_message(self, mocker: MockerFixture):
        communication_repo = mocker.Mock(spec=ICommunicationRepo)
        communication_messages = [
            {
                "sender_username": "FOO",
                "receiver_username": "BAR",
                "message": "MSG_1",
            },
            {
                "sender_username": "FOO",
                "receiver_username": "BAR",
                "message": "MSG_2",
            },
            {
                "sender_username": "FOO",
                "receiver_username": "BAR",
                "message": "MSG_3",
            },
            {
                "sender_username": "BAR",
                "receiver_username": "FOO",
                "message": "MSG_4",
            },
        ]
        mck = mocker.patch.object(
            target=communication_repo,
            attribute="get_raw_messages",
            return_value=communication_messages,
        )
        foo_client = ChatClient(
            user_name="BAR", communication_repo=communication_repo
        )
        message = foo_client.fetch_messages()
        assert message == communication_messages[:3]
        mck.assert_called_once()
