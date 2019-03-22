import asyncio

METRIC = []


class ServerProtocol(asyncio.Protocol):
    def __init__(self):
        self.transport = None

    def connection_made(self, transport: asyncio.Transport):
        self.transport = transport

    def data_received(self, data):
        resp = data.decode().strip().split()
        if resp[0] == 'put':
            res = self._put(resp[1:])
        elif resp[0] == 'get':
            res = self._get(resp[1:])
        else:
            res = 'error\nwrong command\n\n'
        self.transport.write(res.encode())

    @staticmethod    
    def _put(data):
        if len(data) != 3:
            return 'error\nwrong command\n\n'
        flag = True
        for i in METRIC:
            if i[0] == data[0] and i[2] == data[2]:
                flag = False
        if flag:
            METRIC.append(data)
        res = 'ok\n\n'
        return res

    @staticmethod    
    def _get(data):
        s = 'ok\n'
        if len(data) != 1:
            return 'error\nwrong command\n\n'
        elif data[0] == '*':
            for i in METRIC:
                s = s + ' '.join(map(str, i)) + '\n'
        else:
            for i in METRIC:
                if i[0] == data[0]:
                    s = s + ' '.join(map(str, i)) + '\n'
        res = s + '\n'

        return res




def run_server(host='127.0.0.1', port=8888):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        ServerProtocol,
        str(host), int(port)
    )

    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()

run_server()