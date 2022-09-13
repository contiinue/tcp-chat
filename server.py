import asyncio

server_host, server_port = '', 9090


class Server:
    def __init__(self):
        self.all_clients = []

    def _append_client_to_list(self, writer: asyncio.StreamWriter) -> None:
        self.all_clients.append(writer)

    async def _send_message(self, writer: asyncio.StreamWriter, message: bytes, addr) -> None:
        """ send message l  """
        host, port = addr
        for i in self.all_clients:
            if i != writer:
                i.write(f'[Message port {host}]: {message}')
            else:
                i.write(b'No massage')

    @staticmethod
    def _get_connect_info(writer: asyncio.StreamWriter) -> tuple:
        return writer.get_extra_info('peername')

    async def _server_read(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
        """ server  """
        self._append_client_to_list(writer)
        connect_from = self._get_connect_info(writer)

        while True:
            data = await reader.read(100)
            if not data:
                writer.close()
                break

            await self._send_message(writer, data, connect_from)
            await writer.drain()
        self.all_clients.remove(writer)
        writer.close()

    async def main(self) -> None:
        start_server = await asyncio.start_server(
            self._server_read, server_host, server_port)

        async with start_server:
            print('>>> server started')
            await start_server.serve_forever()


if __name__ == '__main__':
    server = Server()
    asyncio.run(server.main())
