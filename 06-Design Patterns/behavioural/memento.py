class Editor:
    def __init__(self):
        self.text = ""

    def write(self, text):
        self.text += text

    def create_memento(self):
        return EditorMemento(self.text)

    def restore_memento(self, memento):
        self.text = memento.get_saved_text()

    def __str__(self):
        return self.text


class EditorMemento:
    def __init__(self, text):
        self.saved_text = text

    def get_saved_text(self):
        return self.saved_text