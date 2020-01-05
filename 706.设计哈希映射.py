#
# @lc app=leetcode.cn id=706 lang=python3
#
# [706] 设计哈希映射
#

# @lc code=start
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.length = 10000
        self.hashmap = [[] for _ in range(self.length)]
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        t = key % self.length
        for i in range(len(self.hashmap[t])):
            index, v = self.hashmap[t][i]
            if index == key:
                self.hashmap[t][i] = (key, value)
                return
        self.hashmap[t].append((key, value))
        return


    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        t = key % self.length
        for i in range(len(self.hashmap[t])):
            index, v = self.hashmap[t][i]
            if index == key:
                return v
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        t = key % self.length
        for i in range(len(self.hashmap[t])):
            index, v = self.hashmap[t][i]
            if index == key:
                del self.hashmap[t][i]
                return
        return
                
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end

