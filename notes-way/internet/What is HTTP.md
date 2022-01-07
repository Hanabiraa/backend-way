# This article cover some other articles:
1) [An overview of HTTP. MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)
2) [Hypertext Transfer Protocol. Wikipedia](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol)
3) [What is HTTP? Cloudflare](https://www.cloudflare.com/learning/ddos/glossary/hypertext-transfer-protocol-http/)
4) [Journey to HTTP/2](https://kamranahmed.info/blog/2016/08/13/http-in-depth/)

## Introduction

**HTTP** is a protocol for fetching resources such as HTML documents. It is the foundation of any data exchange on the Web and it is a client-server protocol, which means requests are initiated by the recipient, usually the Web browser. A complete document is reconstructed from the different sub-documents fetched, for instance, text, layout description, images, videos, scripts, and more.

![](./assets/img/fetching_a_page.png)

Clients and servers communicate by exchanging individual messages (as opposed to a stream of data). The messages sent by the client, usually a Web browser, are called **requests** and the messages sent by the server as an answer are called **responses**.

![](./assets/img/http-layers.png)

Designed in the early 1990s, HTTP is an extensible protocol which has evolved over time. It is an application layer protocol that is sent over TCP, or over a TLS-encrypted TCP connection, though any reliable transport protocol could theoretically be used. Due to its extensibility, it is used to not only fetch hypertext documents, but also images and videos or to post content to servers, like with HTML form results. HTTP can also be used to fetch parts of documents to update Web pages on demand.

Terminology:
> HTTP - The Hypertext Transfer Protocol
> 
> request - the messages sent by the client, usually a Web browser
> 
> response - the messages sent by the server as an answer
> 
## Components of HTTP-based systems

HTTP is a client-server protocol: requests are sent by one entity, the user-agent (or a proxy on behalf of it). Most of the time the user-agent is a Web browser, but it can be anything, for example, a robot that crawls the Web to populate and maintain a search engine index.

Each individual request is sent to a server, which handles it and provides an answer called the response. Between the client and the server there are numerous entities, collectively called **proxies (this term is explained in detail in a separate chapter of the article)**, which perform different operations and act as _gateways or caches_, for example.

![](./assets/img/client-server-chain.png)

In reality, there are more computers between a browser and the server handling the request: there are routers, modems, and more. Thanks to the layered design of the Web, these are hidden in the network and transport layers. HTTP is on top, at the application layer. Although important for diagnosing network problems, the underlying layers are mostly irrelevant to the description of HTTP.

## Client: the user-agent

The user-agent is any tool that acts on behalf of the user. This role is primarily performed by the Web browser, but it may also be performed by programs used by engineers and Web developers to debug their applications.

> The browser is **always** the entity initiating the request. It is never the server (though some mechanisms have been added over the years to simulate server-initiated messages).

To display a Web page, the browser sends an original request to fetch the HTML document that represents the page. It then parses this file, making additional requests corresponding to execution scripts, layout information (CSS) to display, and sub-resources contained within the page (usually images and videos). The Web browser then combines these resources to present the complete document, the Web page. Scripts executed by the browser can fetch more resources in later phases and the browser updates the Web page accordingly.

A Web page is a hypertext document. This means some parts of the displayed content are links, which can be activated (usually by a click of the mouse) to fetch a new Web page, allowing the user to direct their user-agent and navigate through the Web. The browser translates these directions into HTTP requests, and further interprets the HTTP responses to present the user with a clear response.

## The Web server

On the opposite side of the communication channel is the server, which *serves* the document as requested by the client. A server appears as only a single machine virtually; but it may actually be a collection of servers sharing the load (load balancing), or a complex piece of software interrogating other computers (like cache, a DB server, or e-commerce servers), totally or partially generating the document on demand.

> A server is not necessarily a single machine, but several server software instances can be hosted on the same machine. With HTTP/1.1 and the Host header, they may even share the same IP address.

## Proxies

Between the Web browser and the server, numerous computers and machines relay the HTTP messages. Due to the layered structure of the Web stack, most of these operate at the transport, network or physical levels, becoming transparent at the HTTP layer and potentially having a significant impact on performance. Those operating at the application layers are generally called **proxies**. These can be transparent, forwarding on the requests they receive without altering them in any way, or non-transparent, in which case they will change the request in some way before passing it along to the server.

Proxies may perform numerous functions:

* caching (the cache can be public or private, like the browser cache)
  
* filtering (like an antivirus scan or parental controls)
  
* load balancing (to allow multiple servers to serve different requests)
  
* authentication (to control access to different resources)
  
* logging (allowing the storage of historical information)

## Basic aspects of HTTP

### HTTP is simple

HTTP is generally designed to be simple and human readable, even with the added complexity introduced in HTTP/2 by encapsulating HTTP messages into frames. HTTP messages can be read and understood by humans, providing easier testing for developers, and reduced complexity for newcomers.

### HTTP is extensible

Introduced in HTTP/1.0, HTTP headers make this protocol easy to extend and experiment with. New functionality can even be introduced by a simple agreement between a client and a server about a new header's semantics.

### HTTP is stateless, but not sessionless

HTTP is stateless: there is no link between two requests being successively carried out on the same connection. This immediately has the prospect of being problematic for users attempting to interact with certain pages coherently, for example, using e-commerce shopping baskets. But while the core of HTTP itself is stateless, HTTP cookies allow the use of stateful sessions. Using header extensibility, HTTP Cookies are added to the workflow, allowing session creation on each HTTP request to share the same context, or the same state.

### HTTP and connections

A connection is controlled at the transport layer, and therefore fundamentally out of scope for HTTP. HTTP doesn't require the underlying transport protocol to be connection-based; it only requires it to be reliable, or not lose messages (at minimum, presenting an error in such cases). Among the two most common transport protocols on the Internet, TCP is reliable and UDP isn't. HTTP therefore relies on the TCP standard, which is connection-based.

Before a client and server can exchange an HTTP request/response pair, they must establish a TCP connection, a process which requires several round-trips. The default behavior of HTTP/1.0 is to open a separate TCP connection for each HTTP request/response pair. This is less efficient than sharing a single TCP connection when multiple requests are sent in close succession.

In order to mitigate this flaw, HTTP/1.1 introduced pipelining (which proved difficult to implement) and persistent connections: the underlying TCP connection can be partially controlled using the Connection header. HTTP/2 went a step further by multiplexing messages over a single connection, helping keep the connection warm and more efficient.

## What can be controlled by HTTP

This extensible nature of HTTP has, over time, allowed for more control and functionality of the Web. Cache and authentication methods were functions handled early in HTTP history. The ability to relax the origin constraint, by contrast, was only added in the 2010s.

Here is a list of common features controllable with HTTP:

* Caching How documents are cached can be controlled by HTTP. The server can instruct proxies and clients about what to cache and for how long. The client can instruct intermediate cache proxies to ignore the stored document.
  
* Relaxing the origin constraint To prevent snooping and other privacy invasions, Web browsers enforce strict separation between Web sites. Only pages from the same origin can access all the information of a Web page. Though such a constraint is a burden to the server, HTTP headers can relax this strict separation on the server side, allowing a document to become a patchwork of information sourced from different domains; there could even be security-related reasons to do so.
  
* Authentication Some pages may be protected so that only specific users can access them. Basic authentication may be provided by HTTP, either using the WWW-Authenticate and similar headers, or by setting a specific session using HTTP cookies.
  
* Proxy and tunneling Servers or clients are often located on intranets and hide their true IP address from other computers. HTTP requests then go through proxies to cross this network barrier. Not all proxies are HTTP proxies. The SOCKS protocol, for example, operates at a lower level. Other protocols, like ftp, can be handled by these proxies.
  
* Sessions Using HTTP cookies allows you to link requests with the state of the server. This creates sessions, despite basic HTTP being a state-less protocol. This is useful not only for e-commerce shopping baskets, but also for any site allowing user configuration of the output.

## HTTP flow

When a client wants to communicate with a server, either the final server or an intermediate proxy, it performs the following steps:

1. Open a TCP connection: The TCP connection is used to send a request, or several, and receive an answer. The client may open a new connection, reuse an existing connection, or open several TCP connections to the servers.
   
2. Send an HTTP message: HTTP messages (before HTTP/2) are human-readable. With HTTP/2, these simple messages are encapsulated in frames, making them impossible to read directly, but the principle remains the same. For example:

```
GET / HTTP/1.1
Host: developer.mozilla.org
Accept-Language: fr
```

3. Read the response sent by the server, such as:

```
HTTP/1.1 200 OK
Date: Sat, 09 Oct 2010 14:28:02 GMT
Server: Apache
Last-Modified: Tue, 01 Dec 2009 20:18:22 GMT
ETag: "51142bc1-7449-479b075b2891b"
Accept-Ranges: bytes
Content-Length: 29769
Content-Type: text/html

<!DOCTYPE html... (here come the 29769 bytes of the requested web page)
```

4. Close or reuse the connection for further requests.

If HTTP pipelining is activated, several requests can be sent without waiting for the first response to be fully received. HTTP pipelining has proven difficult to implement in existing networks, where old pieces of software coexist with modern versions. HTTP pipelining has been superseded in HTTP/2 with more robust multiplexing requests within a frame.

## HTTP Messages

HTTP messages, as defined in HTTP/1.1 and earlier, are human-readable. In HTTP/2, these messages are embedded into a binary structure, a frame, allowing optimizations like compression of headers and multiplexing. Even if only part of the original HTTP message is sent in this version of HTTP, the semantics of each message is unchanged and the client reconstitutes (virtually) the original HTTP/1.1 request. It is therefore useful to comprehend HTTP/2 messages in the HTTP/1.1 format.

There are two types of HTTP messages, requests and responses, each with its own format.

### Requests

An example HTTP request:

![](./assets/img/http_request.png)

Requests consists of the following elements:

* An HTTP method, usually a verb like GET, POST, or a noun like OPTIONS or HEAD that defines the operation the client wants to perform. Typically, a client wants to fetch a resource (using GET) or post the value of an HTML form (using POST), though more operations may be needed in other cases.
  
* The path of the resource to fetch; the URL of the resource stripped from elements that are obvious from the context, for example without the protocol (http://), the domain (here, developer.mozilla.org), or the TCP port (here, 80).
  
* The version of the HTTP protocol.
  
* Optional headers that convey additional information for the servers.

* A body, for some methods like POST, similar to those in responses, which contain the resource sent.

### Responses

An example response:

![](./assets/img/http_response.png)

Responses consist of the following elements:

* The version of the HTTP protocol they follow.
  
* A status code, indicating if the request was successful or not, and why.

* A status message, a non-authoritative short description of the status code.

* HTTP headers, like those for requests.

* Optionally, a body containing the fetched resource.

## What’s an HTTP status code?
HTTP status codes are 3-digit codes most often used to indicate whether an HTTP request has been successfully completed. Status codes are broken into the following 5 blocks:

1. 1xx Informational
   
2. 2xx Success

3. 3xx Redirection

4. 4xx Client Error

5. 5xx Server Error
   
The “xx” refers to different numbers between 00 and 99.

Status codes starting with the number ‘2’ indicate a success. For example, after a client requests a web page, the most commonly seen responses have a status code of ‘200 OK’, indicating that the request was properly completed.

If the response starts with a ‘4’ or a ‘5’ that means there was an error and the webpage will not be displayed. A status code that begins with a ‘4’ indicates a client-side error (It’s very common to encounter a ‘404 NOT FOUND’ status code when making a typo in a URL). A status code beginning in ‘5’ means something went wrong on the server side. Status codes can also begin with a ‘1’ or a ‘3’, which indicate an informational response and a redirect, respectively.

## APIs based on HTTP

The most commonly used API based on HTTP is the XMLHttpRequest API, which can be used to exchange data between a user agent and a server. The modern Fetch API provides the same features with a more powerful and flexible feature set.

Another API, server-sent events, is a one-way service that allows a server to send events to the client, using HTTP as a transport mechanism. Using the EventSource interface, the client opens a connection and establishes event handlers. The client browser automatically converts the messages that arrive on the HTTP stream into appropriate Event objects, delivering them to the event handlers that have been registered for the events' type if known, or to the onmessage event handler if no type-specific event handler was established.

## HTTP versions (and three-way handshake)

### `HTTP/0.9` - The One Liner (1991)

It was the simplest protocol ever.
Having a single method called GET. If a client had to access some webpage on the server, it would have made the simple request like below

```
GET /index.html
```

And the response from server would have looked as follows

```
(response body)
(connection closed)
```

That is, the server would get the request, reply with the HTML in response and as soon as the content has been transferred, the connection will be closed. There were:

* No headers
  
* `GET` was the only allowed method

* Response had to be HTML

As you can see, the protocol really had nothing more than being a stepping stone for what was to come.


### `HTTP/1.0` - 1996

In 1996, the next version of HTTP i.e. `HTTP/1.0` evolved that vastly improved over the original version.

Unlike `HTTP/0.9` which was only designed for HTML response, `HTTP/1.0` could now deal with other response formats i.e. images, video files, plain text or any other content type as well. It added more methods (i.e. `POST` and `HEAD`), request/response formats got changed, HTTP headers got added to both the request and responses, status codes were added to identify the response, character set support was introduced, multi-part types, authorization, caching, content encoding and more was included.

Here is how a sample `HTTP/1.0` request and response might have looked like:

```
GET / HTTP/1.0
Host: kamranahmed.info
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5)
Accept: */*
```

As you can see, alongside the request, client has also sent it’s personal information, required response type etc. While in `HTTP/0.9` client could never send such information because there were no headers.

Example response to the request above may have looked like below:

```
HTTP/1.0 200 OK 
Content-Type: text/plain
Content-Length: 137582
Expires: Thu, 05 Dec 1997 16:00:00 GMT
Last-Modified: Wed, 5 August 1996 15:55:28 GMT
Server: Apache 0.84

(response body)
(connection closed)
```

In the very beginning of the response there is `HTTP/1.0` (HTTP followed by the version number), then there is the status code 200 followed by the reason phrase (or description of the status code, if you will).

In this newer version, request and response headers were still kept as ASCII encoded, but the response body could have been of any type i.e. image, video, HTML, plain text or any other content type. So, now that server could send any content type to the client; not so long after the introduction, the term “Hyper Text” in HTTP became misnomer. HMTP or Hypermedia transfer protocol might have made more sense but, I guess, we are stuck with the name for life.

**One of the major drawbacks of `HTTP/1.0` were you couldn’t have multiple requests per connection**. That is, whenever a client will need something from the server, it will have to open a new TCP connection and after that single request has been fulfilled, connection will be closed. And for any next requirement, it will have to be on a new connection. Why is it bad? Well, let’s assume that you visit a webpage having 10 images, 5 stylesheets and 5 javascript files, totalling to 20 items that needs to fetched when request to that webpage is made. Since the server closes the connection as soon as the request has been fulfilled, there will be a series of 20 separate connections where each of the items will be served one by one on their separate connections. **This large number of connections results in a serious performance hit as requiring a new TCP connection imposes a significant performance penalty because of three-way handshake followed by slow-start.**

### **Three-way Handshake**

Three-way handshake in it’s simples form is that all the TCP connections begin with a three-way handshake in which the client and the server share a series of packets before starting to share the application data.

* `SYN` - Client picks up a random number, let’s say **x**, and sends it to the server.

* `SYN ACK` - Server acknowledges the request by sending an **ACK** packet back to the client which is made up of a random number, let’s say **y** picked up by server and the number **x+1** where **x** is the number that was sent by the client

* `ACK` - Client increments the number **y** received from the server and sends an ACK packet back with the number **y+1**

![](./assets/img/threewayHandshake.png)

> Please note that there is a **minor issue** with the image, the last ACK packet sent by the client to end the handshake contains only y+1 i.e. **it should have been ACK:y+1 instead of ACK: x+1, y+1**

However, some implementations of `HTTP/1.0` tried to overcome this issue by introducing a new header called `Connection: keep-alive` which was meant to tell the server “Hey server, do not close this connection, I need it again”. But still, it wasn’t that widely supported and the problem still persisted.

Apart from being connectionless, **HTTP** also is a stateless protocol i.e. server doesn’t maintain the information about the client and so each of the requests has to have the information necessary for the server to fulfill the request on it’s own without any association with any old requests. And so this adds fuel to the fire i.e. apart from the large number of connections that the client has to open, it also has to send some redundant data on the wire causing increased bandwidth usage.

### `HTTP/1.1` - 1999

After merely 3 years of `HTTP/1.0`, the next version i.e. `HTTP/1.1` was released in 1999; which made alot of improvements over it’s predecessor. The major improvements over `HTTP/1.0` included:

* **New HTTP methods** were added, which introduced `PUT`, `PATCH`, `OPTIONS`, `DELETE`

* **Hostname Identification** In `HTTP/1.0` Host header wasn’t required but `HTTP/1.1` made it required.

* **Persistent Connections** As discussed above, in `HTTP/1.0` there was only one request per connection and the connection was closed as soon as the request was fulfilled which resulted in accute performance hit and latency problems. `HTTP/1.1` introduced the persistent connections i.e. **connections weren’t closed by default** and were kept open which allowed multiple sequential requests. *To close the connections*, the header `Connection: close` had to be available on the request. **Clients usually send this header in the last request to safely close the connection**.

* **Pipelining** It also introduced the support for pipelining, where the client could send multiple requests to the server without waiting for the response from server on the same connection and server had to send the response in the same sequence in which requests were received. But how does the client know that this is the point where first response download completes and the content for next response starts, you may ask! Well, to solve this, there must be `Content-Length` header present which clients can use to identify where the response ends and it can start waiting for the next response.

> It should be noted that in order to benefit from persistent connections or pipelining, `Content-Length` header must be available on the response, because this would let the client know when the transmission completes and it can send the next request (in normal sequential way of sending requests) or start waiting for the the next response (when pipelining is enabled).

> But there was still an issue with this approach. And that is, what if the data is dynamic and server cannot find the content length before hand? Well in that case, you really can’t benefit from persistent connections, could you?! In order to solve this `HTTP/1.1` introduced chunked encoding. In such cases server may omit content-Length in favor of chunked encoding (more to it in a moment). However, if none of them are available, then the connection must be closed at the end of request.

* **Chunked Transfers** In case of dynamic content, when the server cannot really find out the `Content-Length` when the transmission starts, it may start sending the content in pieces (chunk by chunk) and add the `Content-Length` for each chunk when it is sent. And when all of the chunks are sent i.e. whole transmission has completed, it sends an empty chunk **i.e. the one with `Content-Length` set to zero in order to identify the client that transmission has completed**. In order to notify the client about the chunked transfer, server includes the header:

    > `Transfer-Encoding: chunked`

* Unlike `HTTP/1.0` which had Basic authentication only, `HTTP/1.1` included digest and proxy authentication

* Caching

* Byte Ranges

* Character sets

* Language negotiation

* Client cookies

* Enhanced compression support

* New status codes

* ..and more

`HTTP/1.1` was introduced in 1999 and it had been a standard for many years. Although, it improved alot over it’s predecessor; with the web changing everyday, it started to show it’s age. Loading a web page these days is more resource-intensive than it ever was. A simple webpage these days has to open more than 30 connections. Well `HTTP/1.1` has persistent connections, then why so many connections? you say! The reason is, in `HTTP/1.1` it can only have one outstanding connection at any moment of time. `HTTP/1.1` tried to fix this by introducing pipelining but it didn’t completely address the issue because of the **head-of-line blocking** where a slow or heavy request may block the requests behind and once a request gets stuck in a pipeline, it will have to wait for the next requests to be fulfilled. To overcome these shortcomings of `HTTP/1.1`, the developers started implementing the workarounds, for example use of spritesheets, encoded images in CSS, single humungous CSS/Javascript files, domain sharding etc.

### `SPDY` - 2009

Google went ahead and started experimenting with alternative protocols to make the web faster and improving web security while reducing the latency of web pages. In 2009, they announced `SPDY`.

> `SPDY` is a trademark of Google and isn’t an acronym.

It was seen that if we keep increasing the bandwidth, the network performance increases in the beginning but a point comes when there is not much of a performance gain. But if you do the same with latency i.e. if we keep dropping the latency, there is a constant performance gain. This was the core idea for performance gain behind `SPDY`, decrease the latency to increase the network performance.

> For those who don’t know the difference, latency is the delay i.e. how long it takes for data to travel between the source and destination (measured in milliseconds) and bandwidth is the amount of data transfered per second (bits per second).

The features of `SPDY` included, multiplexing, compression, prioritization, security etc. I am not going to get into the details of `SPDY`, as you will get the idea when we get into the nitty gritty of `HTTP/2` in the next section as I said `HTTP/2` is mostly inspired from `SPDY`.

`SPDY` didn’t really try to replace HTTP; it was a translation layer over HTTP which existed at the application layer and modified the request before sending it over to the wire. It started to become a defacto standards and majority of browsers started implementing it.

> **In 2015, at Google, they didn’t want to have two competing standards and so they decided to merge it into HTTP while giving birth to HTTP/2 and deprecating SPDY.**

### `HTTP/2` - 2015

By now, you must be convinced that why we needed another revision of the HTTP protocol. `HTTP/2` **was designed for low latency transport of content**. The key features or differences from the old version of `HTTP/1.1` include

* Binary instead of Textual

* Multiplexing - Multiple asynchronous HTTP requests over a single connection

* Header compression using HPACK

* Server Push - Multiple responses for single request

* Request Prioritization

* Security

![](./assets/img/http2sheme.png)

1. **Binary Protocol**

    `HTTP/2` tends to address the issue of increased latency that existed in `HTTP/1.x` by making it a binary protocol. Being a binary protocol, it easier to parse but unlike `HTTP/1.x` it is no longer readable by the human eye. **The major building blocks of `HTTP/2` are Frames and Streams**

    **Frames and Streams:**

    **HTTP messages are now composed of one or more `frames`**. There is a `HEADERS` frame for the meta data and `DATA` frame for the payload and there exist several other types of frames (`HEADERS`, `DATA`, `RST_STREAM`, `SETTINGS`, `PRIORITY` etc) that you can check through the `HTTP/2` specs.

    Every `HTTP/2` request and response is given a unique stream ID and it is divided into frames. Frames are nothing but binary pieces of data. **A collection of frames is called a `Stream`**. Each frame has a stream id that identifies the stream to which it belongs and each frame has a common header. Also, apart from stream ID being unique, it is worth mentioning that, any request initiated by client uses odd numbers and the response from server has even numbers stream IDs.

    Apart from the `HEADERS` and `DATA`, another frame type that I think worth mentioning here is **`RST_STREAM` which is a special frame type that is used to abort some stream** i.e. client may send this frame to let the server know that I don’t need this stream anymore. 
    
    > In `HTTP/1.1` the only way to make the server stop sending the response to client was closing the connection which resulted in increased latency because a new connection had to be opened for any consecutive requests. 
    
    > While in `HTTP/2`, client can use `RST_STREAM` and stop receiving a specific stream while the connection will still be open and the other streams will still be in play.

2. **Multiplexing**
   
    Since `HTTP/2` is now a binary protocol and as I said above that it uses frames and streams for requests and responses, once a TCP connection is opened, all the streams are sent asynchronously through the same connection without opening any additional connections. 
    
    And in turn, the server responds in the same asynchronous way i.e. the response has no order and the client uses the assigned stream id to identify the stream to which a specific packet belongs. **This also solves the head-of-line blocking issue that existed in HTTP/1.x** i.e. the client will not have to wait for the request that is taking time and other requests will still be getting processed.

3. **HPACK Header Compression**
   
    It was part of a separate RFC which was specifically aimed at optimizing the sent headers. The essence of it is that when we are constantly accessing the server from a same client there is alot of redundant data that we are sending in the headers over and over, and sometimes there might be cookies increasing the headers size which results in bandwidth usage and increased latency. To overcome this, `HTTP/2` introduced header compression.

    ![](./assets/img/HPAC.png)

    Unlike request and response, headers are not compressed in `gzip` or `compress` etc formats but there is a different mechanism in place for header compression which is literal values are encoded using Huffman code and a headers table is maintained by the client and server and both the client and server omit any repetitive headers (e.g. user agent etc) in the subsequent requests and reference them using the headers table maintained by both.

    While we are talking headers, let me add here that the headers are still the same as in `HTTP/1.1`, except for the addition of some pseudo headers i.e. `:method`, `:scheme`, `:host` and `:path`

4. **Server Push**

    Server push is another tremendous feature of `HTTP/2` where the server, knowing that the client is going to ask for a certain resource, can push it to the client without even client asking for it. For example, let’s say a browser loads a web page, it parses the whole page to find out the remote content that it has to load from the server and then sends consequent requests to the server to get that content.

    Server push allows the server to decrease the roundtrips by pushing the data that it knows that client is going to demand. How it is done is, server sends a special frame called `PUSH_PROMISE` notifying the client that, “Hey, I am about to send this resource to you! Do not ask me for it.” The `PUSH_PROMISE` frame is associated with the stream that caused the push to happen and it contains the promised stream ID i.e. the stream on which the server will send the resource to be pushed.

5. **Request Prioritization**

    A client can assign a priority to a stream by including the prioritization information in the `HEADERS` frame by which a stream is opened. At any other time, client can send a `PRIORITY` frame to change the priority of a stream.

    Without any priority information, server processes the requests asynchronously i.e. without any order. If there is priority assigned to a stream, then based on this prioritization information, server decides how much of the resources need to be given to process which request.

6. **Security**

    There was extensive discussion on whether security (through `TLS`) should be made mandatory for `HTTP/2` or not. In the end, it was decided not to make it mandatory. However, most vendors stated that they will only support `HTTP/2` when it is used over `TLS`. So, although `HTTP/2` doesn’t require encryption by specs but it has kind of become mandatory by default anyway. With that out of the way, `HTTP/2` when implemented over `TLS` does impose some requirements i.e. `TLS` version 1.2 or higher must be used, there must be a certain level of minimum keysizes, ephemeral keys are required etc.

    `HTTP/2` is here and it has already surpassed `SPDY` in adaption which is gradually increasing. `HTTP/2` has a lot to offer in terms of performance gain and it is about time we should start using it.

## Conclusion

HTTP is an extensible protocol that is easy to use. The client-server structure, combined with the ability to add headers, allows HTTP to advance along with the extended capabilities of the Web.