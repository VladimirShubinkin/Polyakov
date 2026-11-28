from io import StringIO
import sys
import os

from test import *  # импортируем проверяемую функцию/класс из нужного модуля

folder = 'tests_11242425'  # папка с тестовыми файлами
files_count = len(os.listdir(f'{folder}')) // 2
for i in range(1, files_count + 1):
    with open(f'{folder}/{i}') as fin, open(f'{folder}/{i}.clue') as fout:
        tmp_stdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        exec(fin.read())
        sys.stdout = tmp_stdout
        ans = result.getvalue().strip()
        clue = fout.read().strip()
        if ans != clue:
            print(i, ans, clue)
