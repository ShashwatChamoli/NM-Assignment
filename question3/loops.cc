#include<iostream>
using namespace std;
int cube(int a,int n)
{
int b=0,c;
for(int i=a;i<a+n;i++)
{
c=i*i*i;
b=b+c;
}
return b;
}
int main()
{
cout<<"The sum of the cubes of 30 consecutive natural numbers starting from 11 is ";
cout<<cube(11,30);
return 0;
}
