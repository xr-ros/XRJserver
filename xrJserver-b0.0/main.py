import time
from os import getpid, path, system
import sys
import getopt

from urls import urls
from xrJserver.base_class.Router import Router
from xrJserver.base_class.tcp_server import Tcp_server
from setting import data_container

options, args = getopt.getopt(sys.argv[1:], "hi:P:", ["stop", "start"])

IP = "127.0.0.1"
PORT = 11322
default_flag = 0
ready_to_start_service = False

try:
    for opt, arg in options:
        # print("checking")
        if opt in ("-h", "--h"):
            print("Documentation: this is a tcp_server used to bridging robot and another app")
            print("options:")
            print("-h or --help: for help")
            print("-i: server working IP")
            print("-P: server working PORT")
            print("--stop: stop server")
            print("--start: start server")
            sys.exit()

        elif opt == "-i":
            if [True]*4 == [num.isdigit() and 0 <= int(num) < 255 for num in arg.split(".")]:
                IP = arg
                default_flag += 1
            else:
                print("ArgError: option -i, Please enter the correct IP!")
                sys.exit()

        elif opt == "-P":
            if arg.isdigit() and 0 < int(arg) < 62535:
                PORT = int(arg)
                default_flag += 1
            else:
                print("ArgError: Please enter the correct PORT!")
                sys.exit()

        elif opt == "--start":
            ready_to_start_service = True

        elif opt == "--stop":
            with open("./pid/main.pid", "w") as f:
                f.write("")
            print("stop server")
            sys.exit()

        else:
            print(opt + ": This option is not allowed")
            sys.exit()

except getopt.GetoptError:
    print("options error, please use '-h' to learn how to use it")
    sys.exit()

if not ready_to_start_service:
    print("please use --start option to start server, or --stop to stop server")
    sys.exit()
if not default_flag:
    print("server working in default setting: 127.0.0.1:11322")
else:
    print("server working in %s:%d" % (IP, PORT))

tcp = Tcp_server("0.0.0.0", 11322, Router, urls, thread_num=10)
tcp.run()

pid = getpid()
with open("./pid/main.pid", "w") as f:
    f.write("%d" % pid)

while True:
    try:
        if path.getsize("./pid/main.pid") == 0:
            break
        # print(data_container)
        
        time.sleep(2)

    except KeyboardInterrupt:
        print("Force service shutdown")
        break

tcp.close()

