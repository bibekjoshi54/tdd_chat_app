from typing import Protocol


class ICommunicationRepo(Protocol):
    def broadcast(
        self, sender_username: str, receiver_username: str, message: str
    ): ...

    def get_raw_messages(self) -> list: ...
