class Node:
    def __init__(self,data):
        self.data = data
        self.next = None




def ll_input():
    head = None

    arr = [int(x) for x in input().split()]

    for ele in arr:
        if ele==-1:
            break
        else:
            node = Node(ele)

            if head is None:
                head = node
                tail = node


            else:
                tail.next = node
                tail = node
    return head



def printll(head):
    temp = head
    while temp is not None:
        print(temp.data,"-->",end="")
        temp = temp.next
    print("None")





def reverse1(head):
    prev = None
    while head is not None:
        save = head.next
        head.next = prev
        prev = head
        head = save


    return prev



# he = ll_input()
# printll(he)
# he2 = reverse1(he)
# printll(he2)



