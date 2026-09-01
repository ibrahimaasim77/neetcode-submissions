class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = {}
        cols = {}
        boxes = {}

        for r in range(9):
            for c in range(9):

                num = board[r][c]

                # Ignore empty spaces
                if num == ".":
                    continue

                # Check row
                if r not in rows:
                    rows[r] = set()

                if num in rows[r]:
                    return False

                rows[r].add(num)

                # Check column
                if c not in cols:
                    cols[c] = set()

                if num in cols[c]:
                    return False

                cols[c].add(num)

                # Find which 3x3 box we're in
                box = (r // 3, c // 3)

                if box not in boxes:
                    boxes[box] = set()

                if num in boxes[box]:
                    return False

                boxes[box].add(num)

        return True