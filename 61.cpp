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
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (k<1) return head;
        if (head == 0) return head;

        ListNode* p = head;

        int len = 1;
        while (p->next != 0) {
            p = p->next;
            len++;
        }
        if (k>=len) k = k%len;
        
        p->next = head; // last node連去head
        p = head; // p重新開始
        for (int i=1; i<len-k; i++) {
            p = p->next; // p去斷開的左邊
        }
        head = p->next; // head = 斷開的右邊
        p->next = 0; // 斷開的左邊要接0
        return head;
    }
};
