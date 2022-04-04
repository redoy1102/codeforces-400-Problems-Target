#include<bits/stdc++.h>
using namespace std;
int sd(int n)
{
    int cN = n, flag = 1;
    while(cN>0)
    {
        int mod = cN % 10;
        if(mod %2 == 0)
        {
            flag = 0;
        }
        cN /= 10; 
    }
    
    return flag;
}
 
int main()
{
    int t, n;
    cin>>t;
    while(t--)
    {
        cin>>n;
        if(n %2 == 0)   cout<<0<<endl;
        
        else if((n < 10 && n %2 != 0) || (sd(n) == 1))  cout<<-1<<endl;
        
        else if(n %2 != 0)
        {
            int digits = (int)log10(n);
            int fd = (int)(n / pow(10, digits));
            
            if(fd %2 == 0)  cout<<1<<endl;
            else            cout<<2<<endl;
        }
        
    }
    return 0;
}
