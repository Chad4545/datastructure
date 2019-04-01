class Node:
    value = ''
    nextnode = ''
    binhead = False
    bintail = False

    def __init__(self, value='', nextnode='', binhead=False, bintail=False):
        self.value = value
        self.nextnode = nextnode
        self.binhead = binhead
        self.bintail = bintail

    def getValue(self):
        return self.value

    def setValue(self, value=''):
        self.value = value

    def getNext(self):
        return self.nextnode

    def setNext(self, nextnode=''):
        self.nextnode = nextnode

    def isTail(self):
        return self.bintail

    def isHead(self):
        return self.binhead

    