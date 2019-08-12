# -*- coding: utf-8 -*-


class NetworkError(Exception):
    pass


class HostnameError(NetworkError):
    pass


class TimeoutError(NetworkError):
    pass


class ProtocolError(NetworkError):
    pass


class CustomError(Exception):
    def __init__(self, message, status):
        # 使用所有参数调用 Exception.__init__()
        # Exception的默认行为是接受所有传递的参数并将它们以元组形式存储在 .args
        super().__init__(message, status)
        self.message = message
        self.status = status

try:
    raise RuntimeError('It failed')
except RuntimeError as e:
    print(e.args)

try:
    raise RuntimeError('It failed', 42, 'spam')
except RuntimeError as e:
    print(e.args)
