from Crypto.Cipher import AES

mail = 'admin@sekai.team'
enc = '03afaa672ff078c63d5bdb0ea08be12b09ea53ea822cd2acef36da5b279b9524'
enc = bytes.fromhex(enc)

key = b'react_native_expo_version_47.0.0'
iv = b'__sekaictf2023__'

cipher = AES.new(key, AES.MODE_CBC, iv)
passwd = cipher.decrypt(enc)
print(passwd) # b's3cr3t_SEKAI_P@ss'

# SEKAI{15_React_N@71v3_R3v3rs3_H@RD???}
