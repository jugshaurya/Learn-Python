# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head1 = l1
        head2 = l2
        newHead = None
        newTail = None
        while(head1 is not None and head2 is not None):
            newNode = ListNode((head1.val + head2.val + carry) % 10)
            carry = (head1.val + head2.val + carry) // 10
            if(not newHead):
                newHead = newNode
                newTail = newNode
            elif newTail == newHead:
                newHead.next = newNode
                newTail = newNode
            else:
                newTail.next = newNode
                newTail = newNode
            head1 = head1.next
            head2 = head2.next
        if(head1):
            while(head1 is not None):
                newNode = ListNode((head1.val + carry) % 10)
                carry = (head1.val + carry) // 10
                if(newHead == newTail):
                    newHead.next = newNode
                    newTail = newNode
                else:
                    newTail.next = newNode
                    newTail = newNode
                head1 = head1.next
        if(head2):
            while(head2 is not None):
                newNode = ListNode((head2.val + carry) % 10)
                carry = (head2.val + carry) // 10
                if(newHead == newTail):
                    newHead.next = newNode
                    newTail = newNode
                else:
                    newTail.next = newNode
                    newTail = newNode
                head1 = head1.next

        if(carry != 0):
            newNode = ListNode(carry)
            if(newHead == newTail):
                newHead.next = newNode
                newTail = newNode
            else:
                newTail.next = newNode
                newTail = newNode

        return newHead


def stringToIntegerList(input):
    return json.loads(input)


def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


def main():
    import sys
    import io

    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            l1 = stringToListNode(line)
            line = next(lines)
            l2 = stringToListNode(line)

            ret = Solution().addTwoNumbers(l1, l2)

            out = listNodeToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
