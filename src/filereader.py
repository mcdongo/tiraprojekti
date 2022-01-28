class Reader:
    def __init__(self, path):
        self.path = path

    def read(self):
        try:
            with open(self.path, "r") as file:
                return file.read().splitlines()
        except Exception:
            raise SystemExit("Invalid filename or path")

    def parse_data(self):
        self.data = self.read()
        self.data.pop(0)
        height = int(self.data.pop(0).split(" ")[1]) + 50
        width = int(self.data.pop(0).split(" ")[1]) * 2
        self.data.pop(0)
        temp = []
        for y in range(len(self.data)):
            temp.append(list(self.data[y]))
        self.data = temp

        return height,width,self.data