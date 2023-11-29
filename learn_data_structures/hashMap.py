class HashMap:
    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def __repr__(self):
        buckets = []
        for i, v in enumerate(self.hashmap):
            if v != None:
                buckets.append(f"{str(v)} @ {i}")
        return str(buckets)

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)

    def insert(self, key, value):
        i = self.key_to_index(key)
        self.hashmap[i] = (key, value)

    def get(self, key):
        i = self.key_to_index(key)
        bucket = self.hashmap[i]
        if bucket is None:
            raise Exception("sorry, key not found")
        return bucket[1]
