class parent:
    def __init__(self, name):
        print('Parent __init__', name)
class parent2:
    def __init__(self, id):
        print('Parent2__init', id)
class child(parent, parent2):
    def __init__(self):
        print('Child __init__')
        parent.__init__(self,'max')
        parent2.__init__(self,'12')
Child = child()
