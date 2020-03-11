

#include <bits/stdc++.h> 
using namespace std; 
  
int arr[100000000-1];
// int arr[100];
unsigned int countSetBits(int n) 
{ 
    unsigned int count = 0; 
    while (n) { 
        n &= (n - 1); 
        count++; 
    } 
    return count; 
}

int main() 
{ 

  for(int i = 0; i<100000000-1;i++){
    arr[i] = __builtin_popcount(i) & 1;
  }

  int t;
  cin>>t;
  while(t--){
    int n,q;
    cin>>n>>q;
    int* temp =  new int[n];
    int* temp2 =  new int[n];
    
    for (int i=0;i<n;i++){
      cin>>temp[i];
    }
    
    while(q--){
      int p;
      cin>>p;
      
      for (int i=0; i<n; i++){
        temp2[i] = countSetBits(temp[i]^p) & 1;
      }
        
      int odd = 0 ;
      int even = 0;
      for (int i=0; i<n; i++){
        if(temp2[i]==1){
          odd+=1;
        }else{
          even+=1;
        }
      }

      cout<<even<<" "<<odd<<endl;
    }
    
  }
  
    return 0; 
} 




// #include <bits/stdc++.h> 
// using namespace std; 
  
// int oddEvenArr[100000008];
// int main() 
// { 

//   for(int i = 0; i<100000008;i++){
//     oddEvenArr[i] = __builtin_popcount(i) & 1;
//   }

//   int t;
//   cin>>t;
//   while(t--){
//     int n,q;
//     cin>>n>>q;
//     int* inputArr =  new int[n];
//     int* pArr = new int[q];
//     int j = 0 ;
//     for (int i=0;i<n;i++){
//       cin>>inputArr[i];
//     }
    
//     while(q--){
//       int p;
//       cin>>p;
//       pArr[j++] = p;
//     }
    
//     for (int i =0; i<j;i++){
    
//         int even = 0;
//         int odd  =0;
//         for (int k =0;k<n;k++){
//             int val = oddEvenArr[inputArr[k]^pArr[i]];
//             if(val==1){
//                 odd+=1;
//             }else{
//                 even+=1;
//             }
//         }
//         cout<<even<<" "<<odd<<endl;
//     }
    
    
    
//   }
  
//     return 0; 
// } 
