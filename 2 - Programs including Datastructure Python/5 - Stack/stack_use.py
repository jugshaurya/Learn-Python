from stack_using_array import StackArr
from stack_using_ll import StackLL

s = StackArr()
s.push(12)
s.push(1)
s.push(2)
s.push(102)

print('stack size is ', s.size())
while not s.isEmpty():
    print(s.top())
    s.pop()

s = StackLL()
s.push(12)
s.push(1)
s.push(2)
s.push(102)


print('stack size is ', s.size())
while not s.isEmpty():
    print(s.top())
    s.pop()
    