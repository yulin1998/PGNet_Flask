import os
import cv2
import uuid
import time
import base64
from test import *
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)


def get_img():
    img_str = request.form['image']  # 获取图像数据,对应客户端的img_str
    img_byte = base64.b64decode(img_str)  # img_byte是字节型数据，二进制编码。b64decode对字节型b64编码数据进行解码。bytes->bytes
    image = np.fromstring(img_byte, np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    random_name = '{}.jpg'.format(uuid.uuid4().hex)
    save_path = os.path.join('caches', secure_filename(random_name))
    cv2.imwrite(save_path, image)
    return save_path


@app.route('/ocr', methods=['GET', 'POST'])
def ocr():
    file = request.form['image']
    if file is not None:
        save_path = get_img()
        # time-1
        t1 = time.time()
        img = cv2.imread(save_path)
        img_res, word_res = test_net(img)
        # time-2
        t2 = time.time()
        return jsonify({
            'status': 'success',
            'res': word_res,
            'time': '{:.4f}'.format(t2-t1)
        })
    else:
        return jsonify({'status': 'failure'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    # app.run(debug=True)