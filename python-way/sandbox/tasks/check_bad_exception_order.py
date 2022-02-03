"""
task link: https://stepik.org/lesson/24463/step/7?thread=solutions&unit=6771

Вам дано описание наследования классов исключений в следующем формате.
<имя исключения 1> : <имя исключения 2> <имя исключения 3> ... <имя исключения k>
Это означает, что исключение 1 наследуется от исключения 2, исключения 3, и т. д.

Формат входных данных
В первой строке входных данных содержится целое число n - число классов исключений.
В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов наследуется i-й класс.
Обратите внимание, что класс может ни от кого не наследоваться. 
Гарантируется, что класс не наследуется сам от себя (прямо или косвенно), что класс не наследуется явно от одного класса более одного раза.
В следующей строке содержится число m - количество обрабатываемых исключений.
Следующие m строк содержат имена исключений в том порядке, в каком они были написаны у Антона в коде.
Гарантируется, что никакое исключение не обрабатывается дважды.

Формат выходных данных
Выведите в отдельной строке имя каждого исключения, обработку которого можно удалить из кода, не изменив при этом поведение программы. 
Имена следует выводить в том же порядке, в котором они идут во входных данных.
"""

class_except_tree = {}
for _ in range(int(input())):
    tree = input().split()
    class_except_tree[tree[0]] = [] if len(tree) == 1 else tree[2:]


class_except_order = []
for _ in range(int(input())):
    class_except_order.append(input())


def check_independence(target_group, parents):
    if not parents:
        return False
    if set(target_group).intersection(set(parents)):
        return True
    return any([
        check_independence(target_group, class_except_tree.get(parrent, []))
        for parrent in parents
    ])


for idx, except_class in enumerate(class_except_order):
    if check_independence(class_except_order[:idx], class_except_tree.get(except_class, [])):
        print(except_class)
        