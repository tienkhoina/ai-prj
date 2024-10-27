# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 14:02:48 2024

@author: PC
"""

# Đọc nội dung của hai tệp văn bản
with open(r'D:\discord data set\[136542963336478720] [part 10].txt', 'r', encoding='utf-8') as f1:
    text1 = f1.read()

with open(r'D:\discord data set\[136542963336478720] [part 11].txt', 'r', encoding='utf-8') as f2:
    text2 = f2.read()

# Lấy tập hợp các ký tự duy nhất trong cả hai văn bản
chars1 = sorted(list(set(text1)))
chars2 = sorted(list(set(text2)))

# Tính toán kích thước từ vựng của mỗi văn bản
vocab_size1 = len(chars1)
vocab_size2 = len(chars2)

# In ra các ký tự chỉ có trong văn bản thứ nhất
print("Ký tự chỉ có trong văn bản 1:")
for char in chars1:
    if char not in chars2:
        print(char)

# In ra các ký tự chỉ có trong văn bản thứ hai
print("\nKý tự chỉ có trong văn bản 2:")
for char in chars2:
    if char not in chars1:
        print(char)
