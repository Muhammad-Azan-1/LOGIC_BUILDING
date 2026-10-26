
### **JavaScript: 50 Logic-Building Challenges**

**Array & String Manipulation (The Fundamentals)**

1. Write a function that takes a string and returns the longest word in it.
2. Given an array of integers, move all zeros to the end while maintaining the relative order of the non-zero elements.
3. Write a function to deeply flatten an array of arbitrarily nested arrays (e.g., `[1, [2, [3, 4]]]`).
4. Implement a function that chunks an array into smaller arrays of a specified size.
5. Find the missing number in an array containing numbers from 1 to N, where one number is missing.
6. Write a function to find the first non-repeating character in a string.
7. Create a function that takes a string and capitalizes the first letter of every word.
8. Find the intersection (common elements) of two arrays without using the built-in `.filter()` method initially.
9. Write a function to check if two strings are perfect anagrams of each other.
10. Given an array of numbers, return all unique pairs that add up to a specific target sum.

**Objects & Data Structures**
11. Write a function to deeply clone an object (without using `JSON.parse(JSON.stringify())`).
12. Merge two objects. If a key exists in both, store their values in an array under that key.
13. Convert a complex nested object into a flattened single-level object with dot-notation keys (e.g., `{'a': {'b': 1}}` becomes `{'a.b': 1}`).
14. Group an array of objects by a specific property (e.g., group an array of users by their `role`).
15. Write a function to invert an object's keys and values.
16. Implement a function that converts a URL query string into a JavaScript object.
17. Write a function that takes an object and a string path (like "user.profile.name") and safely returns the value, or `undefined` if it doesn't exist.
18. Count the occurrences of all properties (including nested ones) in an object and return a frequency map.
19. Implement a basic `Map` data structure using plain JavaScript objects and arrays.
20. Write a function that compares two deeply nested objects and returns `true` if they are identical.

**Functions & Closures (Advanced JS Logic)**
21. Implement a `debounce` function from scratch (delays invoking a function until after X milliseconds have elapsed).
22. Implement a `throttle` function from scratch (ensures a function is only called at most once in a specified time period).
23. Write a function that memoizes another function (caches the results of expensive function calls based on arguments).
24. Create a stateful counter function using closures that can increment, decrement, and reset its value.
25. Implement a `curry` function that transforms a function of N arguments into N functions of 1 argument.
26. Write a function `compose` that takes multiple functions and runs them in sequence, passing the output of one to the input of the next.
27. Implement your own version of `Function.prototype.bind`.
28. Write a function that takes an array of asynchronous functions and runs them sequentially.
29. Create a retry wrapper: a function that attempts to execute a callback function up to X times if it throws an error.
30. Write a function that limits how many times another function can be called (e.g., `once()`).

**Asynchronous & Event Loop**
31. Implement `Promise.all()` from scratch using standard Promises.
32. Write a `sleep` or `delay` function using Promises that pauses execution for X milliseconds.
33. Create a function that wraps a `fetch` request with a timeout (rejects if the request takes longer than X seconds).
34. Write a script that polls an API endpoint every 5 seconds until it receives a specific status code.
35. Implement a concurrent request limiter that takes an array of 100 URLs but only ever fetches 5 at a time.
36. Create a simple Event Emitter class with `.on()`, `.emit()`, and `.off()` methods.
37. Write an async function that fetches user data, then uses the user's ID to fetch their posts, handling errors at both levels.
38. Simulate a race condition by writing two async functions that modify a shared variable, then fix it.
39. Write a countdown timer using `setInterval` that formats time as MM:SS and triggers a callback when it hits zero.
40. Implement a basic observable pattern where subscribers can listen to state changes.

**Algorithmic & System Design Mini-Projects**
41. Implement an LRU (Least Recently Used) Cache class.
42. Write a validator for a string of brackets `(){}[]` to ensure they are properly nested and closed.
43. Build the core logic (no UI) for a Tic-Tac-Toe game, including checking for win states.
44. Write a simple rate limiter logic that allows 3 actions per minute per user ID.
45. Implement a basic mathematical expression evaluator (e.g., "3 + 5 * 2") without using `eval()`.
46. Create a Roman Numeral to Integer converter.
47. Implement binary search on a sorted array.
48. Write a function to sort an array of objects by multiple fields (e.g., sort by age, then by name).
49. Find the shortest path through a 2D grid (maze) from start to finish.
50. Build a basic Dependency Injection container where you can register and resolve services.

---

