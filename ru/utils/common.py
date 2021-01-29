import gzip
import base64
import math
from PIL import Image
from io import BytesIO
# from Crypto.Cipher import AES
# from Crypto.Random import get_random_bytes
# from Crypto.PublicKey import RSA


def query_dict(key, value):
    doc = {
        "query": {
            "term": {
                key: str.lower(value)
            }
        }
    }
    return doc


def query_with(kv):
    doc = {
            "query": {
                "bool": {
                    "must": []
                }
            }
        }
    for k, v in kv:
        doc["query"]["bool"]["must"].append({"term": {k: v}})
    return doc


def image_to_base64(image_path):
    pic = Image.open(image_path)
    pic = pic.convert('RGB')
    w, h = pic.size
    if w > 800:
        pic = pic.resize((800, int(h / (w / 800))), Image.ANTIALIAS)
    else:
        pic = pic.resize((w, h), Image.ANTIALIAS)
    output_buffer = BytesIO()
    pic.save(output_buffer, format='JPEG', quality=50)
    byte_data = output_buffer.getvalue()
    base64_str = base64.b64encode(byte_data)
    return base64_str.decode()


def base64_to_image(base64_str):
    byte_data = base64.b64decode(base64_str)
    image_data = BytesIO(byte_data)
    return image_data


def file_compress(file):
    return gzip.compress(file)


def file_decompress(file):
    return gzip.decompress(eval(file))


def babel_test_data():
    tmp = [
        {
          'id': 1,
          'name': 'Radon',
          'children': [
            {'id': 2, 'name': 'Calendar', 'value':'kk1', 'type':'string', 'range':'""'},
            {'id': 3, 'name': 'Chrome', 'value':15, 'type':'int', 'range':[1,20] },
            {'id': 4, 'name': 'Webstorm', 'value':'a', 'type':'list', 'range':['a','b','c'] },
          ],
        },
        {
          'id': 5,
          'name': 'Xilinx',
          'children': [
            {
              'id': 6,
              'name': 'vuetify',
              'children': [
                {
                  'id': 7,
                  'name': 'src',
                  'children': [
                    { 'id': 8, 'name': 'index' , 'value':{
                        'title': {'text': 'Line Chart'},
                        'tooltip': {},
                        'toolbox': {
                            'feature': {
                                'dataView': {},
                                'saveAsImage': {
                                    'pixelRatio': 2
                                },
                                'restore': {}
                            }
                        },
                        'xAxis': {},
                        'yAxis': {},
                        'series': [{
                            'type': 'line',
                            'smooth': True,
                            'data': [[12, 5], [24, 20], [36, 36], [48, 10], [60, 10], [72, 20]]
                        }]
                    }, 'type':'echarts', 'range':'""'},
                    {'id': 9, 'name': 'bootstrap' , 'value':'kk1', 'type':'echarts', 'range':'""'},
                  ],
                },
              ],
            },
          ],
        },
      ],
    return tmp


def babel_test_he_status(): # status: free,holding,ready
    tmp = [
        {'id': 'a', 'name': 'hardware_environment1', 'status': 'free', 'is_data_updated': False},
        {'id': 'b', 'name': 'hardware_environment2', 'status': 'holding', 'is_data_updated': False},
        {'id': 'c', 'name': 'hardware_environment3', 'status': 'ready', 'is_data_updated': True}
    ],
    return tmp


def babel_test_he_data(): # status: free,holding,ready
    tmp = {
        [{'id': 'a', 'name': 'hardware_environment1', 'status': 'free', 'is_data_updated': False}],
        [{'id': 'b', 'name': 'hardware_environment2', 'status': 'holding', 'is_data_updated': False}],
        [{'id': 'c', 'name': 'hardware_environment3', 'status': 'ready', 'is_data_updated': True}],
    }
    return tmp


# def cal_sin():
#     x = float_range(-1, 1, 0.1)
#     y = float_range(-1, 1, 0.1)
#     return math.sin(x * math.pi) * math.sin(y * math.pi)
#
#
# def float_range(i:float, j:float, k=1)->list:
#     xlen=str((len(str(k-int(k)))-2)/10)+"f"
#     # print("xlen=",xlen)
#     lista=[]
#     while i<j:
#         lista.append(format(i, xlen))
#         i+=k
#     return lista
# def new_rsa_keys(bit):
#     key = RSA.generate(bit)
#     private_key = key.export_key()
#     file_out = open("private.pem", "wb")
#     file_out.write(private_key)
#     file_out.close()
#
#     public_key = key.publickey().export_key()
#     file_out = open("receiver.pem", "wb")
#     file_out.write(public_key)
#     file_out.close()


# def rsa_encrypt(text, public_key):
#     content = text.encode("utf-8")
#     ciphertext = rsa.encrypt(content, public_key)
#     return ciphertext
#
#
# def rsa_decrypt(ciphertext, private_key):
#     content = rsa.decrypt(ciphertext, private_key)
#     text = content.decode("utf-8")
#     return text
