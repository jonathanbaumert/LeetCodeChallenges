
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def createLinkedListFromArray(arrayIn: list) -> ListNode:
    linkedList = list()
    linkedList.append((ListNode(arrayIn[0])))
    for i in range(1,len(arrayIn)):
        linkedList.append(ListNode(arrayIn[i]))
        linkedList[i-1].next = linkedList[i]

    return linkedList[0]


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    values = [l1.val,l2.val]
    i = 1
    nextNode1 = l1.next
    while nextNode1 != None:
        values[0] = values[0] + nextNode1.val * (10 ** i)
        i = i+1
        nextNode1 = nextNode1.next
        
    i = 1
    nextNode2 = l2.next
    while nextNode2 != None:
        values[1] = values[1] + nextNode2.val * (10 ** i)
        i = i + 1
        nextNode2 = nextNode2.next
        
    sumVal = values[0] + values[1]
    
    returnNode = ListNode()
    returnNode.val = sumVal % 10
    sumVal = int(sumVal/10)
    
    nodeList = list()
    nodeList.append(returnNode)
    i = 1
    
    # set up a list
    while sumVal > 0:
        nodeList.append(ListNode())
        nodeList[i].val = sumVal % 10
        sumVal = int(sumVal/10)
        nodeList[i-1].next = nodeList[i]
        i = i + 1
    
    return returnNode

hundNode1 = ListNode(3)
tensNode1 = ListNode(4, hundNode1)
onesNode1 = ListNode(2, tensNode1)

hundNode2 = ListNode(4)
tensNode2 = ListNode(6, hundNode2)
onesNode2 = ListNode(5, tensNode2)

o = addTwoNumbers(onesNode1,onesNode2)
print(f"{o.val}, {o.next.val}, {o.next.next.val}")

tensNode3 = ListNode(8)
onesNode3 = ListNode(1, tensNode3)

onesNode4 = ListNode(0)
o2 = addTwoNumbers(onesNode3, onesNode4)
print(f"{o2.val}, {o2.next.val}")
