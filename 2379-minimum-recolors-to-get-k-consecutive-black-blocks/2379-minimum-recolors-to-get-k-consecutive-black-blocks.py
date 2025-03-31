class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        win = Counter(blocks[:k])
        l = 0
        min_op = win['W']
        for r in range(k, len(blocks)):
            if blocks[r] in win:
                win[blocks[r]] += 1
            else:
                win[blocks[r]] = 1
            if win[blocks[l]] == 1:
                del win[blocks[l]]
            else:
                win[blocks[l]] -= 1
            l += 1
            min_op = min(min_op, win['W'])
        return min_op

            

        