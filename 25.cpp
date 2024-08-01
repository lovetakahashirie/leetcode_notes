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
    void reverse(ListNode* p) { // reverse，不過本來就有start,end指著，可以return void
        if (p->next == 0) {return;}
        reverse(p->next);

        ListNode* q = p->next;
        q->next = p;
        p->next = 0;
        return;
    }

    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode *prev = 0;
        ListNode *start = head;
        ListNode *next = 0;

        if (k==1) return head;

        while (start != 0) {
            ListNode *kth = start; // 開kth，去kth位
            for (int i=1; i<k; i++) {
                kth = kth->next; // 每次向前一格
                if (kth == 0) { // 我就要check是不是到null了，如果到了，代表這個loop少於k個
                    prev->next = start; // 將上一組的連去這組（未做）的start，直接走人
                    return head;
                }
            }

            next = kth->next; //剩下就是reverse的前置要做的，
            kth->next = 0; // 斷
            reverse(start);

            if (head == start) {head = kth;} // 第一組
            else {prev->next = kth;} // 第2345678.....組

            prev = start; // prev轉成上一輪最尾的
            start = next; // 新一輪的第一個
        }

        return head;
    }
};
