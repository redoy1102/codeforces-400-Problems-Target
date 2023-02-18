#include<bits/stdc++.h>
using namespace std;

int gcd(int n1, int n2){
    while(n2 != 0){
        int r = n1 % n2;
        n1 = n2;
        n2 = r;
    }
    return n1;
}

int main(){
    int t, l, r, j, k, m, n, p, size = 1, v1 = 1, v2 = 2;
    bool decision;
    cin>>t;
    while(t--){
        cin>>l>>r>>k;
        if((l > 0) && (r > 0) && (k >= 0)){
            for(int i = l; i < r; i++){
                size++;
            }
            int a[size];
            //cout<<"Size = "<<size<<endl;
            for(j = l, m = 0; j <= r, m < size; j++, m++){
                a[m] = j;
            }
            //!Array 
            // for(n = 0; n < size; n++){
            //     cout<<a[n]<<" ";
            // }
            if(k == 0){
                int res = gcd(l, r);
                if(res > 1){
                    cout<<"YES"<<endl;
                }
                else{
                    cout<<"NO"<<endl;
                }
            }
            else{
                for(p = 1, v1, v2; p <= k, v1 < size, v2 < size; p++, v1 += 2, v2 += 2){
                    int res1 = gcd(a[0],(a[v1] * a[v2]));
                    cout<<"res1 = "<<res1<<endl;
                    if(res1 > 1){
                        decision = true;
                    }
                    else{
                        decision = false;
                    }
                }
                if(decision == true){
                    cout<<"YES"<<endl;
                }
                else{
                    cout<<"NO"<<endl;
                }
            }
        }
    }
    return 0;
}