# Эксперимент с tabulate
# pip install tabulate
from tabulate import tabulate

data = [
    ["Alice", 24, "Engineer"],
    ["Bob", 30, "Doctor"],
    ["Charlie", 22, "Artist"]
]

headers = ["Name", "Age", "Profession"]

print(tabulate(data, headers, tablefmt="grid"))

# Еще изменения в файле