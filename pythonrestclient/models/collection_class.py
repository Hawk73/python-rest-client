class CollectionClass:
    def __init__(self, items):
        self.items = items

    def items(self):
        self.items

    def delete_all(self):
        for item in self.items:
            self.delete(item['id'])

    def delete(self, id):
        if self.items[id]:
            return self.items[id].delete()
        else:
            return True
