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
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = 0;
        ListNode* cur = head;
        ListNode* next = 0;
        while (cur != 0) {
            next = cur->next;
            cur->next = prev;
            prev = cur;
            cur = next;
        }
        // head = prev; //可以不用，因爲直接return new head address就可以
        return prev;
    }
};
