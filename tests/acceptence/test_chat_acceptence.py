import pytest

class TestChatAcceptance:


    def test_message_exchange(self):
        user_1 = ChatClient("Bibek")
        user_2 = ChatClient("Abhai")
        user_1.send_message(user=user_2, message="Hello")
        message = user_2.fetch_message()

        assert message == [{"user": "Bibek", "message": "Hello"}]

