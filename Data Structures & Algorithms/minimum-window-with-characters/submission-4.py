class Solution:

  def minWindow(self, s: str, t: str) -> str:
    # If t is longer than s, it's impossible to contain all characters
    if len(t) > len(s):
      return ""

    lst = []
    for ch in range(len(s)):
      if s[ch] in t:
        lst.append([ch, s[ch]])

    lst.sort()

    minWindow = float("inf")
    windowStr = []

    for i in range(len(lst)):
      for j in range(i, len(lst)):
        current_chars = [lst[k][1] for k in range(i, j + 1)]

        # Check if the frequency of each character in t is satisfied
        from collections import Counter

        t_count = Counter(t)
        curr_count = Counter(current_chars)

        valid = all(curr_count[char] >= t_count[char] for char in t_count)

        if valid:
          if minWindow > (lst[j][0] - lst[i][0]):
            minWindow = lst[j][0] - lst[i][0]
            windowStr = [lst[i][0], lst[j][0]]
          break

    if not windowStr:
      return ""

    return s[windowStr[0] : windowStr[1] + 1]