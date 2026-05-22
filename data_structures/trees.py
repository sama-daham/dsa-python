class Node:
   def __init__(self, val):
      self.val = val
      self.left = None
      self.right = None

class BST:
    #not self-balancing like avl - that'd require tracking balance factor and updating w/changes
    def __init__(self):
        self.root = None
    
    def insert(self,val):
        new_node = Node(val)
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        while True:
            if val == current.val:
                return
            elif val<current.val:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right
       
        
   
    def search(self, val):
        current_node = self.root
        while current_node is not None:
            if current_node.val == val:
                return True
            elif current_node.val>val:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return False

   
    def delete(self, val):
        if self.search(val):
            self.root = self._delete(self.root,val)
        else:
            raise KeyError("Value does not exist in tree")
    
    def _delete(self, node, val):
        if node is None:
            return None
        if val<node.val:
            node.left = self._delete(node.left,val)
        elif val>node.val:
            node.right = self._delete(node.right,val)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor = node.right
                while successor.left is not None:
                    successor = successor.left
                node.val = successor.val
                node.right = self._delete(node.right, successor.val)
        return node
   
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node is None:
            return
        self._inorder(node.left, result)
        result.append(node.val)
        self._inorder(node.right, result)

    def preorder(self):
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, node, result):
        if node is None:
            return
        result.append(node.val)
        self._preorder(node.left, result)
        self._preorder(node.right, result)

    def postorder(self):
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, node, result):
        if node is None:
            return
        self._postorder(node.left, result)
        self._postorder(node.right, result)
        result.append(node.val)