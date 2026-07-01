class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        # Edge case
        if not digits:
            return []

        # Digit to letters mapping
        digitMap = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        result = []
        cur = []

        def dfs(i):
            # Base Case
            # We've processed all digits
            if i == len(digits):
                result.append("".join(cur))
                return

            # Iterate through all letters corresponding to current digit
            for ch in digitMap[digits[i]]:

                # Choose
                cur.append(ch)

                # Explore next digit
                dfs(i + 1)

                # Undo choice (Backtrack)
                cur.pop()

        dfs(0)

        return result