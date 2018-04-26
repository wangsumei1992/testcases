import os
file_path1 = os.path.dirname(__file__)
print(file_path1)
file_path2 = os.path.dirname()
print(file_path2)
file_path3 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print(file_path3)
file_path4 = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
print(file_path4)