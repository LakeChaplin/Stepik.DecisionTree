class TreeObj:
    def __init__(self, index, value=None):
        self.index = index
        self.value = value
        self.__left = None
        self.__right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, node):
        if self.__left is None:
            self.__left = node

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, node):
        if self.__right is None:
            self.__right = node


class DecisionTree:
    @classmethod
    def predict(cls, root, x):
        """
        Выполняет прогноз на основе решающего дерева.

        Args:
            root (TreeObj): Корневая вершина решающего дерева.
            x (list): Вектор с бинарными значениями для выполнения прогноза.

        Returns:
            str: Результат прогноза.

        Raises:
            TypeError: Если root не является экземпляром класса TreeObj.
        """
        cls.check_instance(root)

        current_node = root

        while current_node is not None and current_node.value is None:
            if x[current_node.index] == 1:
                current_node = current_node.left
            elif x[current_node.index] == 0:
                current_node = current_node.right

        if current_node is not None and current_node.value is not None:
            return current_node.value
        else:
            return 'Неизвестно'

    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        """
        Добавляет вершину или лист в решающее дерево.

        Args:
            obj (TreeObj): Вершина или лист для добавления.
            node (TreeObj, optional): Вершина, к которой добавляется obj. Если не указана, obj становится корневой вершиной.
            left (bool, optional): Флаг, определяющий, добавлять obj к левой или правой ветви node.

        Returns:
            TreeObj: Добавленный объект obj.

        Raises:
            TypeError: Если obj не является экземпляром класса TreeObj.
        """
        cls.check_instance(obj)

        if node is None:
            return obj
        if left:
            node.left = obj
        else:
            node.right = obj
        return obj

    @classmethod
    def check_instance(cls, obj):
        """
        Проверяет, является ли объект экземпляром класса TreeObj.

        Args:
            obj: Объект для проверки.

        Raises:
            TypeError: Если obj не является экземпляром класса TreeObj.
        """
        if not isinstance(obj, TreeObj):
            raise TypeError('Object must be an instance of TreeObj')


assert hasattr(DecisionTree, 'add_obj') and hasattr(DecisionTree,
                                                    'predict'), "в классе DecisionTree должны быть методы add_obj и predict"

assert type(TreeObj.left) == property and type(
    TreeObj.right) == property, "в классе TreeObj должны быть объекты-свойства left и right"

root = DecisionTree.add_obj(TreeObj(0))
v_11 = DecisionTree.add_obj(TreeObj(1), root)
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
DecisionTree.add_obj(TreeObj(-1, "программист"), v_11)
DecisionTree.add_obj(TreeObj(-1, "кодер"), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "посмотрим"), v_12)
DecisionTree.add_obj(TreeObj(-1, "нет"), v_12, False)
result = DecisionTree.predict(root, [1, 1, 0])
#print(result)
assert DecisionTree.predict(root, [1, 1, 0]) == 'программист', "неверный вывод решающего дерева"
assert DecisionTree.predict(root, [0, 1, 0]) == 'нет', "неверный вывод решающего дерева"
assert DecisionTree.predict(root, [0, 1, 1]) == 'посмотрим', "неверный вывод решающего дерева"
