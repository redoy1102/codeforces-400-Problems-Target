#include <bits/stdc++.h>
using namespace std;
 
int main() {
    int t, flag = 0;
    string s;
    char c;
    cin>>t;
    
    
    while(t--)
    {
        cin>>s;
        int sSize = s.length();
        
        if(sSize %2 != 0)
        {
            if(sSize >= 1 && sSize <= 49)
            {
                cin>>c;
                if(c >= 'a' && c <= 'z')
                {
                    for(int i = 0; i < sSize; i+=2)
                    {
                        if(s[i] == c){
                            flag++;
                        }
                    }
                    if(flag > 0)    cout<<"YES"<<endl;
                    else    cout<<"NO"<<endl;
                    flag = 0;
                }
            }
        }
    }
    
    return 0;
}
