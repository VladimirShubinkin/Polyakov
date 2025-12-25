def max(*args, **kwargs):
    raise NameError('В этой задаче запрещено использование функции max()')

def min(*args, **kwargs):
    raise NameError('В этой задаче запрещено использование функции min()')

def sum(*args, **kwargs):
    raise NameError('В этой задаче запрещено использование функции sum()')

def bin(*args, **kwargs):
    raise NameError('В этой задаче запрещено использование функции bin()')

def len(*args, **kwargs):
    raise NameError('В этой задаче запрещено использование функции len()')

def str(*args, **kwargs):
    raise NameError('В этой задаче запрещено использование функции str()')

def sorted(*args, **kwargs):
    raise NameError('В этой задаче запрещено использование функции sorted()')

class list:
    raise NameError('В этой задаче запрещено использовние списков')

# запрет импорта
import sys

class ImportTracker:
    def find_spec(self, fullname, path, target=None):
        raise NameError('Решите задачу без использования готовых функций')


sys.meta_path.insert(0, ImportTracker())

