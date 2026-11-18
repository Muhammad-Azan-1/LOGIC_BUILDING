
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


#* 5. Write a function to find the longest common prefix string amongst an list of strings.

# problem : find the longest prefix amongst the list of string
# pattren : vertical scanning with zip(*lst)
# Horizontal : scanning would compare whole words: take word 1 and word 2 and find their common prefix, then compare that result with word 3.
# Vertical : scanning reads column by column: check the first letters of all words, then the second letters, and so on, stopping at the first
# column that isn’t all the same.
# trick : zip groups the letters at the same position across all words of the list, then we check does that group have all elements same?
#.        if then this will be added to the prefix if not loops break and prefix returned

#* Time O(n*m)
#* where n is the number of words and m is the shortest word length in the list
#* (prefix ki length zyada se zyada m hoti hai kyunke zip sab se choti word pe ruk jata hai,
#*  aur aksar us se kam hoti hai kyunke break pehle mismatch pe loop rok deta hai)

# ["apple", "apple", "apple"].

# Time

# n = 3 words, m = 5 (shortest word ki length)
# Columns = 5, aur har column mein 3 letters check hote hain (count pura group dekhta hai)
# Total = 3 × 5 = 15 checks, yahi O(n·m) hai

# Ab ["flower", "flow", "flght"] dekho. Yahan m = 4, to worst case 3 × 4 = 12 checks banta hai. Lekin teesre column (o, o, i) pe break ho jata hai, to asal mein sirf 3 × 3 = 9 checks hue. O(n·m) worst case hai, aur break actual kaam ko kam kar sakta hai.

# Growth ka andaza

# 1000 words, shortest length 10 → 10,000 checks
# Words double karke 2000 kar do → 20,000 checks, yani kaam bhi double
# Length double karke 20 kar do → phir double


#* space O(n+m)
#* you hold one column at a time, which is n letters, plus the prefix you build, which is at most m letters.

# ["apple", "apple", "apple"] ke liye:

# Ek waqt mein ek column ka group = 3 letters (n)

# Banta hua prefix = 5 letters tak (m)

# Total = 3 + 5 = 8 items, yahi O(n + m) hai


def longest_common_prefix(lst):
    longest_prefix = ''
    if len(lst) == 0 :
        return ""
    if len(lst) == 1:
        return lst[0]
        
    for x in zip(*lst):
       print(x.count(x[0]),x[0])
       if len(x) > x.count(x[0]):
            break
       else:
        longest_prefix+=x[0]

       
    return(longest_prefix)

# print(longest_common_prefix(["flower", "flow", "flight"]))
# print(longest_common_prefix(["flower"]))
# print(longest_common_prefix([]))
# print(longest_common_prefix(["dog", "racecar", "car"]))
# print(longest_common_prefix(["interview", "internet", "interval"]))
# print(longest_common_prefix(["apple", "apple", "apple"] ))
# print(longest_common_prefix(["alone"]))
# print(longest_common_prefix(["flower", "flow"]))
# print(longest_common_prefix(["abxc", "abyc", "abzc"]))




#* 6. Check if an IP address string is a valid IPv4 address without using the `ipaddress` module.

# pattren : loop and if condition
# trick :  check each condition on which an IPV4 number does not satisfy and return false if that condition is true
# time O(n)
# space O(1)

def check_IPV4(ip_address):
   ip_list = ip_address.split(".")
   if len(ip_list) <  4 or  len(ip_list) > 4:
       return False

   if len(ip_list) == 4:
       for i in ip_list:
           
           if not i.isdigit():
               return False

           num = int(i)
           if not (0 <= num <= 255):
                return False

           if i.startswith('0') and i != '0':
               return False

       return True 
            
           

# print(check_IPV4("192.168.1.1"))
# print(check_IPV4("0.0.0.0"))
# print(check_IPV4("255.255.255.255"))
# print(check_IPV4("256.100.50.25"))

# print(check_IPV4("192.168.1"))
# print(check_IPV4("192.168.1.a"))
# print(check_IPV4("192.168..1"))
# (print(check_IPV4("192.168.1")))
# print(check_IPV4("192.168.01.1"))




#* 7. Write a script to format a list of messy phone number strings into a standard `(XXX) XXX-XXXX` format.

import re
def formate_messy_ph(num_str):
    if num_str.strip() == '':
        return False
    
    #clean_num_str = "".join(c for c in s if c.isdigit()) alternative
    clean_num_str = re.sub(r"\D" , "" , num_str)
    if (len(clean_num_str) == 11 and clean_num_str[0] == '1'):
        clean_num_str = clean_num_str[1:]
    elif (len(clean_num_str) != 10):
        return False

    return f'({clean_num_str[0:3]}) {clean_num_str[3:6]}-{clean_num_str[6:]} '


phones = [
    "123-456-7890",
    "(123) 456-7890",
    "123.456.7890",
    "123 456 7890",
    "1234567890",
    "+1 123 456 7890",
    "1-123-456-7890",
    "  (123)456-7890  ",
    "123-45-67890",
    "123-45-67890",
    "123-45-678901",
    "123-45-6789",
]

for p in phones:
    pass
    # print(formate_messy_ph(p))