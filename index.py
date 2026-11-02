

#! Important concept

#* 1. `a = [1, 2]; a.append(a)`. What does `print(a)` show, and what do `len(a)` and `a[2][2][0]` give? Why doesn't it loop forever?
#* [1,2,[...]] we push the a inside it sel now the a list holds the a infinite times


#* 2. Predict the final `x`:

# x = [1, 2, 3]
# x.extend(x)
# x.insert(len(x), x[:2])
# x.insert(-2 ,'z')


# print(x[-1])
# print(x)

# bahaviour of insert 

# This behavior happens any time you use a negative index (like -1, -2, etc.) with insert().

# The confusion is caused by a clash between two rules:

# The Rule of Negative Indices: -1 refers to the last item in the list.

# The Rule of insert(): insert() always places the new item before the index you give it.

# When you combine them, x.insert(-1, 'z') tells Python: "Find the item at index -1 (the last item), 
# and insert 'z' right before it." Because it inserts before the last item, your new item ends up in the second-to-last position, 
# pushing the original last item out of the way.



#* 2. Write `find_all(lst, x)` that returns every index of `x` using only `index()` with its `start` argument (no `enumerate`, no loop over indices).
#*  Handle the `ValueError`.

# a = [[0] * 3] * 3
# print(a)
# b = a.copy()
# a[0][0] = 5
# print(a)

#* ----- *#

# 1. Why do they share the same reference?

# In Python, the multiplication operator (*) on a list copies references (pointers), not the actual objects.

# Let's break down the code step-by-step:

# [0] * 3: Creates one inner list containing three zeros: [0, 0, 0]. Let's imagine its memory address is Memory Location A.

# [[0] * 3]: Puts that inner list inside an outer list: [Memory Location A].

# [...] * 3: Multiplies that outer list by 3. Instead of creating 3 new lists, Python just copies the reference/pointer to Memory Location A three times.

# So your outer list actually looks like this under the hood:[Memory Location A, Memory Location A, Memory Location A]

# 2. Why does print() show three separate lists?
# When you use print(a), Python looks at the outer list and says: "What is in slot 0? It points to [0, 0, 0]."
# "What is in slot 1? It points to [0, 0, 0]. What is in slot 2? It points to [0, 0, 0]."

#! -- ends here

