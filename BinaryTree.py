from collections import deque


# Creating nodes of binary tree
class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return repr(self.val)


# All the operations of BTree defined in this class
class BinaryTree:
    def __init__(self):
        self.root = None

    # Inserting elements in BTree
    def insert(self, val):
        if not self.root:
            self.root = Node(val=val)
            return
        dq = deque()
        dq.append(self.root)
        while dq:
            curr = dq.popleft()
            if not curr.left:
                curr.left = Node(val=val)
                break
            else:
                dq.append(curr.left)
            if not curr.right:
                curr.right = Node(val=val)
                break
            else:
                dq.append(curr.right)

    # Deleting the deepest or rightmost node of BTree
    def delete_deepest_node(self, deepest_node):
        dq = deque()
        dq.append(self.root)
        while dq:
            curr = dq.popleft()
            if curr is deepest_node:
                curr = None
                return
            if curr.right:
                if curr.right is deepest_node:
                    curr.right = None
                    return
                else:
                    dq.append(curr.right)
            if curr.left:
                if curr.left is deepest_node:
                    curr.left = None
                    return
                else:
                    dq.append(curr.left)

    # Deleting the required node from BTree
    def delete(self, key):
        if not self.root:
            print('Binary tree is empty')
            return
        if not self.root.left and not self.root.right:
            if self.root.val == key:
                self.root = None
                return
            else:
                print(f'{key} not in the binary tree')
                return
        dq = deque()
        dq.append(self.root)
        req_key_node = None
        curr = None
        while dq:
            curr = dq.popleft()
            if curr.val == key:
                req_key_node = curr
            if curr.left:
                dq.append(curr.left)
            if curr.right:
                dq.append(curr.right)
        if req_key_node:
            deepest_val = curr.val
            self.delete_deepest_node(curr)
            req_key_node.val = deepest_val
        else:
            print(f'{key} not in the binary tree')

    # Inorder traversal of BTree
    def inorder(self, curr):
        ans = []
        if curr.left:
            ans = self.inorder(curr.left)
        ans.append(curr)
        if curr.right:
            ans = ans + self.inorder(curr.right)
        return ans

    # Postorder traversal of BTree
    def postorder(self, curr):
        ans = []
        if curr.left:
            ans = self.postorder(curr.left)
        if curr.right:
            ans = ans + self.postorder(curr.right)
        ans.append(curr)
        return ans

    # Preorder Traversal of BTree
    def preorder(self, curr):
        ans = []
        if curr:
            ans.append(curr)
            ans = ans + self.preorder(curr.left)
            ans = ans + self.preorder(curr.right)
        return ans

    # Searching the required element in BTree
    def search(self, key):
        dq = deque()
        dq.append(self.root)
        while dq:
            curr = dq.popleft()
            if curr.val == key:
                print(f'{key} found in the binary tree')
                return
            if curr.left:
                if curr.left.val == key:
                    print(f'{key} found in the binary tree')
                    return
                else:
                    dq.append(curr.left)
            if curr.right:
                if curr.right.val == key:
                    print(f'{key} found in the binary tree')
                    return
                else:
                    dq.append(curr.right)
        print(f'{key} not in binary tree')


# Main function
if __name__ == '__main__':
    bt = BinaryTree()
    bt.insert(10)
    bt.insert(20)
    bt.insert(30)
    bt.insert(50)
    bt.insert(40)
    bt.insert(100)
    print(bt.inorder(bt.root))
    # print(bt.postorder(bt.root))
    # print(bt.preorder(bt.root))
    bt.delete(50)
    print(bt.inorder(bt.root))
    bt.delete(10)
    print(bt.inorder(bt.root))
    bt.delete(30)
    print(bt.inorder(bt.root))
    bt.search(100)
    bt.search(40)
    bt.search(30)
