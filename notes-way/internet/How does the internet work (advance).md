# This article cover [Stanford article about it](http://web.stanford.edu/class/msande91si/www-spr04/readings/week1/InternetWhitepaper.htm)

## Internet addresses

Because the Internet is a global network of computers each computer connected to the Internet must have a unique address.

Internet addresses are in the form `nnn.nnn.nnn.nnn`.

Each `nnn` segment must be a number from 0 - 255.

This address is known as an **IP address**.

If you connect to the Internet through an Internet Service Provider (ISP), you are usually assigned a temporary IP address for the duration of your dial-in session. If you connect to the Internet from a LAN your computer might have a permanent IP address or it might obtain a temporary one from a DHCP  server. *In any case, if you are connected to the Internet, your computer has a unique IP address.*

Terminology:
> **LAN** - Local Area Network 
> 
> **DHCP** - Dynamic Host Configuration Protocol

## Protocol Stacks and Packets

So your computer is connected to the Internet and has a unique address. How does it 'talk' to other computers connected to the Internet? An example should serve here: Let's say your IP address is 1.2.3.4 and you want to send a message to the computer 5.6.7.8. The message you want to send is "Hello computer 5.6.7.8!". Obviously, the message must be transmitted over whatever kind of wire connects your computer to the Internet. Let's say you've dialed into your ISP from home and the message must be transmitted over the phone line. Therefore the message must be translated from alphabetic text into electronic signals, transmitted over the Internet, then translated back into alphabetic text. How is this accomplished?

> **Answer:** Through the use of a **protocol stack**.
 
Every computer needs one to communicate on the Internet and it is usually built into the computer's operating system (i.e. Windows, Unix, etc.). The protocol stack used on the Internet is refered to as the **TCP/IP protocol** stack because of the two major communication protocols used. 

The TCP/IP stack looks like this:

1. **Application Protocols Layer** - protocols specific to applications such as WWW, e-mail, FTP, etc
2. **Transmission Control Protocol Layer (TCP)** - TCP directs packets to a specific application on a computer using a port number
3. **Internet Protocol Layer (IP)** - IP directs packets to a specific computer using an IP address
4. **Hardware Layer** - Converts binary packet data to network signals and back. (E.g. ethernet network card, modem for phone lines, etc.)

If we were to follow the path that the message "Hello computer 5.6.7.8!" took from our computer to the computer with IP address 5.6.7.8, it would happen something like this:

![](./assets/img/ruswp_diag2.gif)

1. The message would start at the top of the protocol stack on your computer and work it's way downward.
   
2. If the message to be sent is long, each stack layer that the message passes through may break the message up into smaller chunks of data. This is because data sent over the Internet (and most computer networks) are sent in manageable chunks. On the Internet, these chunks of data are known as **packets**.
   
3. The packets would go through the Application Layer and continue to the TCP layer. Each packet is assigned a **port number**. Ports will be explained later, but suffice to say that many programs may be using the TCP/IP stack and sending messages. We need to know which program on the destination computer needs to receive the message because it will be listening on a specific port.
   
4. After going through the TCP layer, the packets proceed to the IP layer. This is where each packet receives it's destination address, 5.6.7.8.
   
5. Now that our message packets have a port number and an IP address, they are ready to be sent over the Internet. The hardware layer takes care of turning our packets containing the alphabetic text of our message into electronic signals and transmitting them over the phone line.
   
6. On the other end of the phone line your ISP has a direct connection to the Internet. The ISPs router examines the destination address in each packet and determines where to send it. Often, the packet's next stop is another router. More on routers and Internet infrastructure later.
   
7. Eventually, the packets reach computer 5.6.7.8. Here, the packets start at the bottom of the destination computer's TCP/IP stack and work upwards.
   
8. As the packets go upwards through the stack, all routing data that the sending computer's stack added (such as IP address and port number) is stripped from the packets.
   
