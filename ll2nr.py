from nodesrefs import BinaryTree


def ll2nr(l):
    """
    """

    if len(l) == 0:
        return BinaryTree(None)
    elif type(l[2]) != type([]) or type(l[1]) != type([]) or len(l) != 3:
        raise ValueError("Given list is not a Binary Tree List")
    else:
        T = BinaryTree(l[0])
        lchild = l[1]
        rchild = l[2]
        if len(lchild) != 0:
            T.insertLeftChild(lchild)
        if len(rchild) != 0:
            T.insertRightChild(rchild)
        if conditions(lchild, rchild):
            T.setLeftSubtree(ll2nr(lchild))
            T.setRightSubtree(ll2nr(rchild))
        return T


def conditions(l, r):
    if len(l) == 0:
        l = None
    if len(r) == 0:
        r = None
    return l is not None or r is not None


