#include<bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin>>n;

    int firstTerm=0;
    int secondTerm=1;
    int nextTerm;

    for(int i=0;i<n;i++){
        if(i<=1){
            cout<<i<<" ";
        }else{
            nextTerm=firstTerm+secondTerm;
            cout<<nextTerm<<" ";
            firstTerm=secondTerm;
            secondTerm=nextTerm;
        }

    }
    return 0;
}