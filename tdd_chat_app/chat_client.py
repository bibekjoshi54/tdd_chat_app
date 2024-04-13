from tdd_chat_app.irepo import ICommunicationRepo


class ChatClient:
    def __init__(self, user_name: str, communication_repo: ICommunicationRepo):
        self.user_name = user_name
        self.communication_repo = communication_repo

    def send_message(self, receiver_username: str, message: str):
        self.communication_repo.broadcast(
            sender_username=self.user_name,
            receiver_username=receiver_username,
            message=message,
        )
        return {"receiver_username": receiver_username, "message": message}

    def fetch_messages(self):
        all_messages = self.communication_repo.get_raw_messages()
        return list(
            filter(
                lambda msg: msg["receiver_username"] == self.user_name,
                all_messages,
            )
        )
