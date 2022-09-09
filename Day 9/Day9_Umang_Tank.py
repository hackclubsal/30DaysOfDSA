"""
A version number consists of one or more revisions connected by a dot.
Each revisions consists of digits and may contain leading zeroes. Each revision consists atleast one digit.

Revisions are 0-indexed from left to right.
To compare two versions, compare revisions in the left-to-right order. Revisions are compared using their integer value ignoring any leading zeroes.


Example 1:
- version 1: 1.1.0
- version 2: 1.2.0

Output:
- version 2 > version 1.

Example 2:
- version 1: 1.001.2
- version 2: 1.1.2

Output:
- version 2 = version 1.
"""


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
    v1 = "1.001.2"
    v2 = "1.1.2"
    check = Checkversion(v1, v2)
    check.compare()
