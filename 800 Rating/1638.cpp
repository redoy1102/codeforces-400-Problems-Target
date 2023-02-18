#include<bits/stdc++.h>
using namespace std;
int main(){
    int t, n, ac = 0, c = 0;
    cin>>t; //test case
    if((t >= 1) && (t <= 500)){
        while(t--){
            cin>>n; //array length
            if((n >= 1) && (n <= 500)){
                int a[n],b[n];
                
                for(int i = 0; i < n; i++){ //taking values of array
                    int x;
                    cin>>x;
                    a[i] = x;
                    b[i] = x;
                }
                if(n == 1){
                    for(int j = 0; j < n; j++){
                        cout<<a[j];
                    }
                    cout<<endl;
                }
                else{
                    for(int k = 0; k <= n-1; k++){
                        if(a[k] > a[k+1]){
                            ac++;
                        }
                    }
                    if(ac > 0){
                        for(int l = 0; l < n; l++){
                            if(a[l] > a[l+1]){
                                a[l] = b[l+1];
                                a[l+1] = b[l];
                                c++;
                            }
                            if(c==1){
                                for(int m = 0; m < n; m++){
                                    cout<<a[m]<<" ";
                                }
                                cout<<endl;
                                c = 0;
                                ac = 0;
                                break;
                            }
                        }
                    }
                    else{
                        for(int p = 0; p < n; p++){
                            cout<<a[p]<<" ";
                        }
                        cout<<endl;
                    }
                }
            }
        }
    }
    return 0;
}
