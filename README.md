# Python Socket Web Server

A simple HTTP web server built with Python's socket library as a small learning project to explore TCP sockets and the HTTP request-response flow.

## Original Assignment

See the [original task sheet](docs/Week5-Project1-TaskSheet-WebServer-1.docx) for the course project requirements. The downloaded document is included without changes.

## Features

- Listens for connections on port `12000` using an IPv4 TCP socket.
- Reads a file path from an HTTP request and returns the corresponding text file.
- Returns `200 OK` when the file is read successfully.
- Returns `404 Not Found` when the file does not exist or cannot be read.
- Includes `simpleWeb.html` as a demo page.

## How to Run

Requires Python 3. The project uses only the standard library, so no third-party packages are needed.

Open a terminal in the project directory and run:

```bash
python web_server.py
```

Then open this URL in a browser:

```text
http://127.0.0.1:12000/simpleWeb.html
```

To see the 404 page, request a file that does not exist, such as `http://127.0.0.1:12000/missing.html`. Press `Ctrl+C` to stop the server.

Use the full `/simpleWeb.html` path. The current version does not provide a default page for the root path `/`.

## Project Files

| File | Purpose |
| --- | --- |
| `web_server.py` | Socket server and basic HTTP response handling |
| `simpleWeb.html` | Sample web page for testing the server |

## Learning Topics

- Creating, binding, listening on, accepting connections with, and closing sockets.
- The basic request-response flow over a TCP connection.
- HTTP status lines, response headers, and response bodies.
- File reading and basic exception handling.

## Limitations

This learning demo preserves the original implementation and should only be run in a trusted local environment. The server listens on all network interfaces and does not restrict requested file paths. Do not expose it to the public internet or untrusted clients, or run it in a directory containing sensitive files.

The current version handles connections sequentially, reads each request once with a maximum of 1024 bytes, uses basic request parsing, and serves files as HTML text. It does not yet provide robust handling of malformed requests, partial reads and writes, concurrent connections, binary files, or HTTPS.

## Ideas for Further Learning

- Restrict file access and bind to the loopback address by default.
- Add a default page for `/`.
- Improve request parsing, error handling, and response headers.
- Support more file types and concurrent connections.
