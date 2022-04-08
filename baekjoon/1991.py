import sys
input = sys.stdin.readline


tree = {}
for _ in range(int(input())):
    root, left, right = input().split()
    tree[root] = [left, right]

def preorder(v):
    print(v, end="")
    if tree[v][0] != ".":
        preorder(tree[v][0])
    if tree[v][1] != ".":
        preorder(tree[v][1])
def inorder(v):
    if tree[v][0] != ".":
        inorder(tree[v][0])
    print(v, end="")
    if tree[v][1] != ".":
        inorder(tree[v][1])
def postorder(v):
    if tree[v][0] != ".":
        postorder(tree[v][0])
    if tree[v][1] != ".":
        postorder(tree[v][1])
    print(v, end="")
preorder('A')
print()
inorder('A')
print()
postorder('A')
