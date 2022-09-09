
class Checkversion:
    def __init__(self, version1, version2):
        self.version1 = version1
        self.version2 = version2

    def compare(self):
        v1 = self.version1.split('.')
        v2 = self.version2.split('.')
        for i in range(0, len(v1)):
            if int(v1[i]) > int(v2[i]):
                print("Version 1 is greater than Version 2")
                break
            elif int(v1[i]) < int(v2[i]):
                print("Version 2 is greater than Version 1")
                break
            else:
                print("Version 1 is equal to Version 2")
                break


if __name__ == '__main__':
    v1 =  "1.001.2"
    v2 = "1.1.2"
    check = Checkversion(v1, v2)
    check.compare()