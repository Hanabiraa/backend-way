# This article cover some other articles:
1) [What is DNS? | How DNS works](https://www.cloudflare.com/en-gb/learning/dns/what-is-dns/)

## **Intro**

**The Domain Name System (DNS)** is the phonebook of the Internet. Humans access information online through domain names, like *nytimes.com* or *espn.com*. Web browsers interact through Internet Protocol (IP) addresses. 

> DNS translates domain names to IP addresses so browsers can load Internet resources.

Each device connected to the Internet has a unique IP address which other machines use to find the device. DNS servers eliminate the need for humans to memorize IP addresses such as 192.168.1.1 (in IPv4), or more complex newer alphanumeric IP addresses such as 2400:cb00:2048:1::c629:d7a2 (in IPv6).

## **How does DNS work?**

### **There are 4 DNS servers involved in loading a webpage:**

1) **DNS recursor** - is a server designed to receive queries from client machines through applications such as web browsers. 
    > Typically the recursor is then responsible for making additional requests in order to satisfy the client’s DNS query.

2) **Root nameserver** - The root server is the first step in translating (resolving) human readable host names into IP addresses.
    > Typically it serves as a reference to other more specific locations.

3) **TLD nameserver** - This nameserver is the next step in the search for a specific IP address, and it hosts the last portion of a hostname 
   > (In example.com, the TLD server is “com”).

4) **Authoritative nameserver** - The authoritative nameserver is the last stop in the nameserver query. If the authoritative name server has access to the requested record, it will return the IP address for the requested hostname back to the DNS Recursor that made the initial request.

![](./assets/img/dns-record-request-sequence-1.webp)

### **The 8 steps in a DNS lookup:**

1) A user types *‘example.com’* into a web browser and the query travels into the Internet and is received by a **DNS recursive resolver**.

2) **The resolver** then queries a **DNS root nameserver** (.).

3) **The root server** then responds to the **resolver** with the address of a **Top Level Domain (TLD) DNS server** (such as .com or .net), which stores the information for its domains. When searching for *example.com*, our request is pointed toward the *.com* **TLD**.

4) **The resolver** then makes a request to the *.com* **TLD**.

5) **The TLD server** then responds with the IP address of the domain’s nameserver, *example.com*.

6) Lastly, the **recursive resolver** sends a query to the domain’s nameserver.

7) The IP address for *example.com* is then returned to the **resolver** from the **nameserver**.

8) **The DNS resolver** then responds to the web browser with the IP address of the domain requested initially.

Once the 8 steps of the DNS lookup have returned the IP address for *example.com*, the browser is able to make the request for the web page:

9) The browser makes a HTTP request to the IP address.

10) The server at that IP returns the webpage to be rendered in the browser.

![](./assets/img/dns-lookup-diagram.webp)

### What is a DNS resolver

The DNS resolver is the first stop in the DNS lookup, and it is responsible for dealing with the client that made the initial request. The resolver starts the sequence of queries that ultimately leads to a URL being translated into the necessary IP address.

> Note: A typical uncached DNS lookup will involve both recursive and iterative queries.

### What's the difference between an **recursive DNS query** and **a recursive DNS resolver**?

    > The query refers to the request made to a DNS resolver requiring the resolution of the query. A DNS recursive resolver is the computer that accepts a recursive query and processes the response by making the necessary requests.

![](./assets/img/dns-recursive-query.webp)

### **What are the types of DNS queries?**

In a typical DNS lookup three types of queries occur. By using a combination of these queries, an optimized process for DNS resolution can result in a reduction of distance traveled. In an ideal situation cached record data will be available, allowing a DNS name server to return a non-recursive query.

#### **3 types of DNS queries:**

1) **Recursive query** - In a recursive query, a DNS client requires that a DNS server (typically a **DNS recursive resolver**) will respond to the client with either the requested resource record or an error message if the resolver can't find the record.

2) **Iterative query** - in this situation the DNS client will allow a DNS server to return the best answer it can. If the queried DNS server does not have a match for the query name, it will return a referral to a DNS server authoritative for a lower level of the domain namespace. The DNS client will then make a query to the referral address. This process continues with additional DNS servers down the query chain until either an error or timeout occurs.

3) **Non-recursive query** - typically this will occur when a DNS resolver client queries a DNS server for a record that it has access to either because it's authoritative for the record or the record exists inside of its cache. Typically, a DNS server will cache DNS records to prevent additional bandwidth consumption and load on upstream servers.

### **What is DNS caching? Where does DNS caching occur?**

> The purpose of caching is to temporarily stored data in a location that results in improvements in performance and reliability for data requests. 

**DNS caching** involves storing data closer to the requesting client so that the DNS query can be resolved earlier and additional queries further down the DNS lookup chain can be avoided, thereby improving load times and reducing bandwidth/CPU consumption. DNS data can be cached in a variety of locations, each of which will store DNS records for a set amount of time determined by a **time-to-live (TTL)**.

### **Browser DNS caching**

> Modern web browsers are designed by default to cache DNS records for a set amount of time.

The purpose here is obvious; the closer the DNS caching occurs to the web browser, the fewer processing steps must be taken in order to check the cache and make the correct requests to an IP address. When a request is made for a DNS record, *the browser cache is the first location checked for the requested record*.

In Chrome, you can see the status of your DNS cache by going to chrome://net-internals/#dns.