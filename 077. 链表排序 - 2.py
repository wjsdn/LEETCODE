# 开发时间：2022/9/16 14:41
# 文件名称：077. 链表排序 - 2.py
# LC官方解法：方法二：自底向上归并排序
# MEDIUM
'''
输入：5
-1 5 3 4 0
输出：-1 0 3 4 5
输入：4
4 2 1 3
输出：1 2 3 4
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sortList(head: ListNode) -> ListNode:
    if not head:
        return head

    def merge(head1: ListNode, head2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        temp, temp1, temp2 = dummyHead, head1, head2
        # 根据下方函数可知，此时temp，temp1，temp2都是互相不连接的
        while temp1 and temp2:
            if temp1.val <= temp2.val:
                temp.next = temp1
                temp1 = temp1.next
            else:
                temp.next = temp2
                temp2 = temp2.next
            # 此时temp链接的一定是head1，head2带进来的链表结点中，除了temp之前的结点外，val最小的
            temp = temp.next # temp变为上述最小值
        if temp1:
            temp.next = temp1
        elif temp2:
            temp.next = temp2
        # 某一长度为sublength的链表已经排序完成，跳出了while循环，另一个链表中剩下的结点必定是最大的，连到尾段
        return dummyHead.next

    length = 0
    node = head
    while node:
        length += 1
        node = node.next

    dummyHead = ListNode(0, head)
    subLength = 1
    while subLength < length:
        prev, curr = dummyHead, dummyHead.next
        while curr:
            head1 = curr
            for i in range(1, subLength):
                if curr.next:
                    curr = curr.next
                else:
                    break
            head2 = curr.next
            # 前面这几行只是为了找到2个长度为sublength的链表的头
            curr.next = None # 断开2个长度为sublength的链表的连接
            curr = head2
            for i in range(1, subLength):
                if curr and curr.next:
                    curr = curr.next
                else:
                    break
            # 这几行是为了让curr到达第二个长度为sublength的链表的尾

            succ = None
            if curr:
                succ = curr.next
                curr.next = None
            # 将已找到的2个长度为sublength的链表与后面的结点断开
            # curr在第二个长度为sublength的链表的尾，succ在其余链表的头

            merged = merge(head1, head2) # 将两个链表以排好序的顺序合并，返回合并后链表的头
            prev.next = merged # 将排好序的链表的最后一个结点，和新排好序的链表的头连接起来
            while prev.next:
                prev = prev.next
            # 由于之前curr和succ断开连接，所以prev最后会停留在未排序链表的第一个结点
            curr = succ # curr现在在其余链表的头
        subLength <<= 1 # 二进制左移1位补齐0，相当于每次*2，1->10，10->100……

    return dummyHead.next

def linkList(ls):
    if not ls: return ListNode()
    head = ListNode(ls[0])
    p = head
    q = head
    for i in range(1, len(ls)):
        node = ListNode(ls[i])
        q.next = node
        q = q.next
    return p

if __name__ == "__main__":
    s1 = input()
    s2 = input()
    n = int(s1)
    ls = [int(i) for i in s2.split()]
    head = linkList(ls)
    res = sortList(head)
    for _ in range(n):
        print(res.val, end=" ")
        res = res.next