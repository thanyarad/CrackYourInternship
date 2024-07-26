import random
from collections import defaultdict

class RandomizedCollection:

    def __init__(self):
        self.elements = []
        self.idx_map = defaultdict(set)

    def insert(self, val: int) -> bool:
        self.elements.append(val)
        self.idx_map[val].add(len(self.elements) - 1)
        return len(self.idx_map[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.idx_map[val]:
            return False
        remove_idx = self.idx_map[val].pop()
        last_val = self.elements[-1]
        self.elements[remove_idx] = last_val
        self.idx_map[last_val].add(remove_idx)
        self.idx_map[last_val].discard(len(self.elements) - 1)
        self.elements.pop()
        if not self.idx_map[val]:
            del self.idx_map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.elements)

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
