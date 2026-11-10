Good call. Here is the same set with the method names removed from the questions. After each section there is a hint list, so only look at it when you are really stuck. Everything is in words only.

## List questions

1. Build the first N rows of Pascal's triangle, where each row is made from the previous one. Explain what it costs, on average, to add one item to the end of a list.
2. Flatten a list that is nested to any depth, using recursion. Then predict what happens when you merge the string "abc" into a list by spreading it out, compared with adding it as one single item. Do the same with a list **(trap)**.
3. Keep a list sorted while numbers arrive one at a time, without ever re-sorting the whole list. Work out the right position yourself, and explain the cost of each placement.
4. Delete every occurrence of a value from a list in place, without making a new list. Deleting while looping forward skips items, so explain why and fix it **(trap)**.
5. Check whether a string with three kinds of brackets is balanced, using a list as a stack. Then explain why taking an item from the front of a big list is slow and taking one from the back is not.
6. Write a function that receives a list and must empty it for the caller. Show why assigning a new empty list inside the function doesn't work **(trap)**.
7. Find the position of the k-th occurrence of a value, without rescanning from the beginning each time. Handle the case where there are fewer than k occurrences.
8. Decide whether two strings are anagrams without sorting and without a dict. Give the time complexity and say why it is worse than the dict approach **(trap)**.
9. Sort version strings like "1.10.2" and "1.2.10" so that 1.2.10 comes before 1.10.2. Plain alphabetical order gets this wrong **(trap)**.
10. Rotate a list by k positions in place, with no extra list, using only in-place flips of ranges. Work out how many flips you need and why it works.
11. Build a 3×3 grid of zeros in two ways: by repeating one row, and by building each row separately. Change one cell in each and explain the difference. Then explain why making a shallow duplicate of the outer list alone doesn't save you **(trap)**.

**Hints (peek only if stuck)**
1. append
2. extend (and append)
3. insert
4. remove, or looping over a copy
5. pop
6. clear
7. index with its start argument
8. count
9. sort with a key
10. reverse
11. copy

## Tuple questions

1. Before running anything, predict how many times 1 appears in `(1, True, 1.0, "1")` and explain the answer. Then find all the items in a tuple that appear exactly twice, without using a set **(trap)**.
2. Given two tuples, find the first item of the first tuple that also exists in the second, and report its position in both. Handle the case where there is no common item without crashing.

**Hints**
1. count
2. index (plus a safe way to handle the failure)

## Set questions

1. Find the first repeating element in a list, meaning the one whose second occurrence comes earliest, in a single pass. Check `[5, 1, 5, 1]`, where the answer is 5, and `[2, 3, 3, 2]`, where it is 3 **(trap)**.
2. Given each day's visitors as a separate list, find everyone who visited at least once. Then predict what happens if you feed in a string instead of a list **(trap)**.
3. Find the longest run of consecutive numbers in an unsorted list in O(n) time. Make sure a run you have already counted is never counted again.
4. Find all pairs that add up to a target, where each number can be used in only one pair. Track what is still available, and explain why a deletion that never crashes is safer here.
5. Given a graph as a list of edges, count its connected groups. Pick an unvisited starting node each time, and explain why you can't predict which node you get.
6. Track the unique users in the current window of a stream, resetting every K items. Explain when emptying a set is different from creating a new one.
7. Remove all even numbers from a set while looping over it. First explain why that crashes, then fix it **(trap)**.
8. Given each candidate's skills as a set, list all the distinct skills, and then the skills that only one candidate has. The second part needs more than the first, so work out what else you need.
9. Find the items common to K lists. Then change the problem so duplicates must be kept, with `[1, 1, 2]` and `[1, 1, 1]` giving two 1s. Explain why sets can't solve that version **(trap)**.
10. You expect the numbers 1 to N, and you got a list with some missing and some unexpected. Report both groups, and show that the order of the two sets changes the answer.
11. Find the items two inventories disagree on. Then chain the same operation over three sets and work out what the result really means. It is not "in exactly one set" **(trap)**.
12. Decide whether a ransom note can be built from a magazine's letters. Comparing letters as sets looks right but fails when a letter repeats, so find the bug and fix it **(trap)**.
13. Given a job's required skills and a list of candidates, return the ones who qualify. Then also return the ones who are missing at most one skill.
14. Given meetings with their attendee sets, decide whether two meetings can run at the same time. Then return every pair that can, and work out the complexity.
15. Find the users who were active on every day of the week, using one running set that you change in place. Explain why this uses less memory than keeping seven sets.
16. Remove stopwords and already-processed words from a set of words, in place. Explain why the caller's set changes too, and when that is a problem.
17. Process a list of toggle events for light switches, where each event flips one switch. End with the set of lights that are on, using a single set that you change in place.

