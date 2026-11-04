
#* 1. Implement basic string compression (e.g., "aabcccccaaa" becomes "a2b1c5a3").

# Problem: String Compression (Python #1)
# Pattern: Linear scan + group counting
# Trick: Keep the current char and a count. When the next char differs, save "char+count", then reset.
#        Don't forget to save the last group after the loop.
# Time: O(n) one pass
# Space: O(n) for the result

def compress_str(value):
    if not value:
        return ""
    parts = []    
    count = 1
    curr = value[0]
    for ch in value[1:]:
        if ch == curr:
            count += 1
        else:
            parts.append(f'{curr}{str(count)}')
            count = 1
            curr = ch
   
    parts.append(f'{curr}{str(count)}')
    return "".join(parts)
  
 
# print(compress_str("aabcccccaa"))
# print(compress_str("ttzzxxttzzxx"))
# print(compress_str(""))



#* 2. Write a function to transpose a 2D matrix without using NumPy or `zip`.

# Problem: Tranpose the 2D matrix (Python #2
# Pattern: Nested loops over a 2D grid, building a new matrix
# trick: find the no of rows and columns then covert rows into colums and columns into rows which means
#          loop through the column and create rows inside it (bcz we need the rows to be exact no of columns so we need to create rows with in columns so it iterates 3 times means create 3 rows)
#           lopp through the row and create columns inside it (bcz we need the columns to be exact no of rows so we need to create columns with in the rows it it iterates 2 times mens create 2 rows per time)

# Time: O(n), n = total number of items (rows x columns).
#       The two loops together visit each item exactly once.
#       10x more items -> about 10x more steps.
# Space: O(n), the new matrix holds every item again.
#        10x more items -> about 10x more memory.
matrix_2D = [
    [1,2,3],
    [4,5,6]
    ]

def transpose_2D_matrix(matrix):
    tranpose_matrix = []

    total_columns = len(matrix[0])
    total_rows = len(matrix)

    for i in range(total_columns): # why inside column we create row ? bcz we have 3 columns and in tranpose we need to convert 3 columns into 3 rows
        row = []
        for j in range(total_rows):
            item1 = matrix[j][i]
            row.append(item1)
        tranpose_matrix.append(row)
    print(tranpose_matrix)


# transpose_2D_matrix(matrix_2D)


#* 3 Rotate a list to the right by `k` steps.

# Problem : Rotate the list to right by k steps [1,2,3,4,5] if k = 2 then [4,5,1,2,3]
# pattren : Repeat a one-step rotation, with k reduced using modulo
# Trick :  k % len(list) removes useless full rotations (k = 7 on 5 items is the same as 2). Each step: pop the last item, insert it at the front.

# Time : : O(n * k), because insert at index 0 shifts every item, and you repeat it k times
#* Time O(n * k) -> Take n = 10 and k = 2:
#* One rotation touches all 10 items, because insert(0, ...) pushes every other item one step to the right.
#* You do that 2 times, so about 10 x 2 = 20 steps.

# Space: O(1), the list is changed in place and only a few variables are used
#* space means the extra memory your code creates does not grow with the input. 
#* Here you create only steps_to_move, i, and item (one value at a time). You never build a new list,
#* because the original list is changed in place. A list of 5 items or 5 million items uses the same three variables.

nums_list = [1,2,3,4,5]
def rotate_list(given_list , k):
    if len(given_list) == 0:
        return []
    
    steps_to_move = k % len(given_list)
    i = 0
    while i < steps_to_move:
        item = given_list.pop()
        given_list.insert(0,item)
        i+=1

    return given_list

# print(rotate_list(nums_list , 2))

#* 4. Find all duplicate elements in a list without using built-in sets.

# problem : find all duplicates items in a list
# Pattren : frequency map (hash map counting)
# Trick : count every item in a dict in one pass, then keep the keys whose count is above 1
# Time : O(n) time, since there’s one pass to count and one to filter
# Space : O(n) space for the dict

nums_list = [1, 2, 3, 2, 4, 5, 1] 

def find_duplicates(nums):
    duplicates = {}
    if len(nums) <= 1:
        return []
    for i in nums:
        duplicates[i] = duplicates.get(i , 0) + 1
    return [x for (x,y) in duplicates.items() if y > 1]
   
# print(find_duplicates(nums_list))
# print(find_duplicates([]))
# print(find_duplicates([7]))

