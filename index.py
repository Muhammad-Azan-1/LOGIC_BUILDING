

#! Important concept

#? 1. `a = [1, 2]; a.append(a)`. What does `print(a)` show, and what do `len(a)` and `a[2][2][0]` give? Why doesn't it loop forever?
# [1,2,[...]] we push the a inside it self now the a list holds the a infinite times


#? 2. Predict the final `x`:

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



#? 3. Write `find_all(lst, x)` that returns every index of `x` using only `index()` with its `start` argument (no `enumerate`, no loop over indices).
#?  Handle the `ValueError`.

# a = [[0] * 3] * 3
# print(a)
# b = a.copy()
# a[0][0] = 5
# print(a)


# 1. Why do they share the same reference?

# In Python, the multiplication operator (*) on a list copies references (pointers), not the actual objects.

# Let's break down the code step-by-step:

# [0] * 3: Creates one inner list containing three zeros: [0, 0, 0]. Let's imagine its memory address is Memory Location A.

# [[0] * 3]: Puts that inner list inside an outer list: [Memory Location A].

# [...] * 3: Multiplies that outer list by 3. Instead of creating 3 new lists, Python just copies the reference/pointer to Memory Location A three times.

# So your outer list actually looks like this under the hood:[Memory Location A, Memory Location A, Memory Location A]

# 2. Why does print() show three separate lists?
# When you use print(a), Python looks at the outer list and says: "What is in slot 0? It points to memory location where this list is store [0, 0, 0]."
# "What is in slot 1? It points to again [0, 0, 0]. What is in slot 2? It points to again same as above[0, 0, 0]."

#? 6. Sort `["Azan", "zayyan", "muhammad", "raza", "huzaif", "anus"]` by length descending,  # with ties broken alphabetically ascending, in a single `sort()` call.


# ## 6. sort() with key = tuple (multi-rule sorting)

# idea : sort() compares whatever the key function returns, not the items themselves.
#        If the key returns a pair (a, b), sort treats it as "sort by a, break ties with b".

# how it works :
# 1. sort calls the key function once on every item and builds a pair for each
# 2. it compares the pairs with each other
# 3. first values differ  -> the first value decides, second value is never looked at
# 4. first values equal (tie) -> the second value decides
# 5. it rearranges the ORIGINAL items to match that order (the list never holds pairs)

# analogy : phone book. Sort by last name first, only when two last names match look at first name.

# making one rule descending and the other ascending in a single sort :
# 1. sort stays ascending (no reverse=True), because reverse flips BOTH values
# 2. for numbers, put a minus sign in front: -8 < -6 < -4, so the biggest comes first
# 3. strings keep their default A to Z order

# running example : key = (-len(item), item)
# 1. muhammad -> (-8, muhammad)  -8 beats -6, so it comes first, names never compared
# 2. zayyan   -> (-6, zayyan)    tie with huzaif on -6, so the name decides
# 3. huzaif   -> (-6, huzaif)    huzaif comes before zayyan

# watch out : plain strings put capitals before lowercase ("Azan" before "anus").
#             use item.lower() as the second value if case should be ignored

# remember : the ORDER of values inside the pair = the priority of the rules


# 2. Sort integers by their number of `1` bits in binary, ties by value descending. 
# Then explain why sorting twice (secondary key first, primary key second) also works. What property guarantees that?
lst = ["Azan", "zayyan", "muhammad", "raza", "huzaif", "anus"]
def resolve_sort(item):
   return (-len(item) , item)

# lst.sort(key=resolve_sort)
# print(lst)

#! -- ends here
