class Editor:
    def __init__(self):
        self.text = ""

    def set_text(self, text):
        self.text = text

    def create_snapshot(self):
        return Snapshot(self, self.text)

    def restore(self, snapshot):
        self.text = snapshot.text


class Snapshot:
    def __init__(self, editor, text):
        self.editor = editor
        self.text = text


if __name__ == "__main__":
    editor = Editor()
    editor.set_text("Versão 1")
    print(f"Texto atual: {editor.text}")

    snapshot = editor.create_snapshot()#salvar texto

    editor.set_text("Versão 2") #modifica texto
    print(f"Texto alterado: {editor.text}") 

    editor.restore(snapshot) #restaura texto
    print(f"Texto restaurado: {editor.text}")
