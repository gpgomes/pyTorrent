class Audit(object):
    def __init__(self, class_name: str):
        self.class_name = class_name

    def message(self, level: str, msg: str):
        print(f"[{level}] [{self.class_name}]: {msg}")

    def info(self, msg: str):
        self.message(level="Info", msg=msg)

    def warning(self, msg: str):
        self.message(level="Warning", msg=msg)

    def error(self, msg: str):
        self.message(level="Error", msg=msg)

    def input(self, msg: str):
        self.message(level="Input", msg=msg)
