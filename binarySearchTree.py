class Node : 
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def insert (root, data):
    if root is None:
        root = Node(data)
    else:
        if data < root.data:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
    return root
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

arr = [7, 5, 1, 8, 3, 6, 0, 9, 4, 2]
root = None
for i in range(len(arr)):
    root = insert(root, arr[i])
inorder(root)
