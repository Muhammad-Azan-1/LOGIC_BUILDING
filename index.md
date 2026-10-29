# Hard practice questions (2 per topic)

Try them without running the code first, then verify.

## 1. `append` / `extend` / `insert`
1. `a = [1, 2]; a.append(a)`. What does `print(a)` show, and what do `len(a)` and `a[2][2][0]` give? Why doesn't it loop forever?
2. Predict the final `x`:
   ```python
   x = [1, 2, 3]
   x.extend(x)
   x.insert(len(x), x[:2])
   x.insert(-1, 'z')
   ```

## 2. `remove` / `pop` / `clear`
1. Predict the result of this loop on `[1, 1, 2, 1, 3, 1]`, explain why it's wrong, then fix it in place (no new list):
   ```python
   for i in lst:
       if i == 1:
           lst.remove(i)
   ```
2. **Josephus problem:** 7 people stand in a circle numbered 1 to 7. Starting from person 1, every 3rd person is eliminated. Using only `pop(index)` and modulo arithmetic, return the elimination order.

## 3. `count` / `index`
1. For `[1, 2, 3, "Azan", 3, 2, 1, True, "Azan", True]`, predict `count(1)`, `count(True)` and `index(True)`. Why are the answers surprising?
2. Write `find_all(lst, x)` that returns every index of `x` using only `index()` with its `start` argument (no `enumerate`, no loop over indices). Handle the `ValueError`.

## 4. `copy` (shallow vs. deep)
1. Predict `a` and `b` after this, and explain the two layers of shared references. Then show the correct way to build a 3×3 grid.
   ```python
   a = [[0] * 3] * 3
   b = a.copy()
   a[0][0] = 5
   ```
2. Write `my_deepcopy(lst)` for arbitrarily nested lists, without the `copy` module, and prove it works with a test.

## 5. `reverse`
1. Predict the output:
   ```python
   a = [1, 2, 3]
   b = a.reverse()
   print(b)
   d = reversed(a)
   print(list(d), list(d))
   ```
2. Reverse a list in place with a two-pointer approach (no `reverse()`, slicing or `reversed`). Then extend it to reverse only the segment between indices `i` and `j`.

## 6. `sort()`
1. Sort `["Azan", "zayyan", "muhammad", "raza", "huzaif", "anus"]` by length descending, with ties broken alphabetically ascending, in a single `sort()` call.
2. Sort integers by their number of `1` bits in binary, ties by value descending. Then explain why sorting twice (secondary key first, primary key second) also works. What property guarantees that?

## 7. `sorted()`
1. Given `{"a": 3, "b": 1, "c": 3, "d": 2}`, return the keys ordered by value descending, ties by key ascending, using `sorted()`.
2. Sort the characters of `"mississippi"` by frequency descending, ties alphabetical, and return a string. Use `sorted()` and one other tool of your choice.

## 8. List comprehension basics
1. Generate all Pythagorean triples `(a, b, c)` with `a < b < c <= 50` in one comprehension.
2. Given `m = [[1,2,3],[4,5,6],[7,8,9]]`, produce the flattened list and the transpose, each in one comprehension.

## 9. Nested / multi-loop comprehensions
1. Predict the output without running it (it's from your notes):
   ```python
   li = [2, 3, 9]
   li = [[x for x in [li]] for x in range(3)]
   ```
   Then explain what `[i+j for i in 'abc' for j in 'def']` gives versus `[[i+j for i in 'abc'] for j in 'def']`.
2. Using one comprehension, produce all pairs `(i, j)` with `0 <= i < j < 5` where `i + j` is odd. Then rewrite it as equivalent nested `for` loops.

## 10. Filter (`if`) vs. ternary (`if/else`)
1. From `data = [10, -5, None, 8, -2, None, "7"]`, in one comprehension: drop `None`, convert numeric strings to `int`, and clamp negatives to `0`.
2. Write FizzBuzz for 1 to 30 as a single comprehension with a chained ternary. Then explain why `[x for x in data if x > 0 else 0]` is a `SyntaxError`.

---

Send me your answers whenever you're ready and I'll check them, or ask for hints on any one.

I also spotted two small slips in your notes:
- In section 1.3, the printed comment for `list_3` doesn't match the code. The last `insert(0, 1)` puts `1` at the front.
- In section 2.2, the second `print(removed_item)` should be `print(removed_item_2)`, which is why your comment says `False` but the code would print `True`.