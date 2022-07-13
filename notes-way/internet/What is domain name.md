# This article cover some other articles:
1) [What is a Domain Name?](hhttps://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_domain_name)

## **Intro**

> Domain names are a key part of the Internet infrastructure. They provide a human-readable address for any web server available on the Internet.

Any Internet-connected computer can be reached through a public IP address, either an **IPv4** address (e.g. `173.194.121.32`) or an **IPv6** address (e.g., `2027:0da8:8b73:0000:0000:8a2e:0370:1337`).

Computers can handle such addresses easily, but people have a hard time finding out who's running the server or what service the website offers. IP addresses are hard to remember and might change over time.

To solve all those problems we use human-readable addresses called domain names.

## **Deeper dive**

### **Structure of domain name**s

A domain name has a simple structure made of several parts (it might be one part only, two, three…), separated by dots and read from right to left:

![](./assets/img/structure.png)

Each of those parts provides specific information about the whole domain name.

#### **TLD (Top-Level Domain)**.

**TLDs** tell users the general purpose of the service behind the domain name. The most generic **TLDs** (`.com`, `.org`, `.net`) don't require web services to meet any particular criteria, but some TLDs enforce stricter policies so it is clearer what their purpose is. For example:

* Local **TLDs** such as `.us`, `.fr`, or `.se` can require the service to be provided in a given language or hosted in a certain country — they are supposed to indicate a resource in a particular language or country.
  
* **TLDs** containing `.gov` are only allowed to be used by government departments.

* The `.edu` **TLD** is only for use by educational and academic institutions.

> TLDs can contain special as well as latin characters. A TLD's maximum length is 63 characters, although most are around 2–3.

#### **Label (or component)**

The labels are what follow the TLD. A label is a case-insensitive character sequence anywhere from one to sixty-three characters in length, containing only the letters A through Z, digits 0 through 9, and the - character (which may not be the first or last character in the label). `a`, `97`, and `hello-strange-person-16-how-are-you` are all examples of valid labels.

> The label **located right** before the TLD is also called a **Secondary Level Domain (SLD)**.

A domain name can have many labels (or components). It is not mandatory nor necessary to have 3 labels to form a domain name. For instance, `www.inf.ed.ac.uk` is a valid domain name. 

> For any domain you control (e.g. `mozilla.org`), you can create "subdomains" with different content located at each, like `developer.mozilla.org`, `iot.mozilla.org`, or `bugzilla.mozilla.org`.