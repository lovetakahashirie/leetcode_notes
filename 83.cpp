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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* a = head; // 用來移動
        while (a != 0 && a->next != 0) {
            if (a->val == a->next->val) {
                ListNode* temp = a->next;
                a->next = temp->next;
                delete temp;
            }
            if (a->next != 0 && a->val == a->next->val)
            // if 有下個可以compare && repeated
            // 要多考慮不用的case，edge etc.
                continue;
            else
                a = a->next;
        }
        return head;
    }
};
