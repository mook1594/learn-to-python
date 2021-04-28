class Folder:
    def __init__(self, name):
        self.name = name
        self.children = {}

    def add_child(self, child):
        pass

    def move(self, new_path):
        pass

    def copy(self, new_path):
        pass

    def delete(self):
        pass

class File:
    def __init__(self, name, contents):
        self.name = name
        self.contents = contents

    def move(self, new_path):
        pass

    def copy(self, new_path):
        pass

    def delete(self):
        pass

class Component:
    def __init__(self, name):
        self.name = name

    def move(self, new_path):
        new_folder = get_path(new_path)
        del self.parent.children[self.name]
        new_folder.child[self.name] = self
        self.parent = new_folder

    def delete(self):
        del self.parent.children[self.name]

class Folder(Component):
    def __init__(self, name):
        super().__init__(name)
        self.children = {}

    def add_child(self, child):
        pass

    def copy(self, new_path):
        pass

class File(Component):
    def __init__(self, name, contents):
        super().__init__(name)
        self.contents = contents

    def copy(self, new_path):
        pass

root = Folder('')
def get_path(path):
    names = path.split('/')[1:]
    node = root
    for name in names:
        node = node.children[name]
    return node

def add_child(self, child):
    child.parent = self
    self.children[child.name] = child

folder1 = Folder('folder1')
folder2 = Folder('folder2')
root.add_child(folder1)
root.add_child(folder2)
folder11 = Folder('folder11')
folder1.add_child(folder11)
file111 = File('file111', 'contents')
folder11.add_child(file111)
file21 = File('file21', 'other contents')
folder2.add_child(file21)
folder2.children
folder2.move('/folder1/folder11')
folder11.children
file21.move('/folder1')
folder1.children


