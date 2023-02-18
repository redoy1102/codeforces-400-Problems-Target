#include<bits/stdc++.h>
using namespace std;
int main(){
    int t, n;
    char ch;
    cin>>t;
    if((t >= 1) && (t <= 100)){
        while(t--){
            cin>>n;
            if((n >= 1) && (n <= 100)){
                string s[n];
                for(int i = 0; i < n; i++){
                    cin>>ch;
                    if((ch == '0' || ch == '1')){
                        s[i] = ch;
                    }
                }
                if(n == 1){
                    cout<<"YES"<<endl;
                }
                else if(n == 2){
                    if(s[0] == s[1]){
                        cout<<"NO"<<endl;
                    }
                    else{
                        cout<<"YES"<<endl;
                    }
                }
                else{
                    cout<<"NO"<<endl;
                }
            }
        }
    }
    return 0;
}