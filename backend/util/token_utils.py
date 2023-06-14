from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

secrete_key = '8FzWtEwM2QjK1x7S'

def encrypt_AES(input_str):
    # 将密钥转换为字节序列
    key_bytes = secrete_key.encode('utf-8')

    # 创建AES加密器对象
    cipher = AES.new(key_bytes, AES.MODE_CBC)

    # 将输入字符串转换为字节序列并填充
    input_bytes = pad(input_str.encode('utf-8'), AES.block_size)

    # 加密数据并返回
    encrypted_bytes = cipher.encrypt(input_bytes)
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    encrypted_str = base64.b64encode(encrypted_bytes).decode('utf-8')
    return iv + encrypted_str

def decrypt_AES(input_str):
    # 将密钥转换为字节序列
    key_bytes = secrete_key.encode('utf-8')

    # 解析IV和加密数据
    iv = base64.b64decode(input_str[:24])
    encrypted_bytes = base64.b64decode(input_str[24:])

    # 创建AES解密器对象
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv)

    # 解密数据并返回
    decrypted_bytes = cipher.decrypt(encrypted_bytes)
    decrypted_str = unpad(decrypted_bytes, AES.block_size).decode('utf-8')
    return decrypted_str