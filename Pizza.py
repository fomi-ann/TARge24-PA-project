import uuid


class Pizza:

        self.id = str(uuid.uuid4())


    def __eq__(self, other):
        return isinstance(other, Pizza) and self.id == other.id