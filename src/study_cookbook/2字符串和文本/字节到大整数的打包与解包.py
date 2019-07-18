# -*- coding: utf-8 -*-


def byte_2_int():
    data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
    print(len(data))

    littele_data = int.from_bytes(data, "little")
    big_data = int.from_bytes(data, "big")
    print(littele_data)
    print(big_data)


def int_2_byte():
    data = 94522842520747284487117727783387188
    little_byte = data.to_bytes(16, "little")
    big_byte = data.to_bytes(16, "big")
    print(little_byte)
    print(big_byte)

    little_byte = data.to_bytes(18, "little")
    big_byte = data.to_bytes(18, "big")
    print(little_byte)
    print(big_byte)

if __name__ == "__main__":
    byte_2_int()
    int_2_byte()
