#include <bits/stdc++.h>
using namespace std;
 
int main() {
    int n, sum = 0;
    cin>>n;
    while(n--)
    {
        int num[3];
        for(int i = 0; i < 3; i++)
        {
            int x;
            cin>>x;
            if(x == 0 || x == 1)
            {
                num[i] = x;
            }
        }
        
        int c = 0;
        for(int i = 0; i < 3; i++)
        {
            if(num[i] == 1)
            {
                c++;
            }
        }
        if(c >= 2)  sum++;
    }
    cout<<sum<<endl;
    
    return 0;
    
}
