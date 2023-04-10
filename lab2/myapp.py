from datetime import datetime


def app(environ, start_response):
    with open('pig.txt', 'r', encoding='utf-8') as f:
        file_contents = f.read()  # Чтение содержимого файла в строку
    data = (f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n\n" + f"{file_contents}").encode('utf-8')
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])
