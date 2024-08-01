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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if (left == right) return head;

        ListNode* l = head;
        ListNode* r = head;
        ListNode* prev=0;
        ListNode* cur=0;
        ListNode* next=0;
        
        for (int i=1; i<left; i++) {l = l->next;}
        for (int i=1; i<right; i++) {r = r->next;}
        cur = l; next = cur->next;

        l->next = r->next;
        while (cur != r) {
            prev = cur; cur = next; next = next->next;
            cur->next = prev;
        }

        if (head == l) {
            head = r;
            return head;
        }
        else {
            cur = head;
            while (cur->next != l) {
                cur = cur->next;
            }
            cur->next = r;
            return head;
        }
    }
};
