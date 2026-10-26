

## 1. The Blueprint

# The initial function is called with our full list: `permutations([1, 2, 3])`.
# Because the list length is greater than 1, we jump to the `else` block and start looping through our three numbers.

# ---

# > **The Core Rule:** We isolate `current`, find all permutations of the `remainder`, and then glue `current` to the front of each one.

# ## 2. Loop 1: Fixing `1`

# **Current:** `1` | **Remainder:** `[2, 3]`

# We ask the function to find permutations of `[2, 3]`.
# **Inside the Sub-Task:**

# * It fixes `2`, leaving `[3]`. It glues them to make `[2, 3]`.
# * It fixes `3`, leaving `[2]`. It glues them to make `[3, 2]`.
# * *The sub-task returns:* `[[2, 3], [3, 2]]`

# **The Glue:** The main loop attaches our current `1` to both:

# * `[1] + [2, 3]` = **`[1, 2, 3]`**
# * `[1] + [3, 2]` = **`[1, 3, 2]`**

# ---

# ## 3. Loop 2: Fixing `2`

# **Current:** `2` | **Remainder:** `[1, 3]`

# We ask the function to find permutations of `[1, 3]`.
# **Inside the Sub-Task:**

# * It fixes `1`, leaving `[3]`. It glues them to make `[1, 3]`.
# * It fixes `3`, leaving `[1]`. It glues them to make `[3, 1]`.
# * *The sub-task returns:* `[[1, 3], [3, 1]]`

# **The Glue:** The main loop attaches our current `2` to both:

# * `[2] + [1, 3]` = **`[2, 1, 3]`**
# * `[2] + [3, 1]` = **`[2, 3, 1]`**

# ---

# ## 4. Loop 3: Fixing `3`

# **Current:** `3` | **Remainder:** `[1, 2]`

# We ask the function to find permutations of `[1, 2]`.
# **Inside the Sub-Task:**

# * It fixes `1`, leaving `[2]`. It glues them to make `[1, 2]`.
# * It fixes `2`, leaving `[1]`. It glues them to make `[2, 1]`.
# * *The sub-task returns:* `[[1, 2], [2, 1]]`

# **The Glue:** The main loop attaches our current `3` to both:

# * `[3] + [1, 2]` = **`[3, 1, 2]`**
# * `[3] + [2, 1]` = **`[3, 2, 1]`**

# ---

# ## 5. The Final Output

# The main loop has finished giving every number a turn at the front. It gathers all the bolded results and returns the final list of lists:

# `[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]`