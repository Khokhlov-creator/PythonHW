class Node:
    def __init__(self, nextNode, prevNode, data):
        self.data = data
        self.nextNode = nextNode
        self.prevNode = prevNode


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, node):
        if self.head:
            self.head.prevNode = node

        node.nextNode = self.head
        self.head = node
        node.prevNode = None

    def insertAfter(self, newNode, node):
        if node.nextNode:
            node.nextNode.prevNode = newNode

        newNode.nextNode = node.nextNode
        node.nextNode = newNode
        newNode.prevNode = node


class Car:
    def __init__(self, identification, name, brand, price, active):
        self.identification = identification
        self.name = name
        self.brand = brand
        self.price = price
        self.active = active


db = LinkedList()


def init(cars):
    db.head = Node(None, None, cars[0])
    for j in range(1, len(cars)):
        add(cars[j])


def add(car):
    newNode = Node(None, None, car)
    curr_node = db.head
    while curr_node and curr_node.nextNode:
        if car.price >= curr_node.nextNode.data.price:
            curr_node = curr_node.nextNode
        else:
            break

    if curr_node and car.price >= curr_node.data.price:
        db.insertAfter(newNode, curr_node)
    else:
        db.insert(newNode)


def updateName(identification, name):
    curr_node = db.head
    ptr = False
    while curr_node:
        if curr_node.data.identification == identification:
            curr_node.data.name = name
            ptr = True
            break
        curr_node = curr_node.nextNode

    if ptr:
        pass
    else:
        return None


def updateBrand(identification, brand):
    curr_node = db.head
    ptr = False
    while curr_node:
        if curr_node.data.identification == identification:
            curr_node.data.brand = brand
            ptr = True
            break
        curr_node = curr_node.nextNode

    if ptr:
        pass
    else:
        return None


def activateCar(identification):
    curr_node = db.head
    ptr = False
    while curr_node:
        if curr_node.data.identification == identification:
            curr_node.data.active = True
            ptr = True
            break
        curr_node = curr_node.nextNode

    if ptr:
        pass
    else:
        return None


def deactivateCar(identification):
    curr_node = db.head
    ptr = False
    while curr_node:
        if curr_node.data.identification == identification:
            curr_node.data.active = False
            ptr = True
            break
        curr_node = curr_node.nextNode

    if ptr:
        pass
    else:
        return None


def getDatabaseHead():
    return db.head


def getDatabase():
    return db


def calculateCarPrice():
    cost = 0
    curr_node = db.head
    while curr_node:
        if curr_node.data.active is True:
            cost += curr_node.data.price
        curr_node = curr_node.nextNode

    return cost


def clean():
    while db.head is not None:
        tmp = db.head
        del db.head.data
        db.head = db.head.nextNode
        tmp = None
