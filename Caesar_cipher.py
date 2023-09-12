from fastapi.responses import HTMLResponse


def encrypt(message, key):
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", 'M', "N", "O", 'P', 'Q', 'R', "S", "T", "U",
               'V', 'W', 'X', 'Y', 'Z']
    output_text = ""
    message = message.upper()
    print(message)
    for char in message:
        if char in letters:
            new_index = letters.index(char) + key
            if new_index > 26:
                new_index -= 26
            output_text += letters[new_index]
        else:
            output_text += char
    return output_text


def decrypt(message, key):
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", 'M', "N", "O", 'P', 'Q', 'R', "S", "T", "U",
               'V', 'W', 'X', 'Y', 'Z']
    output_text = ""
    message = message.upper()
    print(message)
    for char in message:
        if char in letters:
            new_index = letters.index(char) - key
            if new_index < 0:
                new_index += 26
            output_text += letters[new_index]
        else:
            output_text += char
    return output_text


def generate_html_response():
    html_content = """
    <html>
        <head>
            <title>Caesar Cipher</title>
        </head>
        <body>
            <h1>Encryption</h1>
                To encrypt a message go to: <b>http://127.0.0.1:8000/encrypt/?msg=YOUR MESSAGE GOES HERE&key=INPUT ENCRYPTION KEY HERE(1-25)</b><br>
                exemple <a href="http://127.0.0.1:8000/encrypt/?msg=abc&key=5">http://127.0.0.1:8000/encrypt/?msg=abc&key=5</a>
                
                <h1>Decryption</h1>
                To decrypt a message go to: <b>http://127.0.0.1:8000/decrypt/?msg=YOUR MESSAGE GOES HERE&key=INPUT ENCRYPTION KEY HERE(1-25)</b><br>
                exemple <a href="http://127.0.0.1:8000/decrypt/?msg=fgh&key=5">http://127.0.0.1:8000/decrypt/?msg=fgh&key=5</a>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
