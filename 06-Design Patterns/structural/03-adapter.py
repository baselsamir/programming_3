class EuropeanSocket:
    def voltage(self):
        return 220

    def plug(self):
        return "European socket plugged"


class USASocket:
    def voltage(self):
        return 110

    def plug(self):
        return "USA socket plugged"


class EuropeanToUSASocketAdapter:
    def __init__(self, socket):
        self.socket = socket

    def voltage(self):
        return self.socket.voltage() / 2

    def plug(self):
        return self.socket.plug() + " (Adapter used)"


# Client code
european_socket = EuropeanSocket()
print(f"European socket: Voltage = {european_socket.voltage()}, Plug: {european_socket.plug()}")

usa_socket = USASocket()
print(f"USA socket: Voltage = {usa_socket.voltage()}, Plug: {usa_socket.plug()}")

adapter = EuropeanToUSASocketAdapter(european_socket)
print(f"Adapter: Voltage = {adapter.voltage()}, Plug: {adapter.plug()}")