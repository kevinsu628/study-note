'''
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.
'''

'''
Approach 1: two pointers
	i: slow pointer
	j: fast pointer

	Intuition: we assign nums[i] to be nums[j] as long as nums[j] is different than the target

	The whole intuition of two pointer is to replace the array with unique values met by faster pointer
'''



def removeElement(nums, val):
    i = 0;
    for j in range(len(nums)):
        if (nums[j] != val):
            nums[i] = nums[j];
            i+=1

    return i


'''
Approach 2: Two Pointers - when elements to remove are rare
Intuition

Now consider cases where the array contains few elements to remove. 
For example, nums = [1,2,3,5,4], val = 4nums=[1,2,3,5,4],val=4. 
The previous algorithm will do unnecessary copy operation of the first four elements. 
Another example is nums = [4,1,2,3,5], val = 4nums=[4,1,2,3,5],val=4. 
It seems unnecessary to move elements [1,2,3,5][1,2,3,5] one step left as the problem description mentions 
that the order of elements could be changed.

Algorithm

When we encounter nums[i] = valnums[i]=val, 
we can swap the current element out with the last element and dispose the last one. 
This essentially reduces the array's size by 1.

Note that the last element that was swapped in could be the value you want to remove itself. 
xBut don't worry, in the next iteration we will still check this element.
'''

def removeElement(nums, val):
    i = 0
    n = len(nums)

    while (i < n):
        if (nums[i] == val):
            nums[i] = nums[n - 1]
            # reduce array size by one
            n -= 1
        else:
            i += 1
  
    return n;







