import unittest
from unittest.mock import patch, MagicMock
from server import server_client


class TestServer(unittest.TestCase):
    @patch("server.apple")
    @patch("socket.socket")
    def test server_client_00_byte(self, mock_socket, mock_apple):
        client_socket = MagicMock()
        client_socket.recv.side_effect = [b"\x00", b""]

     server_client(client_socket)

        mock_apple.assert_called_once()

        client_socket.sendall.assert_called_with(b"Message received")
        client_socket.close.assert_called_once()

    @patch("server.banana")
    @patch("socket.socket")
    def test server_client_01_byte(self, mock_socket, mock_banana):
        client_socket = MagicMock()
        client_socket.recv.side_effect = [b"\x01", b""]

     server_client(client_socket)

        mock_banana.assert_called_once()

        client_socket.close.assert_called_once()

    @patch("server.mango")
    @patch("socket.socket")
    def test server_client_02_byte(self, mock_socket, mock_mango):
        client_socket = MagicMock()
        client_socket.recv.side_effect = [b"\x02", b""]

     server_client(client_socket)

        mock_mango.assert_called_once()

        client_socket.close.assert_called_once()


if __name__ == "__main__":
    unittest.main()
