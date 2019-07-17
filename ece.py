using namespace std; 
  
// Returns count of all numbers smaller than 
// or equal to n and multples of 3 or 7 or both 
int countMultiples(int n) 
{ 
    int res = 0; 
    for (int i=1; i<=n; i++) 
       if (i%3==0 || i%7 == 0) 
           res++; 
  
    return res; 
} 
  
// Driver code 
int main() 
{ 
   cout << "Count = " << countMultiples(25); 
} 
