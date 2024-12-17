# Face Verification

Mục tiêu của dự án này là xây dựng một hệ thống xác minh khuôn mặt tự động vào việc đăng nhập cho một ứng dụng web, giúp cải thiện tính bảo mật và tối ưu hóa quy trình xác thực người dùng qua đó để chúng ta có được cái nhìn cụ thể và rõ ràng về cách áp dụng các mô hình này vào một dự án thực tế. Và ta sẽ dùng thư viện DeepFace và mô hình chính là Facenet đã được huấn luyện từ trước.

<p align="center"><img src="image/windowshello_800x450-600x400.jpg" width="640" height="360"></p>


## Các bước cài đặt
Bước đầu, ta sẽ clone repository này về, sử dụng command line.

```shell
git clone https://github.com/tthanh1223/Project2_Face_Recognition.git
cd Project2_Face_Recognition
```
Bước tiếp theo là cài đặt các thư viện cần thiết, ở đây chúng ta tải thư viện từ [`PyPI`](https://pypi.org/project/deepface/):
```shell
pip install flask
pip install opencv-python
pip install pandas
pip install tensorflow
pip install gdown
pip install pillow
pip install mtcnn
pip install retina-face
pip install tf-keras
```
>**Note**: Bạn có thể sử dụng cách quen thuộc với bản thân.
## Chạy webapp bằng Flask

Sau khi đã hoàn thành các bước cài đặt ở trên, ta sẽ khởi động webapp bằng lệnh sau trên command line:
```shell
flask --app app run
```
Bằng cách nhấp vào liên kết [http://127.0.0.1:5000](http://127.0.0.1:5000), ta đã truy cập vào webapp cho tính năng đăng nhập và đăng ký tích hợp xác minh bằng khuôn mặt.

<p align="center"><img src="image/Screenshot%202024-12-16%20190321.png" width="964" height="451"></p>

