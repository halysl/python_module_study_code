# -*- coding： utf-8-*-

from tempfile import TemporaryFile, NamedTemporaryFile


def example_create_temp_file():
    # 创建匿名文件
    with TemporaryFile("w+t") as f:
        print("filename:{}".format(f.name))
        f.write("Hello World\n")

        f.seek(0)
        data = f.read()
        print(data)


def example_create_named_file():
    # 创建有名文件
    with NamedTemporaryFile("w+t") as f:
        print("filename:{}".format(f.name))
        f.write("Hello World\n")

        f.seek(0)
        data = f.read()
        print(data)

if __name__ == "__main__":
    example_create_temp_file()
    example_create_named_file()
