class node():
    """Represents a seat"""
    def __init__(self, val=None, parent=None, children=None):
        self.val = val
        self.parent = parent
        self.children = []
        self.history = [val]  # people seated


def Diff(li1, li2):
    """
    >>> Diff([1,2,3,4],[2,4])
    [1,3]
    """
    return (list(list(set(li1) - set(li2)) + list(set(li2) - set(li1))))


def next_person(currNode, n):
    """If currNode is a seat at level 2, grows its level 3 seat arrangement."""
    nextPerson = len(currNode.history)
    if nextPerson > n:
        if currNode.val == n:
            global count
            count += 1
        global ctr
        ctr += 1  # denominator
        return
    if nextPerson in currNode.history:
        # next person's assigned seat is already taken
        availableSeat = Diff(currNode.history, [i for i in range(1, n + 1)])
        availableSeat.remove('root')
        for seat in availableSeat:
            newNode = node(seat)
            newNode.history = currNode.history + newNode.history
            currNode.children.append(newNode)
    else:
        # assigned seat is not yet taken
        newNode = node(nextPerson)
        newNode.history = currNode.history + newNode.history
        currNode.children.append(newNode)


def prob(n):
    """Probability the last person sits in their assigned seat."""

    global count
    count = 0  # numerator
    global ctr
    ctr = 0  # denominator

    root = node('root')

    # seat 1
    for i in range(1, n + 1):
        newNode = node(i)
        newNode.history = root.history + newNode.history
        root.children.append(newNode)

    def wrapper(person):
        if person:
            next_person(person, n)
            for child in person.children:
                wrapper(child)

    # start building the tree
    for person in root.children:
        wrapper(person)

    return (count / ctr)  # the prob that I expected to be 50%


# ========= driver code ==========
index = []
result = []

# maximum 19... prob(20) takes too long
for i in range(2, 20):
    index.append(i)
    result.append(prob(i))

# plotting
import matplotlib.pyplot as pyplot
import numpy as np
pyplot.scatter(index, result)
pyplot.xticks(np.arange(min(index), max(index) + 1, 1.0))
pyplot.show()