class Customer():

    def __init__(self,name,id):
        self._name = name
        self._id = id

    @property
    def id(self):
        return self._id

    def __str__(self):
        return "customer: <name: {}, id: {}>".format(self._name, self._id)