class Solution:
    def isValid(self, s: str) -> bool:
        valid = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        close = []

        for i in s:
            if i in valid:
                # Add to close
                close.append(valid[i])
            elif len(close) > 0:
                # Remove and grab from end
                close_bracket = close.pop()
                if close_bracket != i:
                    return False
            else:
                return False
        # If anything left to close, false
        return False if close else True