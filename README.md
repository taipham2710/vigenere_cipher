# Vigenère Cipher Tool

**Vigenère Cipher** là một thuật toán mã hóa đối xứng dựa trên khóa, giúp mã hóa và giải mã văn bản bằng một chuỗi ký tự làm khóa. Thuật toán này an toàn hơn Caesar Cipher nhờ sử dụng nhiều phép dịch chuyển khác nhau tùy vào ký tự khóa.

## Mô tả
Script này hỗ trợ:
- Mã hóa (Encrypt) văn bản với khóa bất kỳ (chỉ lấy ký tự chữ cái trong khóa).
- Giải mã (Decrypt) văn bản đã mã hóa bằng đúng khóa đã sử dụng trước đó.
- Giữ nguyên các ký tự không phải chữ cái (dấu câu, số, khoảng trắng).

## Cách sử dụng

1. Chạy script:
    ```bash
    python <tên_file.py>
    ```

2. Chọn chế độ:
    - `E` để mã hóa (Encrypt)
    - `D` để giải mã (Decrypt)

3. Nhập văn bản cần xử lý.

4. Nhập khóa (key). Khóa càng dài và phức tạp thì mức độ bảo mật càng cao.

## Ví dụ

### Mã hóa
```
Do you want to (E)ncrypt or (D)ecrypt? E
Enter the text: Hello World!
Enter the key: Secret
Encrypted Text: Zinsl Wsljb!
```

### Giải mã
```
Do you want to (E)ncrypt or (D)ecrypt? D
Enter the text: Zinsl Wsljb!
Enter the key: Secret
Decrypted Text: Hello World!
```

## Lưu ý
- Chỉ các ký tự chữ cái (A-Z, a-z) trong khóa mới được dùng để mã hóa/giải mã.
- Khóa không chứa chữ cái sẽ báo lỗi.
- Các ký tự đặc biệt, số, và dấu câu trong văn bản sẽ giữ nguyên.

## Tham khảo
- [Wikipedia: Vigenère cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)
