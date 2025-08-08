class ConsentGate:
    def __init__(self, authorized=True):
        self.authorized = authorized

    def check(self):
        return self.authorized

    def require(self):
        if not self.check():
            raise PermissionError("Consent gate blocked this action.")


class Node:
    def __init__(self, name, gate=None):
        self.name = name
        self.gate = gate or ConsentGate()

    def execute(self, operation):
        if self.gate.require():
            return f"Node {self.name} executed: {operation}"
