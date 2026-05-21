from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for row in range(9):
            for column in range(9):
                value = board[row][column]
                if value == ".":
                    # Considered blank
                    continue
                
                # Use tuple to track box, (x, y) -- //N groups things into buckets of size N.
                box_id = (row // 3, column // 3)

                # Does value already exist?
                if value in rows[row]:
                    return False
                
                if value in cols[column]:
                    return False
                
                if value in boxes[box_id]:
                    return False
                
                # Store value in the sets

                rows[row].add(value)
                cols[column].add(value)
                boxes[box_id].add(value)
        return True