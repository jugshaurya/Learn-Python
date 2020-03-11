

// #include <bits/stdc++.h> 
// using namespace std; 
  
// int arr[100000000-1];
// // int arr[100];
// unsigned int countSetBits(int n) 
// { 
//     unsigned int count = 0; 
//     while (n) { 
//         n &= (n - 1); 
//         count++; 
//     } 
//     return count; 
// }

// int main() 
// { 

//   for(int i = 0; i<100000000-1;i++){
//     arr[i] = __builtin_popcount(i) & 1;
//   }

//   int t;
//   cin>>t;
//   while(t--){
//     int n,q;
//     cin>>n>>q;
//     int* temp =  new int[n];
//     int* temp2 =  new int[n];
    
//     for (int i=0;i<n;i++){
//       cin>>temp[i];
//     }
    
//     while(q--){
//       int p;
//       cin>>p;
      
//       for (int i=0; i<n; i++){
//         temp2[i] = countSetBits(temp[i]^p) & 1;
//       }
        
//       int odd = 0 ;
//       int even = 0;
//       for (int i=0; i<n; i++){
//         if(temp2[i]==1){
//           odd+=1;
//         }else{
//           even+=1;
//         }
//       }

//       cout<<even<<" "<<odd<<endl;
//     }
    
//   }
  
//     return 0; 
// } 




#include <bits/stdc++.h> 
using namespace std; 
  
int main() 
{ 
  int t;
  cin>>t;
  while(t--){
    int n,q;
    cin>>n>>q;
    int* inputArr =  new int[n];
    int* pArr = new int[q];
    int j = 0 ;
    for (int i=0;i<n;i++){
      cin>>inputArr[i];
    }
    
    while(q--){
      int p;
      cin>>p;
      pArr[j++] = p;
    }
    
    for (int i =0; i<j;i++){
    
        int even = 0;
        int odd  =0;
        for (int k =0; k<n;k++){
            int x = inputArr[k]^pArr[i];
            int isOdd = (floor(log2(x)) & 1);
            int odd =0;
            int even =0;
            if(isOdd){
              if(x&1){
                even+=1;
              }else{
                odd+=1;
              }
            }else{
              if(x&1){
                odd+=1;
              }else{
                even+=1;
              }
            }

        cout<<even<<" "<<odd<<endl;
        }
    }
  }
    return 0; 
} 



// dishghs;pg

#include <bits/stdc++.h> 
using namespace std; 
  
int main() { 
  ios_base::sync_with_stdio(false); 
  cin.tie(NULL); 
  int t;
  cin>>t;

  while(t--){
    int n,q;
    cin>>n>>q;
    int* inputArr =  new int[n];
    for (int i=0;i<n;i++){
      cin>>inputArr[i];
    }  
    while(q--){
      int p;
      cin>>p;
      int even = 0;
      int odd  =0;
      for (int k =0; k<n; k++){
        int x = inputArr[k]^p;
        int d = floor(log2(x));
        int isOdd = d & 1;
        if(isOdd){
          if(x&1){
            even+=1;
          }else{
            odd+=1;
          }
        }else{
          if(x&1){
            odd+=1;
          }else{
            even+=1;
          }
        }
      }
      cout<<even<<" "<<odd<<endl;
    }
  }
  return 0; 
}

//  Last eakelfre

#include <bits/stdc++.h> 
using namespace std; 
# define SIZE 1000006; 
int garr[SIZE];
  
int main() { 
  ios_base::sync_with_stdio(false); 
  cin.tie(NULL); 
  for(int i = 0; i<SIZE-1;i++){
    garr[i] = __builtin_popcount(i);
  }

  int t;
  cin>>t;

  while(t--){
    int n,q;
    cin>>n>>q;
    int* inputArr =  new int[n];
    for (int i=0;i<n;i++){
      cin>>inputArr[i];
    }  
    while(q--){
      int p;
      cin>>p;
      int even = 0;
      int odd  =0;
      for (int k =0; k<n; k++){
        int x = inputArr[k]^p;
        int d = 0;
        if(x>=SIZE){
           d = floor(log2(x));
        }else{
          d = garr[x]
        }

        int isOdd = d & 1;
        if(isOdd){
          if(x&1){
            even+=1;
          }else{
            odd+=1;
          }
        }else{
          if(x&1){
            odd+=1;
          }else{
            even+=1;
          }
        }
      }
      cout<<even<<" "<<odd<<"\n";
    }
  }
  return 0; 
}



// /alsdhf;ahd


#include <bits/stdc++.h> 
using namespace std; 
  
int main() 
{ 
  ios_base::sync_with_stdio(false); 
  cin.tie(NULL); 
  
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
        temp2[i] = __builtin_popcount(temp[i]^p) & 1;
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

      cout<<even<<" "<<odd<<"\n";
    }
    
  }
  
    return 0; 
} 
