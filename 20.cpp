class Solution {
public:
    bool isValid(string s) {
        stack<char> S;
        int index = 0;
        while(s[index]!='\0') {
            if (s[index]=='(' || s[index]=='{' || s[index]=='[') {
                S.push(s[index]);
            }
            if (s[index]==')' || s[index]=='}' || s[index]==']') {
                if (S.empty() == true ||
                    s[index]==')' && S.top()!='(' || //記得看清楚放進stack的是(，string的是)
                    s[index]=='}' && S.top()!='{' ||
                    s[index]==']' && S.top()!='[' ) {
                    // if (S.top() == s[index]) { // 不能直接比較，因爲push進去的是({[ 開的，對比的是)}]
                        return false;
                    }
                S.pop();
            }
            index++;
        }
        return S.empty();
    }
};
