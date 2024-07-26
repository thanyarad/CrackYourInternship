class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Function to perform DFS
        def dfs(x, y, word_index):
            # Check if we have found the entire word
            if word_index == len(word):
                return True
            # Check boundaries and if the current cell matches the current word character
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] != word[word_index]:
                return False
            
            # Save the current cell character and mark it as visited
            temp = board[x][y]
            board[x][y] = '#'
            
            # Explore all four possible directions: up, down, left, right
            found = (dfs(x + 1, y, word_index + 1) or 
                     dfs(x - 1, y, word_index + 1) or 
                     dfs(x, y + 1, word_index + 1) or 
                     dfs(x, y - 1, word_index + 1))
            
            # Restore the current cell character
            board[x][y] = temp
            
            return found
        
        # Iterate over each cell in the board
        for i in range(len(board)):
            for j in range(len(board[0])):
                # Start a DFS search from the current cell
                if dfs(i, j, 0):
                    return True
        
        return False