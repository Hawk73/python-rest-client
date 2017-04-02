class CollectionClass:
    def __init__(self, items, params):
        self.items = items
        self.params = params
        self.cursor = 0

    def items(self):
        return self.items

    def params(self):
        return self.params

    def delete_all(self):
        self.cursor = 0
        while len(self.items) > 0:
            item = self.items.pop()
            item.delete()
        return True

    def first(self):
        self.cursor = 0
        if len(self.items) > 0:
            return self.items[0]
        else:
            return None

    # TODO: Add tests
    def iter(self):
        if self.cursor + 1 < len(self.items):
            self.cursor += 1
            return self.items[self.cursor]
        else:
            return None
