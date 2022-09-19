class stringRearrange:
    def __init__(self, string):
        self.string = string
        self.result = ""
        self.answer = ""

    def stringRearrange(self):
        for i in self.string:
            if ord(i) >= 97 and ord(i) < 123:
                self.result = self.result + i
            else:
                self.result = self.result + '.'

        self.result = self.result.split('.')
        self.result = self.result[1:-1]
        for i in range(len(self.result)-1,-1,-1):
            self.answer = self.answer + self.result[i]
        print(self.answer)


if __name__ == "__main__":
    string = "/u/love\i\\"
    obj = stringRearrange(string)
    obj.stringRearrange()
