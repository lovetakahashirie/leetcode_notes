/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

// 方法
// return base case
// 用fast slow pointer 去 get mid左邊的
// 斷開mid
// recursion,sort(left),sort(right)
// merge(left,right) -->>> 開dummy，比較小的放進去，一邊放完就接另一邊
// return head

class Solution {
public:
    ListNode* sortList(ListNode* head) {
        if (head == 0 || head->next == 0)
            return head; // 0 or 1 node, no need to sort
        ListNode* left = head; // 寫出來清楚一點，也可以直接用head代替left
        ListNode* mid = get_mid(head); // 用fast slow pointer
        ListNode* right = mid->next;
        mid->next = 0;
        left = sortList(left);
        right = sortList(right);
        return merge(left, right); // leetcode21，可以不用剪接，直接開新搬過去
    }

    ListNode* merge(ListNode* left, ListNode* right) {
        ListNode* dummy = new ListNode(); // dummy
        ListNode* cur = dummy;
        while (left != 0 && right != 0) {
            if (left->val <= right->val) {
                cur->next = left;
                left = left->next;
            } else {
                cur->next = right;
                right = right->next;
            }
            cur = cur->next;
        }
        // 出while就應該會有任何一個null，或是兩個都null
        if (left == 0)
            cur->next = right;
        else
            cur->next = left; // 這個無所謂的，反正0也可以
        cur = dummy->next;    // cur set as head
        delete dummy;
        return cur; // new merged list head
    }
    ListNode* get_mid(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = slow->next; // 先排好1，2位
        while (fast != 0 &&
               fast->next !=
                   0) { // 確保有兩格可以移，所以要保證現在and下一格都可以動
            slow = slow->next;
            fast = fast->next->next; // fast到null時，slow就到中間
        }
        return slow;
    }
};


