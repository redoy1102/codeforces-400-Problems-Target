#include<bits/stdc++.h>
using namespace std;
int main(){
    int t, zero = 0, one = 0;
    string s;
    cin>>t;
    if((t >= 1) && (t <= 10^4)){
        for(int i = 0; i < t; i++){
            cin>>s;
            if(s.size() <= 200000){
                for(int j = 0; j < s.size(); j++){
                    if(s[j] == '0'){
                        zero++;
                    }
                    else{
                        one++;
                    }
                }
                if(zero < one){
                    cout<<zero<<endl;
                }
                else if(one < zero){
                    cout<<one<<endl;
                }
                else if (one == zero){
                    cout<<(one - 1)<<endl;
                }
            }
            zero = 0;
            one = 0;
        }
    }
    return 0;
}