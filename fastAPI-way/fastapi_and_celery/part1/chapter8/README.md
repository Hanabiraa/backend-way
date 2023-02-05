# Socket.IO and Celery

Socket.IO is library that simplifies the building of real-time, event-based applications. 

> **Client-side** - socket.io-client is a [client-side library](https://github.com/socketio/socket.io-client) that works on top of the browser's WebSocket API. 

> **Server-side** - [python-socketio](https://python-socketio.readthedocs.io/en/latest/) adds Socket.IO support to FastAPI
It's worth noting that while Socket.IO uses WebSockets, it adds additional metadata to each packet. Because of this you will not be able to successfully connect a regular WebSocket client with Socket.IO server.

It's worth noting that while Socket.IO uses WebSockets, it adds additional metadata to each packet. **Because of this you will not be able to successfully connect a regular WebSocket client with Socket.IO server**

#### Terminology:

1. A **Namespace** is a communication channel that allows you to split the logic of your application over a single shared connection (also called "multiplexing").
2. A **room** is an arbitrary channel that sockets can join and leave. It can be used to broadcast events to a subset of clients.

