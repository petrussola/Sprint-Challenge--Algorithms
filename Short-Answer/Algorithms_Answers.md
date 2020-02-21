#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n^3) - quadratic runtime - a loop goes on for n * n * n. A loop on n would be O(n). SInce lenght of loop is 3 times n, it is O(n) * O(n) * O(n) => O(n^3). Inside the loop it is O(1), so the overall algorithm is O(n^3) 


b) O(n^2) = quadratic runtime - Nested loop for loop goes on n times - O(n) - and the while loop goes on for O(n) times. Inside the while loop we are doing an O(1), so the while loop is O(n) * O(1), which means the for loop is O(n) * O(n). The total algorithm is then O(n^2).


c) O(n) - linear runtime - bunnyEars gets called n times (it decreases at each iteration) - O(n) with a constant addition - 2. bunnyEars contains an assignment - O(1). Therefore: 2 + O(n) * 0(1) ~= O(n)

## Exercise II


