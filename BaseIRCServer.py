__version__ = "0.0.1"

__all__ = ["IRCServer", "BaseIRCHandler"]

import sys
import SocketServer

class IRCServer(SocketServer.TCPServer):
    
    allow_reuse_address = 1    # Seems to make sense in testing environment

    def server_bind(self):
        """Override server_bind to store the server name."""
        SocketServer.TCPServer.server_bind(self)
        host, port = self.socket.getsockname()[:2]
        self.server_name = socket.getfqdn(host)
        self.server_port = port

class BaseIRCHandler(SocketServer.StreamRequestHandler):
    # The Python system version, truncated to its first component.
    sys_version = "Python/" + sys.version.split()[0]

    # The server software version.  You may want to override this.
    # The format is multiple whitespace-separated strings,
    # where each string is of the form name[/version].
    server_version = "BaseIRC/" + __version__
    def handle(self):
        pass
