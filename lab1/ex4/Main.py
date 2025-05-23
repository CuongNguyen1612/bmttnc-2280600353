from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while (1 == 1):
    print("\nChương Trình Quản Lý Sinh Viên")
    print("*************************MENU**************************")
    print("**  1. Thêm sinh viên. **")
    print("**  2. Cập Nhập thông tin sinh viên theo ID. **")
    print("**  3. Xóa sinh viên bởi ID. **")
    print("**  4. Tìm kiếm sinh viên theo tên. **")
    print("**  5. Sắp xếp sinh viên theo điểm trung bình. **")
    print("**  6. Sắp xếp sinh viên theo tên. **")
    print("**  7. Hiển thị danh sách sinh viênviên. **")
    print("**  0. Thoát. **")
    print("*******************************************************")

    
    key = int(input("Nhập tùy chọn: "))
    if (key == 1):
        print("\n1. Thêm sinh viên.")
        qlsv.nhapSinhVien()
        print("\nThêm sinh viên thành công!")

    elif (key == 2):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n2. Cập nhập thông tin sinh viên.")
            try:
                ID = int(input("\nNhap ID: "))
                qlsv.updateSinhVien(ID)
            except ValueError:
                print("\nID phải là một số.")
        else:
            print("\nDanh sách sinh viên trong!") 
    elif (key == 3):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n3. Xoá sinh viên.")
            try:
                ID = int(input("\nNhập ID: "))
                if (qlsv.deleteById(ID)):
                    print("\nSinh viên có ID = ", ID, " đã bị xóa.")
                else:
                    print("\nSinh viên có ID = ", ID, " không tồn tại.")
            except ValueError:
                print("\nID phải là một sốsố.")
        else:
            print("\nDanh sáchsách sinh vien trong!") 
    elif (key == 4):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n4. Tìm kiếm sinh viên theo têntên.")
            name = input("\nNhập tên để tìm kiếmkiếm: ")
            searchResult = qlsv.findByName(name)
            if searchResult: 
                qlsv.showSinhVien(searchResult)
            else:
                print("\nkhông tìm thấy sinh viên nào với tên đã nhậpnhập.")
        else:
            print("\nDanh sách sinh vien trong!") 
    elif (key == 5):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n5. Sắp xếp sinh viên theo điểm trung bìnhbình (GPA).")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach sinh vien trong!") 
    elif (key == 6):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n6. Sắp xếp sinh vien theo tênên.")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach sinh viênviên trong!") 
    elif (key == 7):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n7. Hiển thị danh sách sinh vien.")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sáchsách sinh vien trong!")
    elif (key == 0):
        print("\nBạn đã chọn thoát khỏi chương trình !")
        break
    else:
        print("\nkhông có chức năng này !")
        print("\nHãy chọn chức năng trong menumenu.")