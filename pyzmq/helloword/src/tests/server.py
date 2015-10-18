# -*- coding: utf-8 -*-

# Copyright (c) the Contributors
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

from zmq.eventloop import ioloop
from core.handlers import CommandHandler

loop = ioloop.IOLoop.instance()


class MyCommandHandler(CommandHandler):

    def __init__(self, name, end_point):
        CommandHandler.__init__(self, name, end_point)

    def _on_recv(self, stream, msg):
        print('receive peer message {0}'. format(msg[0]))
        stream.send('command: ok for message: {0}'.format(msg[0]), copy=False)

    def _on_send(self, stream, msg, status):
        print('send peer message {0}'. format(msg[0]))

if __name__ == "__main__":

    server = 'tcp://127.0.0.1:5555'
    handler = MyCommandHandler('MyCommandHandler', server)
    handler.start()
    loop.start()