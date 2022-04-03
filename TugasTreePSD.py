class Node:
    def __init__(self, value=None):
        self.value = value
        self.right = None
        self.left = None

    # getter setter value
    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    # getter setter left dan right
    def set_right_child(self, node):
        self.right = node
  
    def set_left_child(self, node):
        self.left = node
  
    def get_right_child(self):
        return self.right

    def get_left_child(self):
        return self.left
    
    # check has child function
    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.  right != None
    
class Tree:
    def __init__(self, node):
        self.root = node
        
    def get_root(self):
        return self.root

def preorder(startnode, visit_order):
    if startnode:
    # visit_order --> tempat penyimpanan berupa string
        visit_order = visit_order + startnode.get_value() + " "
        if startnode.has_left_child():
            visit_order = preorder(startnode.get_left_child(), visit_order) # terjadi rekursi
        if startnode.has_right_child():
            visit_order = preorder(startnode.get_right_child(), visit_order) # terjadi rekursi
    return visit_order

def inorder(startnode, visit_order):
    if startnode:
        if startnode.has_left_child():
            visit_order = inorder(startnode.get_left_child(), visit_order) # terjadi rekursi
        visit_order = visit_order + startnode.get_value() + " "
        if startnode.has_right_child():
            visit_order = inorder(startnode.get_right_child(), visit_order) # terjadi rekursi
    return visit_order
            
def postorder(startnode, visit_order):
    if startnode:
        if startnode.has_left_child():
            visit_order = postorder(startnode.get_left_child(), visit_order) # terjadi rekursi
        if startnode.has_right_child():
            visit_order = postorder(startnode.get_right_child(), visit_order) # terjadi rekursi
        visit_order = visit_order + startnode.get_value() + " "
    return visit_order


# membuat objek node
ni = Node("Ni")
ki = Node("Ki")
hi = Node("Hi")
da = Node("Da")
ya = Node("Ya")
ti = Node("Ti")

# ketentuan soal: kata dengan abjad terkecil sebagai root, ("Da")
#                 kata dengan abjad terkecil kedua sebagai left child level 1("Hi")
#                 kata dengan abjad terkecil ketiga sebagai right child level 1 ("Ki")

# membuat objek Tree
myTree = Tree(da)
# tree level 1
myTree.get_root().set_left_child(hi)
myTree.get_root().set_right_child(ki)
# tree level 2
myTree.get_root().get_right_child().set_right_child(ni)
# tree level 3
myTree.get_root().get_right_child().get_right_child().set_right_child(ya)
# tree level 4
myTree.get_root().get_right_child().get_right_child().get_right_child().set_left_child(ti)

# visualisasi tree:
#   Da
#  /  \
# Hi   Ki
#       \
#        Ni
#         \
#         Ya
#         /
#        Ti    

# print values
print(preorder(myTree.get_root(), ""))
print(inorder(myTree.get_root(), ""))
print(postorder(myTree.get_root(), ""))
