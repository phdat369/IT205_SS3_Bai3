# Phân tích 
# Đầu vào hiện tại chúng ta cần 3 biến là mã nhân viên, họ và tên và phòng ban 
# Sau đó chúng ta nên tạo 1 vòng lặp với lặp 3 lần để lấy thông tin của 3 nhân viên mới và để 3 biến lấy thông tin vào trong để mỗi lần lặp thì lấy được thông tin của mỗi người 
# Sau đó ta cùng câu lệnh điều kiện để check rỗng hoặc khoảng trắng và in ra lỗi 
# Còn nếu đúng thì in ra phiếu điện tử cho mỗi người 

# Viết code 
for i in range(1,4):
    employee_code = input("Nhập mã nhân viên: ")
    employee_name = input("Nhập tên của nhân viên: ")
    department_code = input("Nhập phòng ban của bạn: ")

    if employee_name.isspace() or employee_name == "":
        print("[CẢNH BÁO] Dữ liệu tên hoặc mã không hợp lệ! Hủy bỏ tạo hồ sơ cho nhân viên này")
    else: 
        print("--- Mã phiếu điện tử ---")
        print(f"Mã nhân viên {i}: {employee_code}")
        print(f"Họ tên nhân viên {i}: {employee_name}")
        print(f"Phòng ban nhân viên {i}: {department_code}")