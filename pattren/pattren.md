Right now your pattern is "solve, then move on." The fix is to add a short loop around each problem. Here's one you can follow every day:

**The 5-step loop (per problem)**

1. **Understand (3-5 min).** Before any code, write the input and output for one small example by hand, and one edge case (empty list, one item, duplicates).
2. **Brute force first (5-10 min).** Write the simple, slow solution in plain words or code. A working slow solution beats a stuck fast one.
3. **Ask "what is slow?" (5 min).** Find the repeated work, then ask which tool removes it: a set/dict for lookups, two pointers, a sliding window, sorting. This is the step you were missing on the consecutive-sequence problem.
4. **Code it and trace it.** Run it on your example by hand, like you did in your last message. Your tracing is already good, so keep doing it.
5. **Write a 3-line note.** Pattern name, the trick in one sentence, and the time complexity.

**Time limit:** if you are stuck after 20-30 minutes, ask for a hint about the *idea* only, then write the code yourself.

**Weekly rhythm**

1. Mon-Fri: new problems (1 JS + 1 Python).
2. Saturday: redo 2-3 problems from earlier in the week with no hints.
3. Sunday: rest, or reread your pattern notes only.

**Keep a pattern notebook.** One line per problem, grouped by pattern, like:

```text
# Set/hash lookup: replace a nested loop with O(1) membership checks
- Longest consecutive sequence: only start at num where num-1 not in set
```

After 30-40 problems, this notebook is what makes new problems feel familiar, because you will start matching them to patterns you have already written down.

If you want, send me your next problem and I'll walk you through steps 1-3 with questions only, without giving the answer, so you can practice the thinking part.