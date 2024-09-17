# 注意，題目要找cycle，不是在找同樣的，不能單純用list解決
# 所以要用快慢跑手，只要是cycle，總有一天，快的在跑圈時會追上慢的
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        # 根本不用check slow，因爲fast已經check過不是none了
        while fast and fast.next:
        # 想了一下其實不用這麽細節，反正只要有cycle，最後都會追上，我們只要set好不要.next.next error就可以，剩下的就讓他們自己慢慢追就好
            slow = slow.next
            fast = fast.next.next
            if slow == fast: # 也不用==val，反正cycle的話next是一樣的，而且可以避免none.val的問題
                return True
        return False