9.  When the data reaches the top of the stack, the packets have been re-assembled into their original form, "Hello computer 5.6.7.8!"

Terminology:
> **ISP** - Internet service provider
> 
> **TCP** - Transmission Control Protocol
> 
> **IP** - Internet protocol
> 
> **packets** - chunks of data transmitted over the Internet (assembled raw data, which is then re-assembled again)

## Networking Infrastructure

So now you know how packets travel from one computer to another over the Internet. But what's in-between? What actually makes up the Internet? Let's look at another diagram:

![](./assets/img/ruswp_diag3.gif)

The physical connection through the phone network to the Internet Service Provider might have been easy to guess, but beyond that might bear some explanation.

The ISP maintains a pool of modems for their dial-in customers. This is managed by some form of computer (usually a dedicated one) which controls data flow from the modem pool to a backbone or dedicated line router. This setup may be refered to as a port server, as it 'serves' access to the network. Billing and usage information is usually collected here as well.

After your packets traverse the phone network and your ISP's local equipment, they are routed onto the ISP's backbone or a backbone the ISP buys bandwidth from. From here the packets will usually journey through several routers and over several backbones, dedicated lines, and other networks until they find their destination, the computer with address 5.6.7.8

For example let's check route to www.google.com
```
$ traceroute www.google.com

1  XiaoQiang (192.168.31.1)  1.196 ms  1.304 ms  1.295 ms
2  192.168.100.1 (192.168.100.1)  2.277 ms  2.387 ms  2.379 ms
3  ip92-101-242-1.onego.ru (92.101.242.1)  5.239 ms  5.230 ms  5.220 ms
4  212.48.194.56 (212.48.194.56)  5.212 ms  5.487 ms  5.478 ms
5  185.140.148.19 (185.140.148.19)  7.989 ms 7.425 ms  7.701 ms
6  * * *
7  87.226.194.47 (87.226.194.47)  9.522 ms  9.513 ms  10.470 ms

...

18  * * *
19  * * *
20  lr-in-f147.1e100.net (209.85.233.147)  10.435 ms * *
```
Most have long names such as sjc2-core1-h2-0-0.atlas.digex.net and fddi0-0.br4.SJC.globalcenter.net. These are Internet routers that decide where to send your packets. Several routers are shown in Diagram 3, but only a few. Diagram 3 is meant to show a simple network structure. The Internet is much more complex.

## Internet Infrastructure

The Internet backbone is made up of many large networks which interconnect with each other. These large networks are known as **Network Service Providers** or **NSPs**. Some of the large NSPs are UUNet, CerfNet, IBM, BBN Planet, SprintNet, PSINet, as well as others. 

These networks **peer** with each other to exchange packet traffic. Each NSP is required to connect to three **Network Access Points** or **NAPs**. At the NAPs, packet traffic may jump from one NSP's backbone to another NSP's backbone.

NSPs also interconnect at **Metropolitan Area Exchanges** or **MAEs**. MAEs serve the same purpose as the NAPs but are privately owned. NAPs were the original Internet interconnect points. Both NAPs and MAEs are referred to as Internet Exchange Points or IXs.

NSPs also sell bandwidth to smaller networks, such as ISPs and smaller bandwidth providers. Below is a picture showing this hierarchical infrastructure.

![](./assets/img/ruswp_diag4.gif)

This is not a true representation of an actual piece of the Internet. Diagram is only meant to demonstrate how the NSPs could interconnect with each other and smaller ISPs

Most NSPs publish maps of their network infrastructure on their web sites and can be found easily.

To draw an actual map of the Internet would be nearly impossible due to it's size, complexity, and ever changing structure.


Terminology:
> **NSP** - Network Service Provider. The Internet backbone is made up of many large networks which interconnect with each other. They sell bandwidth to smaller networks, such as ISPs and smaller bandwidth providers
> 
> **NAP** - Network Access Point. Networks **peer** with each other to exchange packet traffic. At the NAPs, packet traffic may jump from one NSP's backbone to another NSP's backbone.
> 
> **MAE** - Metropolitan Area Exchanges. MAEs serve the same purpose as the NAPs but are privately owned

