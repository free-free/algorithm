# -*- coding:utf-8 -*-

import numpy as np


class Node(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_binary_tree(vals):
    root = Node(vals[0])
    for val in vals[1:]:
        pre = root
        cur = root
        node = Node(val)
        while cur:    
            pre = cur
            if val < cur.val:
                cur = cur.left
            else:
                cur = cur.right
        if val < pre.val:
            pre.left = node
        else:
            pre.right = node
    return root

def pre_traverse(node):
    if not node:
        return 
    print(node.val)
    pre_traverse(node.left)
    pre_traverse(node.right)

def in_traverse(node):
    if not node:
        return 
    in_traverse(node.left)
    print(node.val)
    in_traverse(node.right)

def post_traverse(node):
    if not node:
        return 
    post_traverse(node.left)
    post_traverse(node.right)
    print(node.val)

def traverse_by_layer(root):
    ret = []
    q = []
    if root:
        q.append(root)
    while len(q) > 0 :
        tmp = q[0]
        ret.append(tmp.val)
        if tmp.left:
            q.append(tmp.left)
        if tmp.right:
            q.append(tmp.right)
        q = q[1:]
    print(ret)

def print_by_layer(root):
    ret = []
    q = []
    child_sz = 0
    parent_sz = 1
    if root:
        q.append(root)
    while len(q) > 0 :
        tmp = q[0]
        ret.append(tmp.val)
        if tmp.left:
            q.append(tmp.left)
            child_sz += 1
        if tmp.right:
            q.append(tmp.right)
            child_sz += 1
        q = q[1:]
        parent_sz -= 1
        if parent_sz == 0:
            parent_sz = child_sz
            child_sz = 0
            print(ret)
            ret = []

if __name__ == '__main__':
    data = np.random.randint(0, 100, 10)
    print(data)
    btree = build_binary_tree(data)
    print('pre traversal')
    pre_traverse(btree)
    print('in traversal')
    in_traverse(btree)
    print('post traversal')
    post_traverse(btree)
    print('layer traversal')
    traverse_by_layer(btree)
    print_by_layer(btree)

    


    

