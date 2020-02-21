#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n^3) - quadratic runtime - a loop goes on for n * n * n. A loop on n would be O(n). SInce lenght of loop is 3 times n, it is O(n) * O(n) * O(n) => O(n^3). Inside the loop it is O(1), so the overall algorithm is O(n^3) 

# ^ Correction - O(n) because line 11 is a * a, so it ends up being iteration over n

b) O(n^2) = quadratic runtime - Nested loop for loop goes on n times - O(n) - and the while loop goes on for O(n) times. Inside the while loop we are doing an O(1), so the while loop is O(n) * O(1), which means the for loop is O(n) * O(n). The total algorithm is then O(n^2).

# ^ Correction - O(n log n) becasue nested loop is O(log n) - n is being divided every time by 2

c) O(n) - linear runtime - bunnyEars gets called n times (it decreases at each iteration) - O(n) with a constant addition - 2. bunnyEars contains an assignment - O(1). Therefore: 2 + O(n) * 0(1) ~= O(n)

## Exercise II

1. We look for the middle floor in the building and we throw an egg. For that, we add first floor (in position 0) and last floor and divide by two.
2. If the egg breaks, it means that the floor we are looking for should be lower. Therefore, we set the highest floor to the floor underneath the middle one.
3. If the egg breaks it means that the floor we are looking for should be higher. Therefore, we set the lower floor in our algorithm to the floor above the one we tried.
4. We then look for the middle floor between the first and the highest one using the same technique as point 1 above and we throw an egg. If it breaks, we go back to step 2 above. If it doesn't, to step 3.
5. Eventually we will be narrowing down to one floor, which will be f.

^ BINARY SEARCH :) - Runtime complexity is O(log n)



