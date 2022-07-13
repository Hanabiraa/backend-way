# This article cover some other articles:
1) [What is a URL?](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_URL)

## **Intro**

With Hypertext and HTTP, URL is one of the key concepts of the Web. It is the mechanism used by browsers to retrieve any published resource on the web.

**URL** stands for **Uniform Resource Locator**. A URL is nothing more than the address of a given unique resource on the Web. In theory, each valid URL points to a unique resource. Such resources can be an HTML page, a CSS document, an image, etc.

## **Basic. Anatomy of a URL**

Here are some examples of URLs:

* https://developer.mozilla.org
* https://developer.mozilla.org/en-US/docs/Learn/
* https://developer.mozilla.org/en-US/search?q=URL

Any of those URLs can be typed into your browser's address bar to tell it to load the associated page (resource).

A URL is composed of different parts, some mandatory and others optional. The most important parts are highlighted on the URL below (details are provided in the following sections):

![](./assets/img/mdn-url-all.png)

### **Scheme**

![](./assets/img/mdn-url-protocol%40x2_update.png)

The first part of the URL is the scheme, which indicates the protocol that the browser must use to request the resource (a protocol is a set method for exchanging or transferring data around a computer network). Usually for websites the protocol is HTTPS or HTTP (its unsecured version). Addressing web pages requires one of these two, but browsers also know how to handle other schemes such as `mailto:` (to open a mail client), so don't be surprised if you see other protocols.

### **Authority**

![](./assets/img/mdn-url-authority.png)

Next follows the **authority**, which is separated from the **scheme** by the character pattern `://`. If present the **authority** includes both the domain (e.g. `www.example.com`) and the port (`80`), separated by a colon`:`

* **The domain** indicates which Web server is being requested. Usually this is a domain name, but an IP address may also be used (but this is rare as it is much less convenient).

* **The port** indicates the technical "gate" used to access the resources on the web server. **It is usually omitted if the web server uses the standard ports of the HTTP protocol (80 for HTTP and 443 for HTTPS) to grant access to its resources**. Otherwise it is mandatory.

> Note: The separator between the **scheme** and **authority** is `://`. `The colon` separates the **scheme** from the next part of the URL, while `//` indicates that the next part of the URL is the **authority**.

> One example of a URL that doesn't use an authority is the mail client (`mailto:foobar`). It contains a **scheme** but doesn't use an **authority** component. Therefore, `the colon` is not followed by two slashes and only acts as a delimiter between the **scheme** and mail address.

### **Path to resource**

![](./assets/img/mdn-url-path%40x2.png)

`/path/to/myfile.html` is the path to the resource on the Web server. In the early days of the Web, a path like this represented a physical file location on the Web server. Nowadays, it is mostly an abstraction handled by Web servers without any physical reality.

### **Parameters**

![](./assets/img/mdn-url-parameters%40x2.png)

`?key1=value1&key2=value2` are extra parameters provided to the Web server. Those parameters are a list of key/value pairs separated with the `&` symbol. The Web server can use those parameters to do extra stuff before returning the resource. Each Web server has its own rules regarding parameters, and the only reliable way to know if a specific Web server is handling parameters is by asking the Web server owner.

### **Anchor**

![](./assets/img/mdn-url-anchor%40x2.png)

**#SomewhereInTheDocument** is an anchor to another part of the resource itself. An anchor represents a sort of "bookmark" inside the resource, giving the browser the directions to show the content located at that "bookmarked" spot. On an HTML document, for example, the browser will scroll to the point where the anchor is defined; on a video or audio document, the browser will try to go to the time the anchor represents. It is worth noting that the part after the `#`, also known as the **fragment identifier**, is never sent to the server with the request.

## **Absolute URLs vs relative URLs**

The required parts of a URL depend to a great extent on the context in which the URL is used.

* In your browser's address bar, a URL doesn't have any context, so you must provide a full (or absolute) URL, like the ones we saw above. You don't need to include the protocol (the browser uses HTTP by default) or the port (which is only required when the targeted Web server is using some unusual port), but all the other parts of the URL are necessary.

* When a URL is used within a document, such as in an HTML page, things are a bit different. Because the browser already has the document's own URL, it can use this information to fill in the missing parts of any URL available inside that document. We can differentiate between an absolute URL and a relative URL by looking only at the path part of the URL. If the path part of the URL starts with the `"/"` character, the browser will fetch that resource from the top root of the server, without reference to the context given by the current document.

**Examples of absolute URLs**
|Type|View|Description|
| :---|:---|---|
|**Full URL (the same as the one we used before)**|```https://developer.mozilla.org/en-US/docs/Learn```| - |
|**Implicit protocol**|```//developer.mozilla.org/en-US/docs/Learn``` | In this case, the browser will call that URL with the same protocol as the one used to load the document hosting that URL.|
|**Implicit domain name**|```/en-US/docs/Learn``` | This is the most common use case for an absolute URL within an HTML document. The browser will use the same protocol and the same domain name as the one used to load the document hosting that URL. Note: it isn't possible to omit the domain name without omitting the protocol as well.|

**Examples of relative URLs**

To better understand the following examples, let's assume that the URLs are called from within the document located at the following URL: ```https://developer.mozilla.org/en-US/docs/Learn```

|Type|View|Description|
| :---|:---|---|
|**Sub-resources**|```Skills/Infrastructure/Understanding_URLs```|Because that URL does not start with `/`, the browser will attempt to find the document in a sub-directory of the one containing the current resource. So in this example, we really want to reach this URL: ```https://developer.mozilla.org/en-US/docs/Learn/Skills/Infrastructure/Understanding_URLs.```|
|**Going back in the directory tree**|```../CSS/display``` | In this case, we use the `../` writing convention — inherited from the UNIX file system world — to tell the browser we want to go up from one directory. Here we want to reach this URL: ```https://developer.mozilla.org/en-US/docs/Learn/../CSS/display```, which can be simplified to: ```https://developer.mozilla.org/en-US/docs/CSS/display```.|