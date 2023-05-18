import colorama
import inspect

# Використовуємо функцію inspect для отримання інформації про модуль colorama
module_info = inspect.getmembers(colorama)

# Функції та атрибути, які бажаємо виділити
highlighted_functions = ['init', 'Fore', 'Back', 'Style', 'init_autoreset', 'init_wrapped']

# Виводимо результати інтроспекції
for name, obj in module_info:
    if name in highlighted_functions:
        print(f"Name: {name}")
        print(f"Type: {type(obj)}")
        print(f"Documentation: {inspect.getdoc(obj)}")
        print()
