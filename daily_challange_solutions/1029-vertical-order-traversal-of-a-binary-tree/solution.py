from collections import deque
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        # map: hd -> list of (row, val)
        map = {}
        # queue holds triples: (node, hd, row)
        queue = deque([(root, 0, 0)])

        while queue:
            node, hd, row = queue.popleft()
            # collect (row, value) instead of just value
            temp = map.get(hd, [])
            temp.append((row, node.val))
            map[hd] = temp

            if node.left:
                # left child is one level deeper (row+1), hd-1
                queue.append((node.left, hd - 1, row + 1))

            if node.right:
                # right child is one level deeper (row+1), hd+1
                queue.append((node.right, hd + 1, row + 1))

        # Now sort each list of (row, val) by row first, then val
        final = []
        for i in sorted(map.keys()):
            entries = map[i]  # this is a list of (row, val)
            entries.sort(key=lambda x: (x[0], x[1]))
            # extract just the values in sorted order
            col_vals = [val for (_, val) in entries]
            final.append(col_vals)

        return final

