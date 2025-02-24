# Cờ Vây 2D

## Giới thiệu
Đây là một trò chơi cờ vây với đồ họa 2D nhìn từ trên xuống, được phát triển bằng Python. Trò chơi hỗ trợ:
- Chế độ chơi với bot sử dụng thuật toán Monte Carlo Tree Search (MCTS) (sẽ làm trong thời gian tới)
- Chế độ chơi 1v1 giữa hai người chơi.

## Tính năng chính
- **Giao diện 2D trực quan**: Hiển thị bàn cờ và quân cờ rõ ràng.
- **Chế độ chơi**:
  - Đánh với người chơi khác trên cùng một thiết bị.
- **Xử lý luật chơi**: Tự động kiểm tra nước đi hợp lệ, tính điểm, bắt quân.


## Cài đặt
### Yêu cầu hệ thống
- Python 3.8 trở lên
- Các thư viện cần thiết:
  ```sh
  pip install pygame numpy
  ```

## Hướng dẫn sử dụng
### Chạy trò chơi
Mở terminal/cmd và chạy lệnh:
```sh
python main.py
```

### Cách chơi
- **Chế độ 1v1**: Hai người chơi thay phiên đặt quân đen và trắng.
- Nhấn vào ô trống để đặt quân.
- Trò chơi kết thúc khi không còn nước đi hoặc khi hai bên đều bỏ lượt liên tiếp.



