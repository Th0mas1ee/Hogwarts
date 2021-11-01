class HashTable:
    def __init__(self):
        self.table_size = 10007
        self.table = [0] * self.table_size

    def __contains__(self, item):
        return self.has_key(item)

    def _hash(self, s):
        n = 0
        f = 1
        for i in s:
            n += ord(i) * f
            f *= 10
        return n

    def _index(self, key):
        return self._hash(key) & self.table_size

    def _insert_at_index(self, index, key, value):
        v = self.table[index]
        data = [key, value]
        if isinstance(v, int):
            self.table[index] = [data]
        else:
            self.table[index].append([data])

    def has_key(self, key):
        index = self._index(key)
        v = self.table[index]
        if isinstance(v, list):
            for kv in v:
                if kv[0] == key:
                    return True
        return False

    def add(self, key, value):
        index = self._index(key)
        self._insert_at_index(index, key, value)

    def get(self, key, default_value=None):
        index = self._index(key)
        v = self.table[index]
        if isinstance(v, list):
            for kv in v:
                if kv[0] == key:
                    return kv[1]
        return default_value


def test():
    import uuid
    names = [
        'gua',
        'xiao',
        'name',
        'web',
        'python',
    ]
    ht = HashTable()
    for key in names:
        value = uuid.uuid4()
        ht.add(key, value)
        print('add 元素', key, value)
    for key in names:
        v = ht.get(key)
        print('get 元素', key, v, f'_hash: {bin(ht._hash(key))}; _index: {bin(ht._index(key))}')

    # print(f'_hash: {ht._hash("gua")}; _index: {ht._index("gua")}')
    print(int('111111111111111', 2), bin(10007))

if __name__ == '__main__':
    test()