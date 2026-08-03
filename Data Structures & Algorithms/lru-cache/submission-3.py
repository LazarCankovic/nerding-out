class LRUCache:

    def __init__(self, capacity: int):
        self.my_dict = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.my_dict:
            return -1
        self.my_dict.move_to_end(key)
        return self.my_dict[key]

    def put(self, key: int, value: int) -> None:
        if key in self.my_dict:
            self.my_dict.move_to_end(key)
        self.my_dict[key] = value
        if self.capacity < len(self.my_dict):
            self.my_dict.popitem(last=False)