import socket



s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# I Put 1.1.1.1 For The Server Because I Don't Have A Server Myself. So Put Your Server There.
s.connect(('1.1.1.1',443))

buffer_length = 40
stuff = 'W'*buffer_length

payload = 'GET ' + stuff + ' HTTP/1.1\r\n\r\n'

s.send(payload.encode('raw_unicode_escape'))
print("payload successful")
s.close