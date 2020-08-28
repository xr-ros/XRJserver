import socket
import threading
import time
from xrJserver.base_class.Request import Request
from xrJserver.base_class.Response import Response
from setting import request_middleware, response_middleware


class Tcp_server(object):
    def __init__(self, ip, port, router_class, urls, thread_num=5):
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.__socket.bind((ip, port))
        self.__socket.settimeout(5)
        self.__socket.listen(thread_num*2)
        self.__thread = [threading.Thread(target=self.listen) for i in range(thread_num)]

        self.__router_class = router_class
        self.__urls = urls

        self.tcp_server_is_run = False

    def listen(self):
        while self.tcp_server_is_run:
            try:
                # get data from tcp client
                connect, addr = self.__socket.accept()
                keep_alive = False

                while True:
                    try:
                        content = connect.recv(500)
                        request = Request(connect, addr, content)
                        response = None

                        # if get a wrongful request, don't change the status of keep_alive.
                        if request.data is not None:
                            keep_alive = request.keep_alive

                        # requests middleware working
                        request_inst_intercept = True
                        for middleware in request_middleware:
                            response = middleware(request)
                            if isinstance(response, Response):
                                request_inst_intercept = False
                                break

                        # router working
                        if request_inst_intercept:
                            router = self.__router_class(self.__urls)
                            response = router.rout(request)

                        # response middleware working
                        for middleware in response_middleware:
                            tem_response = middleware(response)
                            if isinstance(tem_response, Response):
                                response = tem_response
                                break

                        # feedback data
                        connect.send(response.response)

                    # if receive data timeout, close connection
                    except socket.timeout:
                        connect.close()
                        break
                    except ConnectionResetError:
                        print("connection break")
                        break
                    except BrokenPipeError:
                        print("connection break")
                        break

                    # if the connection is'nt a long connection, break connection.
                    if not keep_alive:
                        connect.close()
                        break

            except socket.timeout:
                # print("connect timeout")
                pass

    def run(self):
        self.tcp_server_is_run = True
        for thread in self.__thread:
            thread.start()

        print("tcp server is running")

    def close(self):
        self.tcp_server_is_run = False

        for thread in self.__thread:
            thread.join()

        print("all thread is closed")


if __name__ == "__main__":
    from urls import urls
    from xrJserver.base_class.Router import Router
    tcp = Tcp_server("127.0.0.1", 30000, Router, urls)
    tcp.run()
    time.sleep(60)
    tcp.close()
