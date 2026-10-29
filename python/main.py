
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


transpose_2D_matrix(matrix_2D)