import socket
import time

class ClientError(Exception):
    pass

class ClientSocketError(ClientError):
    """Исключение, выбрасываемое клиентом при сетевой ошибке"""
    pass

class ClientProtocolError(ClientError):
    """Исключение, выбрасываемое клиентом при ошибке протокола"""
    pass

class Client:

	def __init__(self, host, port, timeout=None):
		self.host = host
		self.port = port
		try:
			self.connection = socket.create_connection((host, port), timeout)
		except socket.error as err:
			raise ClientSocketError("error create connection", err)

	def _read(self):
		"""Метод для чтения ответа сервера"""
		data = b""
		# накапливаем буфер, пока не встретим "\n\n" в конце команды
		while not data.endswith(b"\n\n"):
			try:
				data += self.connection.recv(1024)
			except socket.error as err:
				raise ClientSocketError("error recv data", err)

		# не забываем преобразовывать байты в объекты str для дальнейшей работы
		decoded_data = data.decode()

		status, payload = decoded_data.split("\n", 1)
		payload = payload.strip()

		# если получили ошибку - бросаем исключение ClientError
		if status == "error":
			raise ClientProtocolError(payload)

		return payload

	def put(self, name, value, timestamp=int(time.time())):
		try:
			self.connection.sendall(f"put {name} {value} {timestamp}\n".encode())
		except socket.error as err:
			raise ClientSocketError("error send data", err)

		self._read()

	def get(self, name):
		try:
			self.connection.sendall(f"get {name}\n".encode())
		except socket.error as err:
			raise ClientSoketError("error send data", err)
		
		payload = self._read()

		if payload == "":
			return {}

		data = {}

		for i in payload.split('\n'):
			i = i.split()
			if i[0] in data:
				data[i[0]].append((int(i[2]), float(i[1])))
			else:
				data.update({i[0]:[(int(i[2]),float(i[1]))]})

		return data

	def close(self):
		try:
			self.connection.close()
		except socket.error as err:
			raise ClientSocketError		

#client = Client("127.0.0.1", 8888, timeout=15)

#client.put("palm.cpu", 0.5, timestamp=1150864247)
#client.put("palm.cpu", 2.0, timestamp=1150864248)
#client.put("palm.cpu", 0.5, timestamp=1150864248)

#client.put("eardrum.cpu", 3, timestamp=1150864250)
#client.put("eardrum.cpu", 4, timestamp=1150864251)
#client.put("eardrum.memory", 4200000)

#print(client.get("*"))

#client.close()

