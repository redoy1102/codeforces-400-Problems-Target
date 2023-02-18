#include<bits/stdc++.h>
using namespace std;
int main(){
    int t, n, c = 0, highA, highB, high, low, v1, v2;
    cin>>t;
    if((t >= 1) && (t <= 100)){
 
        while(t--){
            cin>>n;
            if((n >= 1) && (n <= 100)){
 
                int a[n], b[n];
                //!Taking array
                for(int i = 0; i < n; i++){
                    cin>>v1;
                    a[i] = v1;
                }
                for(int j = 0; j < n; j++){
                    cin>>v2;
                    b[j] = v2;
                }
                //!checking weather all the values are same or not
                for(int l = 0; l < n; l++){
                    if(a[l] != b[l])    c++;
                }
                if(c == 0)    cout<<(a[0]*b[0])<<endl;

                else{
                    //!sorting
                    for(int k = 0; k < n; k++){
                        high = max(a[k], b[k]);
                        low = min(a[k], b[k]);
                        a[k] = high;
                        b[k] = low;
                    }
 
                    highA = a[0];
                    highB = b[0];
 
                    for(int r = 1; r < n; r++){
                        if(a[r] > highA){
                            highA = a[r];
                            
                        }
                    }
                    for(int s = 1; s < n; s++){
                        if(b[s] > highB)    highB = b[s];
                    }
                    cout<<(highA*highB)<<endl;
                }
            }   
        }
    }
    return 0;
}
