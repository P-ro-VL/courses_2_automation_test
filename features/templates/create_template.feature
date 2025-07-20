Feature: Khung quy trình

  Scenario: Tạo một khung quy trình mới
    Given Tôi đang ở trang quản lý khung quy trình
    When Tôi bấm nút a "Tạo khung quy trình mới"
    Then Tôi được chuyển đến trang tạo khung quy trình mới

    When Tôi điền vào placeholder "Tên khung quy trình" là "[Auto Test] Quy trình tạo ngành mới trường Công nghệ - Đại học Kinh tế Quốc dân"

    And Tôi điền vào placeholder "-- Tên giai đoạn --" là "Khoa Viện xây dựng chương trình đào tạo"

    And Tôi điền vào placeholder "-- Tên bước --" là "Khoa/Viện họp và xây dựng chương trình đào tạo"
    And Tôi điền vào placeholder "-- Mô tả bước --" là "Khoa/Viện họp nội bộ để xây dựng chương trình đào tạo"
    And Tôi chọn phòng ban chủ trì thứ 1 là "Khoa Công nghệ thông tin"
    And Tôi chọn người chủ trì thứ 1 là "Phạm Xuân Lâm"
    And Tôi điền sản phẩm đầu ra thứ 1 là "Biên bản họp cấp Khoa/Viện"
    And Tôi chọn loại sản phẩm đầu ra thứ 1 là "File"
    And Tôi bấm nút button "Thêm đầu ra"
    And Tôi điền sản phẩm đầu ra thứ 2 là "Chương trình đào tạo ngành mới"
    And Tôi chọn loại sản phẩm đầu ra thứ 2 là "File"

    And Tôi thêm bước mới

    And Tôi điền vào placeholder "-- Tên bước --" thứ 2 là "Ban Giám hiệu trường Công nghệ xét duyệt chương trình đào tạo"
    And Tôi điền vào placeholder "-- Mô tả bước --" thứ 2 là "Khoa/Viện trình biên bản họp cấp Khoa/Viện và chương trình đào tạo lên Ban Giám hiệu trường Công nghệ"
    And Tôi chọn phòng ban chủ trì thứ 3 là "Trường Công nghệ"
    And Tôi chọn người chủ trì thứ 3 là "Nguyễn Quang Huy"
    And Tôi chọn phòng ban phối hợp thứ 4 là "Khoa Công nghệ thông tin"
    And Tôi chọn người phối hợp thứ 4 là "Trần Thị Mỹ Diệp"
    And Tôi điền sản phẩm đầu ra thứ 3 là "Quyết định của trường Công nghệ"
    And Tôi chọn loại sản phẩm đầu ra thứ 3 là "Link"

    And Tôi thêm giai đoạn thứ 2

    And Tôi điền vào placeholder "-- Tên giai đoạn --" thứ 2 là "Đại học ra quyết định"
    
    And Tôi điền vào placeholder "-- Tên bước --" thứ 3 là "Phòng Quản lý đào tạo xét duyệt"
    And Tôi điền vào placeholder "-- Mô tả bước --" thứ 3 là "Trường Công nghệ chuyển quyết định mở ngành mới lên Phòng Quản lý đào tạo"
    And Tôi chọn phòng ban chủ trì thứ 5 là "Phòng Quản lý đào tạo"
    And Tôi chọn người chủ trì thứ 5 là "Lê Anh Đức"
    And Tôi điền sản phẩm đầu ra thứ 4 là "Thông báo ngành mới"
    And Tôi chọn loại sản phẩm đầu ra thứ 4 là "Text"
    
    And Tôi thêm bước mới

    And Tôi điền vào placeholder "-- Tên bước --" thứ 4 là "Giám đốc Đại học xét duyệt"
    And Tôi điền vào placeholder "-- Mô tả bước --" thứ 4 là "Phòng Quản lý đào tạo chuyển thông báo ngành mới lên Giám đốc Đại học"
    And Tôi chọn phòng ban chủ trì thứ 7 là "Ban Giám đốc Đại học"
    And Tôi chọn người chủ trì thứ 7 là "Bùi Huy Nhượng"
    And Tôi chọn phòng ban phối hợp thứ 8 là "Phòng Quản lý đào tạo"
    And Tôi chọn người phối hợp thứ 8 là "Lê Anh Đức"
    And Tôi điền sản phẩm đầu ra thứ 5 là "Quyết định mở ngành mới của Đại học Kinh tế Quốc dân"
    And Tôi chọn loại sản phẩm đầu ra thứ 5 là "File"
    
    And Tôi bấm nút button "Tiếp tục"
    Then Tôi thấy bước thứ hai của tạo khung quy trình
    When Tôi nhìn thấy đủ các bước tôi đã điền ở bước 1
    
    And Tôi bấm nút button "Tạo khung quy trình"
    
    And Tôi chờ 5 giây
    
    Then Tôi thấy thông báo "Tạo khung quy trình thành công!"

    When Tôi tải lại trang
    Then Tôi nhìn thấy khung quy trình "[Auto Test] Quy trình tạo ngành mới trường Công nghệ - Đại học Kinh tế Quốc dân"