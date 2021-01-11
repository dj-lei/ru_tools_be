import gzip
import base64
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
