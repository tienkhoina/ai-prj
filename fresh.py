import pathlib

# Lấy thư mục làm việc hiện tại
current_directory = pathlib.Path.cwd()

# Lấy thư mục cha của thư mục làm việc hiện tại
parent_directory = current_directory.parent

print(f"The parent directory is: {parent_directory}")

parent_directory = parent_directory/"ai prj"/"data"
print(parent_directory)


def clean_data(input_file, output_file):
    """
    Làm sạch dữ liệu từ file đầu vào và lưu kết quả vào file đầu ra.
    
    :param input_file: Đường dẫn file dữ liệu đầu vào
    :param output_file: Đường dẫn file dữ liệu đầu ra
    """
    cleaned_data = []
    
    with open(input_file, 'r', encoding='utf-8') as infile:
        for line in infile:
            line = line.strip()  # Loại bỏ khoảng trắng đầu/cuối
            if not line:  # Bỏ qua dòng trống
                continue
            
            if ':' in line:
                parts = line.split(':')
                sentence = ':'.join(parts[:-1]).strip()  # Ghép lại phần câu trước dấu cuối
                label = parts[-1].strip()  # Lấy phần cuối cùng làm nhãn
            else:
                sentence = line  # Nếu không có dấu ':', chỉ lấy câu
                label = "unknown"  # Gán nhãn mặc định là "unknown"
            
            # Thêm vào danh sách sau khi làm sạch
            cleaned_data.append(f"{sentence}:{label}")
    
    # Ghi dữ liệu đã làm sạch vào file đầu ra
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for entry in cleaned_data:
            outfile.write(entry + '\n')

    print(f"Dữ liệu đã được làm sạch và lưu vào: {output_file}")


if __name__ == "__main__":
    # Đường dẫn file đầu vào và đầu ra
    input_file = str(parent_directory/"[136542963336478720] [part 10].txt")  # Thay bằng đường dẫn file đầu vào
    output_file =str(parent_directory/"[136542963336478720] [part 10].txt") # Thay bằng đường dẫn file đầu ra
    
    # Gọi hàm làm sạch dữ liệu
    clean_data(input_file, output_file)