**Hints**
1. add
2. update
3. remove
4. discard
5. pop
6. clear
7. copy
8. union (plus symmetric_difference or counting)
9. intersection
10. difference
11. symmetric_difference
12. issubset (plus count)
13. issuperset
14. isdisjoint
15. intersection_update
16. difference_update
17. symmetric_difference_update

## Dict questions

1. Count word frequency in a text, then return the top 3 words, with ties broken alphabetically.
2. Check whether two nested dicts have exactly the same structure, comparing keys at every level and ignoring the values.
3. Decide whether all values in a dict are unique. Then return the key with the second-highest value, and say what you do when the top value is shared.
4. Invert a dict whose values can repeat, so each value maps to a list of all the keys that had it. Explain what is lost if you do a plain swap **(trap)**.
5. Merge two nested dicts so the inner dicts are merged instead of replaced. First show what a simple merge does to the inner dicts **(trap)**.
6. Build a cache with a fixed capacity where reading an item makes it the most recent, and when full, the oldest item is dropped. Explain why the order dicts remember makes this possible.
7. Remove the last N inserted pairs from a dict and return them. Explain the order they come out in, and what happens when the dict is empty.
8. Build a graph's adjacency list from a list of edges in a single pass. Then find the nodes that have no incoming edges.
9. Two modules share one config dict. Show why rebinding a name to a new empty dict doesn't reset it for the other module, and what does **(trap)**.
10. Duplicate a dict whose values are lists, then change one list in the duplicate and watch the original change. Fix it without a special deep-duplicate tool first, then with one.
11. Remove duplicates from a list while keeping the original order. Then create a dict from a list of keys where every value is an empty list, and find out why all keys end up sharing one list **(trap)**.

**Hints**
1. get with a default
2. keys
3. values
4. items (plus setdefault)
5. update
6. pop (plus the dict's insertion order)
7. popitem
8. setdefault
9. clear
10. copy (then deepcopy)
11. fromkeys

## Comprehension questions

**List**
1. Build all pairs `(i, j)` with `i < j` from a list where the sum is divisible by 3, in one expression. Then rewrite it with plain loops and decide which one you would rather read in a review.
2. Flatten a 2D list while keeping only the prime numbers. Then transpose a matrix in one expression.

**Set**
1. Build the set of numbers up to 100 that are divisible by 3 or 5 but not both. Explain why duplicates disappear without extra code.
2. From a sentence, build the set of words whose reverse also appears in the sentence.

**Dict**
1. Map each word to its length, but only for words longer than 3 letters. Then invert it so each length maps to its words, and explain why a one-line version loses data **(trap)**.
2. Build a dict from a names list and a scores list, keeping only the scores above the average, with each name mapped to its rank.

**Tuple and generators**
1. Build a tuple of `(n, n², n³)` for 1 to N where the cube is odd. Then split the result into three separate tuples without a loop.
2. Find the first number under 10,000 divisible by both 7 and 11, without building a list. Then loop over the same generator twice and explain why the second loop is empty.

**Mixed**
1. Replace the negative numbers with 0 while keeping the positives. Then keep only the positives. These look similar but put the condition in different places, so say where it goes in each and why **(trap)**.
2. Turn a list of strings like `"a=1"`, `"b=2"`, `"oops"` into a dict of ints, skipping the broken ones. Then take a triple-nested comprehension and rewrite it as loops, and say where readability breaks down.

**Hints**
1. List 1: two `for` clauses with an `if` at the end. List 2: nested `for` for the flatten, `zip(*matrix)` for the transpose
2. Set 1: `{}` with a condition using `!=` or `^`. Set 2: set membership inside the condition
3. Dict 1: `{}` with a key and value and an `if` at the end. Dict 2: the average has to be computed before the comprehension
4. Tuple 1: `tuple(...)` around a generator, and `zip(*...)`. Tuple 2: `next(...)` on a generator expression
5. Mixed 1: a ternary goes before `for`, a filter goes after. Mixed 2: split each string first, and use a condition to skip the broken ones

## sort and sorted questions

1. Sort names by number of vowels descending, then by length ascending, then alphabetically ignoring case. Say whether you changed the list in place or made a new one, and why.
2. Turn a dict of student scores into a leaderboard where tied students share a rank and the next rank is not skipped, with ties alphabetical. Then explain why a dict or a tuple can't be reordered in place, and what stability means **(trap)**.

**Hints**
1. A key that returns a tuple, with a minus sign on the numbers that must go descending, and `lower()` on the name
2. `sorted` on the dict's items with a key, and a running rank counter

For each question, write the approach in words first, then code it, then write your pattern, trick, time, and space note. Paste your attempt or just your approach and I'll check it. I can also give you test data for any question.