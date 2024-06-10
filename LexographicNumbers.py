
# Python3 program to implement
# above approach
 
# Function to print all the 
# numbers up to n in 
# lexicographical order 
def lexNumbers(n):
     
    s = []

    #Put numbers till n in string format in an array
    for i in range(1, n + 1):
        s.append(str(i))
         
    
    s.sort()

    ans = []
     
    for i in range(n):
        ans.append(int(s[i])) 
 
    for i in range(n):
        print(ans[i], end = ' ')
         
# Driver Code 
if __name__ == "__main__": 
     
    n = 15
    lexNumbers(n)