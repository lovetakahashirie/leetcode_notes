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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        // invalid / base case
        if (list1 == 0 && list2 != 0)
            return list2;
        if (list1 != 0 && list2 == 0)
            return list1;
        if (list1 == 0 && list2 == 0)
            return list1;

        ListNode* head = 0;            // 用來return head;
        if (list2->val < list1->val) { // 想做general start，從最小的開始
            head = list2;
            list2 = list1;
            list1 = head;
        } else {
            head = list1;
        }

        while (list1->next != 0) {
            if (list2 == 0) break;
            if (list1->next->val > list2->val) {
                // compare val, if L1->next > L2, insert L2 between L1 and
                // L1->next
                list2 = insert(list1, list2);
                list1 = list1->next; // 一格一格移動，因爲我新insert后，可能還要新insert的，我要再loop一次
            } else {                       
                list1 = list1->next;
            }
        }

        // 不論list2還有沒有都可以接，反正L2要麽是剩下的，要麽做完了直接
        if (list2 !=0) list1->next = list2;
        return head;
    }

    ListNode* insert(ListNode* l1, ListNode* l2) {
        ListNode* temp = l2->next;
        l2->next = l1->next;
        l1->next = l2;
        return temp;
    }
};
