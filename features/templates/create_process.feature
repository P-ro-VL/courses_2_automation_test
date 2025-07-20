Feature: Quy trình

  Scenario: Tạo một quy trình mới
    Given Tôi đang ở trang quản lý quy trình
    When Tôi bấm nút div "Tạo quy trình mới"
    Then Tôi được chuyển đến trang tạo quy trình mới

    When Tôi chọn khung quy trình "[Auto Test] Quy trình tạo ngành mới trường Công nghệ - Đại học Kinh tế Quốc dân"
    And Tôi điền vào placeholder "Tên quy trình" là "Quy trình mở ngành Kỹ thuật bán dẫn và ứng dụng"
    And Tôi chọn ngày thứ 1 là "10"
    And Tôi chọn ngày thứ 2 là "31"

    And Tôi bấm nút button "Tạo quy trình"

    And Tôi bấm nút a "Quản lý quy trình"
    And Tôi điền vào placeholder "Tìm kiếm..." là "Quy trình mở ngành Kỹ thuật bán dẫn và ứng dụng"
    Then Tôi thấy trạng thái của quy trình là "Nháp"

    When Tôi bấm chỉnh sửa quy trình

    And Tôi chọn phòng ban phối hợp thứ 2 là "Khoa Hệ thống thông tin quản lý"
    And Tôi chọn người phối hợp thứ 2 là "Nguyễn Thị Bạch Tuyết"
    And Tôi chọn ngày thứ 3 là "11"

    And Tôi chọn ngày thứ 4 là "12"
    
    And Tôi chọn phòng ban phối hợp thứ 6 là "Khoa Công nghệ thông tin"
    And Tôi chọn người phối hợp thứ 6 là "Phạm Minh Hoàn"
    And Tôi chọn ngày thứ 5 là "13"

    And Tôi chọn ngày thứ 6 là "14"

    And Tôi bấm nút button "Tạo quy trình"
    
    And Tôi chờ 5 giây
    
    Then Tôi thấy thông báo "Tạo quy trình thành công!"

    When Tôi nhấn nút tắt dialog thành công
    And And Tôi điền vào placeholder "Tìm kiếm..." là "Quy trình mở ngành Kỹ thuật bán dẫn và ứng dụng"
    Then Tôi thấy trạng thái của quy trình là "Đang thực hiện"