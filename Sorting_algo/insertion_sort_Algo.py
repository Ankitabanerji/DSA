def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print ("Sorted array is:")

print(arr)
"""Let us now understand working with the following example:

Consider the following array: 25, 17, 31, 13, 2
First Iteration: Compare 25 with 17. The comparison shows 17< 25. Hence swap 17 and 25.
The array now looks like:
17, 25, 31, 13, 2

Second Iteration: Begin with the second element (25), but it was already swapped on for the correct position, so we move ahead to the next element.
Now hold on to the third element (31) and compare with the ones preceding it.
Since 31> 25, no swapping takes place.
Also, 31> 17, no swapping takes place and 31 remains at its position.
The array after the Second iteration looks like:
17, 25, 31, 13, 2

Third Iteration: Start the following Iteration with the fourth element (13), and compare it with its preceding elements.
Since 13< 31, we swap the two.
Array now becomes: 17, 25, 13, 31, 2.
But there still exist elements that we haven’t yet compared with 13. Now the comparison takes place between 25 and 13. 
Since, 13 < 25, we swap the two.
The array becomes 17, 13, 25, 31, 2.
The last comparison for the iteration is now between 17 and 13. Since 13 < 17, we swap the two.
The array now becomes 13, 17, 25, 31, 2.

Fourth Iteration: The last iteration calls for the comparison of the last element (2), with all the preceding elements 
and make the appropriate swapping between elements.
Since, 2< 31. Swap 2 and 31.
Array now becomes: 13, 17, 25, 2, 31.
Compare 2 with 25, 17, 13.
Since, 2< 25. Swap 25 and 2.
13, 17, 2, 25, 31.
Compare 2 with 17 and 13.
Since, 2<17. Swap 2 and 17.
Array now becomes:
13, 2, 17, 25, 31.
The last comparison for the Iteration is to compare 2 with 13.
Since 2< 13. Swap 2 and 13.

The array now becomes:
2, 13, 17, 25, 31.
This is the final array after all the corresponding iterations and swapping of elements.

Worst Case Time Complexity [ Big-O ]: O(n**2)
Best Case Time Complexity [Big-omega]: O(n)
Average Time Complexity [Big-theta]: O(n**2)"""