## The Internet Routing Hierarchy

So how do packets find their way across the Internet? The information used to get packets to their destinations are contained in routing tables kept by each router connected to the Internet.

Routers are packet switches. A router is usually connected between networks to route packets between them. Each router knows about it's sub-networks and which IP addresses they use. The router usually doesn't know what IP addresses are 'above' it. The black boxes connecting the backbones are routers. The larger NSP backbones at the top are connected at a NAP. Under them are several sub-networks, and under them, more sub-networks. At the bottom are two local area networks with computers attached.

![](./assets/img/ruswp_diag5.gif)

When a packet arrives at a router, the router examines the IP address put there by the IP protocol layer on the originating computer. The router checks it's routing table. If the network containing the IP address is found, the packet is sent to that network. If the network containing the IP address is not found, then the router sends the packet on a default route, usually up the backbone hierarchy to the next router. Hopefully the next router will know where to send the packet. If it does not, again the packet is routed upwards until it reaches a NSP backbone. The routers connected to the NSP backbones hold the largest routing tables and here the packet will be routed to the correct backbone, where it will begin its journey 'downward' through smaller and smaller networks until it finds it's destination.

## Domain Names and Address Resolution

But what if you don't know the IP address of the computer you want to connect to? What if the you need to access a web server referred to as www.anothercomputer.com? How does your web browser know where on the Internet this computer lives? The answer to all these questions is the **Domain Name Service** or **DNS**. The DNS is a distributed database which keeps track of computer's names and their corresponding IP addresses on the Internet.

Many computers connected to the Internet host part of the DNS database and the software that allows others to access it. These computers are known as DNS servers. No DNS server contains the entire database; they only contain a subset of it. If a DNS server does not contain the domain name requested by another computer, the DNS server re-directs the requesting computer to another DNS server.

![](./assets/img/ruswp_diag6.gif)

The Domain Name Service is structured as a hierarchy similar to the IP routing hierarchy. The computer requesting a name resolution will be re-directed 'up' the hierarchy until a DNS server is found that can resolve the domain name in the request. Figure illustrates a portion of the hierarchy. At the top of the tree are the domain roots. Some of the older, more common domains are seen near the top. What is not shown are the multitude of DNS servers around the world which form the rest of the hierarchy.

When an Internet connection is setup (e.g. for a LAN or Dial-Up Networking in Windows), one primary and one or more secondary DNS servers are usually specified as part of the installation. This way, any Internet applications that need domain name resolution will be able to function correctly. For example, when you enter a web address into your web browser, the browser first connects to your primary DNS server. After obtaining the IP address for the domain name you entered, the browser then connects to the target computer and requests the web page you wanted.

Terminology:
> **DNS** - Domain Name Service. It's a distributed database which keeps track of computer's names and their corresponding IP addresses on the Internet.

## Internet Protocols Revisited

As hinted to earlier in the section about protocol stacks, one may surmise that there are many protocols that are used on the Internet. This is true; there are many communication protocols required for the Internet to function. These include the TCP and IP protocols, routing protocols, medium access control protocols, application level protocols, etc. The following sections describe some of the more important and commonly used protocols on the Internet. Higher level protocols are discussed first, followed by lower level protocols.

## Application Protocols: HTTP and the World Wide Web

One of the most commonly used services on the Internet is the **World Wide Web (WWW)**. The application protocol that makes the web work is **Hypertext Transfer Protocol** or **HTTP**. Do not confuse this with the **Hypertext Markup Language (HTML)**. HTML is the language used to write web pages. HTTP is the protocol that web browsers and web servers use to communicate with each other over the Internet. It is an application level protocol because it sits on top of the TCP layer in the protocol stack and is used by specific applications to talk to one another. In this case the applications are web browsers and web servers.