import requests
import base64

if __name__ == '__main__':

    '''
    img1 = f.read(open('./6.jpg', 'rb')) # img1->二进制数据
    img2 = base64.b64encode(img1)   # img2->对二进制数据进行base64编码，得到字节数据
    img3 = img2.decode() # img3->对字节类型数据进行base64解码得到字符串数据
    '''
    url = 'http://192.168.0.133:5000/ocr'
    with open('./6.jpg', 'rb') as f:
        img = base64.b64encode(f.read()).decode()
    file = {'image': img}
    r = requests.post(url, data=file)
    print(r.text)
