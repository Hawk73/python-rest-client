class CollectionClass:
    def __init__(self, items, params):
        self.items = items
        self.params = params

    def items(self):
        return self.items

    def params(self):
        return self.params

    def delete_all(self):
        while len(self.items) > 0:
            item = self.items.pop()
            item.delete()
        return True

    def first(self):
        if len(self.items) > 0:
            return self.items[0]
        else:
            return None
