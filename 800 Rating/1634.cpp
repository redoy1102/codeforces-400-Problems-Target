#include<bits/stdc++.h>
using namespace std;
int main(){
    int n, t, k;
    string s, cs;
    cin>>t;
    while(t--){
        cin>>n>>k;
        cin>>s;
        cs = s;
        reverse(cs.begin(), cs.end());
        if(k == 0 or cs == s) cout<<1<<endl;
        else cout<<2<<endl;
 
    }
 
    return 0;
}
