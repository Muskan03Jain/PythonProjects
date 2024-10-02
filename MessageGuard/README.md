# Message Guard

Message Guard is a simple Streamlit web app that allows users to encrypt and decrypt messages for secure communication. The app transforms regular text into an encrypted format using a basic encoding method, and it also decodes the encrypted message back into its original form.

## Features

- **Encryption**: Converts a message into a coded format using a combination of letter manipulation and random characters.
- **Decryption**: Reverts the coded message back to its original format based on the applied encoding rules.
- **User-friendly interface**: Powered by Streamlit for a seamless user experience.

## How it Works

1. **Message Encryption**:
   - For messages longer than 3 characters:
     - The first letter of the word is shifted to the end.
     - Random letters are appended at the beginning and end of the word.
   - For messages shorter than 3 characters:
     - The message is reversed.

2. **Message Decryption**:
   - For messages longer than 3 characters:
     - Removes the random letters and shifts the original first letter back to its position.
   - For messages shorter than 3 characters:
     - The message is reversed back to its original form.

## How to Use

1. Input a message in the text box.
2. Click "Code" to encrypt the message.
3. Click "Decode" to decrypt the message.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Muskan03Jain/PythonProjects/tree/main/MessageGuard.git
