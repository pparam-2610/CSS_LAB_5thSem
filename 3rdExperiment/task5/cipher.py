from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
# from Crypto.

plainText = b"This is a top secret."
print("The new text is: ",plainText)
cipherHex = "8d20e5056a8d24d0462ce74e4904c1b513e10d1df4a2ef2ad4540fae1ca0aaf9"

lowerCaseWord = 'median'
key = lowerCaseWord.encode() 
print(key)

finalKey = ""
file = open('allWords.txt', 'r')
lines = file.readlines()
words = [str.strip(line) for line in lines]
for word in words:
    if len(word) >= 16:
        continue
    lowerCaseWord = word.lower()
    key = lowerCaseWord.encode() + b' '*(16-len(lowerCaseWord))
    cipher = AES.new(key, AES.MODE_CBC, iv=bytes.fromhex('0'*32))
    cipherText = cipher.encrypt(pad(plainText, AES.block_size))
    status = "not found"
    if bytes.hex(cipherText) == cipherHex:
        status = "found"
        finalKey = lowerCaseWord
    print(word, bytes.hex(cipherText), status)
print("\n\nThe key is:",finalKey)