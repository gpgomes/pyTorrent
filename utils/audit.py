class Audit(object):
    def __init__(self, class_name: str):
        self.class_name = class_name

    def info(self, msg: str):
        print(f"Info [{self.class_name}]: {msg}")

    def warning(self, msg: str):
        print(f"Warning [{self.class_name}]: {msg}")

    def error(self, msg: str):
        print(f"Error [{self.class_name}]: {msg}")

    def input(self, msg: str):
        print(f"Input [{self.class_name}]: {msg}")
