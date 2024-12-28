import torch

# Tải file và ánh xạ dữ liệu từ GPU sang CPU
checkpoint = torch.load("D:\\ai prj\\data\\[136542963336478720][part 10].pth", map_location=torch.device('cpu'))

# Kiểm tra nội dung
print(checkpoint.keys())
