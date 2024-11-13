import socket
import ssl
import base64

# Pilih server SMTP dan port 587 untuk STARTTLS
mailserver = ("smtp.gmail.com", 587)

# Membuat socket dan menghubungkannya ke server SMTP
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(mailserver)  # Coba ganti dengan port 465 jika masalah berlanjut

# Menerima respons dari server
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('Respon 220 tidak diterima dari server.')

# Mengirim perintah HELO
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)

# Mengirim perintah STARTTLS dan mengaktifkan SSL
starttlsCommand = 'STARTTLS\r\n'
clientSocket.send(starttlsCommand.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)

# Membungkus socket dengan SSL menggunakan SSLContext setelah STARTTLS
context = ssl.create_default_context()
clientSocket = context.wrap_socket(clientSocket, server_hostname="smtp.gmail.com")

# Kirim perintah AUTH LOGIN dan lanjutkan autentikasi
username = "email_anda@gmail.com"
password = "kata_sandi_khusus_aplikasi"

authCommand = 'AUTH LOGIN\r\n'
clientSocket.send(authCommand.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)

# Kirim username yang dienkode dalam base64
clientSocket.send(base64.b64encode(username.encode()) + b"\r\n")
recv4 = clientSocket.recv(1024).decode()
print(recv4)

# Kirim kata sandi khusus aplikasi yang dienkode dalam base64
clientSocket.send(base64.b64encode(password.encode()) + b"\r\n")
recv5 = clientSocket.recv(1024).decode()
print(recv5)

# Tutup koneksi
quitCommand = 'QUIT\r\n'
clientSocket.send(quitCommand.encode())
recv6 = clientSocket.recv(1024).decode()
print(recv6)

clientSocket.close()
