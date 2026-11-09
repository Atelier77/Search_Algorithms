nums = [1, 8, 4, 12, 9, 3, 7, 5, 6, 10]


#класс узла/вершины дерева
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def search(self, target):
        node = self
        while node:
            if target == node.val:
                return node
            node = node.left if target < node.val else node.right
        return None

    def contains(self, target):
        return self.search(target) is not None

    def insert(self, val):
        if val < self.val:
            if self.left is None:
                self.left = TreeNode(val)
            else:
                self.left.insert(val)
        elif val > self.val:
            if self.right is None:
                self.right = TreeNode(val)
            else: self.right.insert(val)
        return self

    def delete(self, val):
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.val:
            if self.right:
                self.right = self.right.delete(val)

        else:
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            #Если есть 2 узла-ребёнка
            succesor = self.right._min_node()
            self.val = succesor.val
            self.right = self.right.delete(succesor.val)

        return self

    def _min_node(self):
        node = self
        while node.left:
            node = node.left
        return node

    def _max_node(self):
        node = self
        while node.right:
            node = node.right
        return node

#Функция представления отсортированного массива в виде бинарного(не самобалансируюещегося) дерева поиска
def sortedArrayToBST(nums):

    
    def helper(left, right):
        if left > right:
            return None

        mid = (left + right) // 2
        root = TreeNode(nums[mid])

        root.left = helper(left, mid - 1)
        root.right = helper(mid + 1, right)

        return root

    return helper(0, len(nums) - 1)


#сложный алгортим сортировки
def HeapSort(nums):

    n = len(nums)

    #просеивание элемента массива
    def sift_down(array, start, end):

        if start >= end:
            return None
        max_trio = array[start]
        max_index = start

        if start*2 + 1 <= end and array[start*2 + 1] > max_trio:
            max_trio = array[start*2 + 1]
            max_index = start*2 + 1

        if start*2 + 2 <= end and array[start*2 + 2] > max_trio:
            max_trio = array[start*2 + 2]
            max_index = start*2 + 2

        if max_index != start:
            array[start], array[max_index] = array[max_index], array[start]
            sift_down(array, max_index, end)

    #O(n) на формирование макс_кучи
    for s in range(n // 2 - 1, -1, -1):
        sift_down(nums, s, n - 1)

    #O(n * logn) на конечный отсортированный массив
    for end in range(n - 1, 0, -1):
        nums[0], nums[end] = nums[end], nums[0]
        sift_down(nums, 0, end - 1)

    return nums


nums_sorted = HeapSort(nums)
BST = sortedArrayToBST(nums)

print(HeapSort(nums))


#ПРОВЕРКА выводом дерева в виде отсортированного массива

# def inorder(node):
#     if not node:
#         return []
#     return inorder(node.left) + [node.val] + inorder(node.right)

# print(inorder(BST))

def print_tree(node, prefix="", is_tail=True):
    if node is None:
        return

    if node.right:
        print_tree(node.right, prefix + ("│   " if is_tail else "    "), False)
    print(prefix + ("└── " if is_tail else "┌── ") + str(node.val))
    if node.left:
        print_tree(node.left, prefix + ("    " if is_tail else "│   "), True)

print_tree(BST)

#Проверка поиска, вставки и удаления
print(BST.contains(7))
print_tree(BST.insert(2))
print_tree(BST.delete(6))
