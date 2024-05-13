import streamlit as st
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

class RSAApp:
    def __init__(self):
        self.key = RSA.generate(2048)  # Generate RSA key

    def run(self):
        st.title("RSA Encryption and Decryption")

        plaintext = st.text_area("Enter text to encrypt:")
        encrypt_button = st.button("Encrypt")
        if encrypt_button:
            encrypted_message = self.encrypt(plaintext)
            st.text_area("Encrypted text:", value=encrypted_message, height=100)

        st.subheader("Decryption")
        encrypted_text = st.text_area("Enter text to decrypt:")
        decrypt_button = st.button("Decrypt")
        if decrypt_button:
            decrypted_message = self.decrypt(encrypted_text)
            st.text_area("Decrypted text:", value=decrypted_message, height=100)

    def encrypt(self, plaintext):
        cipher = PKCS1_OAEP.new(self.key.publickey())
        encrypted_message = cipher.encrypt(plaintext.encode())
        return encrypted_message.hex()

    def decrypt(self, encrypted_message_hex):
        encrypted_message = bytes.fromhex(encrypted_message_hex)
        cipher = PKCS1_OAEP.new(self.key)
        decrypted_message = cipher.decrypt(encrypted_message)
        return decrypted_message.decode()

if __name__ == "__main__":
    rsa_app = RSAApp()
    rsa_app.run()
