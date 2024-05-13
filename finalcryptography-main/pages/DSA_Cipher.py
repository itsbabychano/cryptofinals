import streamlit as st
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.exceptions import InvalidSignature

class DSAApp:
    def __init__(self):
        self.private_key, self.public_key = self.generate_keypair()

    def run(self):
        st.title("DSA Signature Verification")

        message = st.text_input("Enter message:")
        sign_button = st.button("Sign")
        if sign_button:
            signature = self.sign_message(message)
            st.text("Signature:")
            st.text(signature)

        st.text("Enter signature to verify:")
        input_signature = st.text_input("")

        verify_button = st.button("Verify Signature")
        if verify_button:
            self.verify_signature(input_signature, message)

    def generate_keypair(self):
        private_key = dsa.generate_private_key(key_size=1024, backend=default_backend())
        public_key = private_key.public_key()
        return private_key, public_key

    def sign_message(self, message):
        signature = self.private_key.sign(message.encode(), hashes.SHA256())
        return signature.hex()

    def verify_signature(self, input_signature, message):
        try:
            input_signature = bytes.fromhex(input_signature)
            self.public_key.verify(input_signature, message.encode(), hashes.SHA256())
            st.success("Signature verified successfully!")
        except InvalidSignature:
            st.error("Signature verification failed!")

if __name__ == "__main__":
    dsa_app = DSAApp()
    dsa_app.run()
