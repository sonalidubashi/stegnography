import cv2
import os
import string

def encrypt_msg(img, msg, password):
    encrypted_img = img.copy()
    n, m, z = 0, 0, 0

    for i in range(len(msg)):
        pixel_val = encrypted_img[n,m,z]
        pixel_val += ord(msg[i]) % 256
        encrypted_img[n,m,z] = pixel_val

        n = n + 1
        m = m + 1
        z = (z + 1) % 3

    return encrypted_img

def decrypt_msg(encrypted_img, msg, password):
    decrypted_img = encrypted_img.copy()
    decrypted_msg = ""
    n, m, z = 0, 0, 0

    for i in range(len(msg)):
        pixel_val = decrypted_img[n,m,z]
        decrypted_char = chr((pixel_val - ord(msg[i])) % 256)
        decrypted_msg += decrypted_char

        n = n + 1
        m = m + 1
        z = (z + 1) % 3

    return decrypted_msg

def main():
    img = cv2.imread("NA.jpg")

    msg = input("Enter secret message: ")
    password = input("Enter password: ")

    encrypted_img = encrypt_msg(img, msg, password)
    cv2.imwrite("Encryptedmsg.jpg", encrypted_img)
    os.system("start Encryptedmsg.jpg")

    decrypted_msg = decrypt_msg(encrypted_img, msg, password)
    print("Decrypted message:", decrypted_msg)

if __name__ == "__main__":
    main()
