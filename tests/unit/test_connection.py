from tdd_chat_app.repo_impl import ConnectionProperties, ProcessConnectionRepo
from pytest_mock import MockerFixture


class FakeServer:
    def __init__(self):
        self.last_command = None
        self.last_args = None
        self.messages = []

    def __call__(self, *args, **kwargs):
        return self

    def send(self, data):
        callid, command, args, kwargs = data
        self.last_command = command
        self.last_args = args

    def close(self):
        pass

    def recv(self, *args, **kwargs):
        if self.last_command == "dummy":
            return "#RETURN", None
        elif self.last_command == "create":
            return "#RETURN", ("fakeid", tuple())
        elif self.last_command == "__getitem__":
            return "#RETURN", self.messages[self.last_args[0]]
        elif self.last_command in ("incref", "decref", "accept_connection"):
            return "#RETURN", None
        elif self.last_command == "__len__":
            return "#RETURN", len(self.messages)
        elif self.last_command == "append":
            self.messages.append(self.last_args[0])
            return "#RETURN", None
        return "#ERROR", ValueError(f"{self.last_command} - {self.last_args}")


class TestConnectionRepo:
    def test_connection_properties(self):
        connection_properties = ConnectionProperties(url=("localhost", 9090))
        assert connection_properties.url == ("localhost", 9090)

    def test_broadcast(self, mocker: MockerFixture):
        connection_properties = ConnectionProperties(url=("localhost", 9090))
        sender_username = "foo"
        receiver_username = "bar"
        message = "HELLO"
        with mocker.patch.object(ProcessConnectionRepo, "connect"):
            connection_repo = ProcessConnectionRepo(
                connection_properties=connection_properties
            )

        with mocker.patch.object(
            target=connection_repo, attribute="get_raw_messages", return_value=[]
        ):
            connection_repo.broadcast(
                sender_username=sender_username,
                receiver_username=receiver_username,
                message=message,
            )
            receiver_message = connection_repo.get_raw_messages()
            assert receiver_message[-1] == {
                "sender_username": sender_username,
                "receiver_username": receiver_username,
                "message": message,
            }

    def test_with_fake_server(self, mocker: MockerFixture):
        mocker.patch(
            target="multiprocessing.managers.listener_client",
            new={"pickle": (None, FakeServer())},
        )
        connection_properties = ConnectionProperties(url=("localhost", 9090))
        c1 = ProcessConnectionRepo(connection_properties=connection_properties)
        c2 = ProcessConnectionRepo(connection_properties=connection_properties)
        c1.broadcast(
            sender_username="FOO", receiver_username="BAR", message="HELLO"
        )
        assert c2.get_raw_messages()[-1] == {
            "sender_username": "FOO",
            "receiver_username": "BAR",
            "message": "HELLO",
        }
