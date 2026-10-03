class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth = group_prev

            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_next = kth.next

            prev = group_next
            curr = group_prev.next

            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            old_start = group_prev.next
            group_prev.next = kth
            group_prev = old_start