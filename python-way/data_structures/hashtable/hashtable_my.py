from math import floor, sqrt
from typing import Any, Tuple


class HashTable():
    """
    Hash table implementation.
    Chaining method for saving data.
    Multiplication hash method
    Constant suggested by Knuth: constant = (sqrt(5)-1) / 2 by default
    """

    def __init__(self, size=10, constant_for_hash=None) -> None:
        self.lst = [[] for _ in range(size)]
        self.size = 10
        self.__const_for_hash = constant_for_hash or (sqrt(5) - 1) / 2

    def _hash(self, key: str) -> Tuple[int, int]:
        hash_key = sum([ord(ch) for ch in key])
        index = floor(self.size * ((hash_key * self.__const_for_hash) % 1))
        return (hash_key, index)

    def __setitem__(self, key: str, data: Any) -> None:
        hash_key, index = self._hash(key)
        self.lst[index].append((hash_key, data))
            
    def __getitem__(self, key: str) -> Any:
        hash_key, index = self._hash(key)

        if not self.lst[index]:
            raise KeyError

        for node in self.lst[index]:
            if hash_key == node[0]:
                return node[1]
        else:
            raise KeyError
    
    def __str__(self) -> str:
        res = ""
        template = "{}: (hashkey:{} val:{})\n"
        for id_, chain in enumerate(self.lst):
            for node in chain:
                res += template.format(id_, *node)
        return res[:-1]

if __name__ == "__main__":
    t = HashTable()
    keys = ["aa", "bb", "cc", "dd"]
    for data, key in enumerate(keys, start=2000):
        t[key] = data
    
    for key in keys:
        print(f"key: {key} -> {t[key]}")
    print(t)

    print(t["ttat"])