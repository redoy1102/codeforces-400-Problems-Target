#include<bits/stdc++.h>
using namespace std;
int main(){
    int t, n, k;
    cin>>t;
    if((t >= 1) && (t <= 100)){
        cin>>n>>k;
        //n is array size
        if((n >= 1) && (n <= 100) && (k >= 1) && (k <= 1000)){
            int a[n], b[n];
            for(int i = 0; i < n; i++){
                cin>>a[i];
            }
            for(int j = 0; j < n; j++){
                cin>>b[j];
            }
        }
    }
    return 0;
}