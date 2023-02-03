# WebSockets and Celery

> **WebSocket** is a computer communications protocol, providing full-duplex communication channels over a single TCP connection.

## ASGI vs WSGI#

ASGI is a spiritual successor to WSGI, the long-standing Python standard for compatibility between web servers, frameworks, and applications.

In short, ASGI was created to add support for WebSockets, HTTP/2, and async/await, none of which are supported by WSGI.

FastAPI is based on Starlette and already implements the ASGI specification.