#include<bits/stdc++.h>
using namespace std;
int main(){
    int t, n;
    cin>>t;
    if((t >= 1) && (t <= 990)){
        while(t--){
            cin>>n;
            if((n >= 10) && (n <= 999)){
                if(n %7 == 0){
                    cout<<n<<endl;
                }
                else{
                    int r = n % 7;
                    //cout<<r<<endl;
                    int add = (7 - r);
                    //cout<<add<<endl;
                    int lastDigit = n % 10;
                    //cout<<lastDigit<<endl;
                    int lastDigitAdd = lastDigit + add;
                    //cout<<lastDigitAdd<<endl;

                    if(lastDigitAdd < 10){
                        cout << n + add << endl;
                    }
                    else{
                        cout << n - r << endl;
                    }
                }
            }
        }
    }
    return 0;
}