from multiprocessing.managers import SyncManager, ListProxy


class ConnectionProperties:
    def __init__(self, url: tuple[str, int]):
        self.url = url


class ProcessConnectionRepo(SyncManager):
    def __init__(self, connection_properties: ConnectionProperties):
        self.connection_properties = connection_properties
        self.register("get_messages", proxytype=ListProxy)
        super().__init__(address=("localhost", 9090))
        self.connect()

    def broadcast(
        self, sender_username: str, receiver_username: str, message: str
    ):
        msg_q = self.get_raw_messages()
        msg_q.append(
            {
                "sender_username": sender_username,
                "receiver_username": receiver_username,
                "message": message,
            }
        )

    def get_raw_messages(self) -> list:
        return self.get_messages()