### **Python: 50 Logic-Building Challenges**

**Lists & Strings**

1. Implement basic string compression (e.g., "aabcccccaaa" becomes "a2b1c5a3").
2. Write a function to transpose a 2D matrix without using NumPy or `zip`.
3. Rotate a list to the right by `k` steps.
4. Find all duplicate elements in a list without using built-in sets.
5. Write a function to find the longest common prefix string amongst an array of strings.
6. Check if an IP address string is a valid IPv4 address without using the `ipaddress` module.
7. Write a script to format a list of messy phone number strings into a standard `(XXX) XXX-XXXX` format.
8. Merge two sorted lists into a single sorted list without using the `.sort()` method.
9. Find the length of the longest substring without repeating characters.
10. Generate all possible permutations of a given list of numbers.

**Dictionaries & Sets**
11. Merge multiple dictionaries, summing the values for keys that appear in more than one dictionary.
12. Write a function that takes a text block and returns a dictionary of word frequencies, ignoring punctuation.
13. Group an array of strings into anagrams (e.g., `["eat", "tea", "tan", "ate", "nat", "bat"]`).
14. Find the symmetric difference of two sets (elements in either set, but not both) using dictionary logic.
15. Invert a dictionary, but if multiple keys have the same value, group the original keys in a list under the new key.
16. Write a dictionary comprehension that maps characters in a string to their ASCII values.
17. Check if dictionary A is a subset of dictionary B (all keys and values match).
18. Implement a cache function that uses a dictionary to store the results of a recursive Fibonacci sequence.
19. Convert a list of edges `[(1, 2), (2, 3), (1, 3)]` into an adjacency list (dictionary) for graph traversal.
20. Write a function to sort a dictionary by its values rather than its keys.

**Functions & Decorators**
21. Write a `@timer` decorator that prints the execution time of the function it decorates.
22. Create a `@retry(n)` decorator that will retry the function `n` times if it raises an Exception.
23. Write a generator function that yields prime numbers infinitely.
24. Create a function that accepts `*args` and `kwargs` and prints only the keyword arguments that are integers.
25. Implement your own version of Python's `map()` function.
26. Write a decorator that validates the types of arguments passed to a function based on annotations.
27. Create a generator that reads a massive file and yields it in chunks of 1024 bytes.
28. Implement a Singleton class design using a decorator.
29. Write a closure in Python that keeps track of a moving average of a stream of numbers.
30. Create a `@memoize` decorator for caching pure functions.

**File I/O & Data Handling**
31. Write a script that reads a CSV file and converts it into a formatted JSON file.
32. Given a directory tree, write a script to find and return the path of the largest file.
33. Parse a server log file and extract a count of the top 5 most frequent IP addresses.
34. Read a JSON file, find a deeply nested key, update its value, and write the file back.
35. Write a script that monitors a text file and prints new lines as they are added (like the `tail -f` command).
36. Write a simple web scraper using `urllib` or `requests` that pulls all `<h1>` tags from a webpage.
37. Extract all valid email addresses from a large body of text using Regular Expressions.
38. Write a program to split a large text file into smaller files of 100 lines each.
39. Convert a basic XML string into a Python dictionary.
40. Use the `sqlite3` library to create a database, insert data from a dictionary, and query it back.

**OOP & Algorithmic Mini-Systems**
41. Build a `BankAccount` class that tracks balance, deposits, withdrawals, and keeps a transaction history log.
42. Implement a Stack and a Queue using only basic Python lists.
43. Design an Object-Oriented text-based To-Do list manager (Tasks should be objects with statuses).
44. Implement a basic Trie data structure for storing words and checking for prefixes (autocomplete logic).
45. Write the logic for Conway's Game of Life on a 2D grid.
46. Create a valid Sudoku board checker (ensures rows, columns, and 3x3 grids contain 1-9 without duplicates).
47. Design a basic Parking Lot object system (tracks available spots, vehicle types, and calculates fees).
48. Write a text-based ATM logic script that handles PIN validation, locking out after 3 attempts, and balance checks.
49. Create a node-based File System tree where folders can contain files or other folders, and write a method to calculate total size.
50. Build a basic Publisher/Subscriber message broker class in Python.

---

The best way to use this list is not to read through it, but to pick **one JavaScript question and one Python question per day**. Open a blank file and try to build the solution entirely on your own before looking up the answer.

Which of these categories (e.g., Arrays, Decorators, OOP Systems, Closures) do you feel is your weakest point right now?