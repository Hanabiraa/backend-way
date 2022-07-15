# A hint summary

### ```<!DOCTYPE html>``` 
this tag is required for the browser to understand that we are using HTML5

### **structure versus presentation (`<strong>` and `<em>` VS `<b>` and `<i>`)**

You might be wondering why we’re using the terms “emphasis” and “strong” instead of “italic” and “bold”. That brings us to an important distinction between HTML and CSS. HTML markup should provide semantic information about your content—not presentational information. In other words, **HTML should define the structure of your document, leaving its appearance to CSS**.

> The pseudo-obsolete `<b>` and `<i>` elements are classic examples of this. They used to stand for “bold” and “italic”, respectively, **but HTML5 attempted to create a clear separation between a document’s structure and its presentation**. Thus, `<i>` was replaced with `<em>`, since emphasized text can be displayed in all sorts of ways aside from being italicized (e.g., in a different font, a different color, or a bigger size). Same for `<b>` and `<strong>`.

### **Empty elements**
Like `<br/>`, `<hr/>` should carry meaning—don’t use it when you just want to display a line for the sake of aesthetics. For that, you’ll want to use the CSS `border` property

> The `<hr/>` element is a “horizontal rule”, which represents a thematic break. The transition from one scene of a story into the next or between the end of a letter and a postscript are good examples of when a horizontal rule may be appropriate. 

### **About absolute, relative and root-relative links** 
* It’s possible to use absolute links to refer to pages in your own website, but hard-coding your domain name everywhere can make for some tricky situations. *It’s usually a better idea to reserve absolute links only for directing users to a different website*.

* “Relative” links point to another file in your website from the vantage point of the file you’re editing. It’s implied that the scheme and domain name are the same as the current page, so the only thing you need to supply is the path.
  > Relative links are nice because they let you move around entire folders without having to update all the href’s on your `<a>` elements, but they can get a little confusing when all your links start with a bunch of dots. They’re best for referring to resources in the same folder or in a standalone section of your website.

* “Root-relative” links are similar to the previous section, but instead of being relative to the current page, they’re relative to the “root” of the entire website. For instance, if your website is hosted on our-site.com, all root-relative URLs will be relative to our-site.com.
    > ```<a href='/'>home page</a>``` 

### **Target attribute**
We can use the target attribute to ask the browser to open a link in a new window/tab.

> ```<a href='https://developer.mozilla.org/en-US/docs/Web/HTML' target='_blank'>Mozilla Developer Network</a>```

### **About `<img/>` attrs `width` and `height`**

Setting only one of them will cause the image to scale proportionally, while defining both will stretch the image. **Dimension values are specified in pixels**, and **you should never include a unit (e.g., width='75px' would be incorrect)**

> The width and height attributes can be useful, but it’s usually better to set image dimensions with CSS so you can alter them with media queries.

### **Attribute lang**

A web page’s default language is defined by the lang attribute on the top-level ```<html>``` element. I.e: ```<html lang='en'>```
  
### **Element meta**
`<meta>` element define character set, what the site will use, so use it everything ```<meta charset='UTF-8'```

> These days, UTF-8 is sort of like a universal alphabet for the Internet. Every web page you create should have this line in its `<head>`.

### **About `px` and `em` font size**

The em unit is very useful for defining sizes relative to some base font

```
body {
  font-size: 18px;
}

h1 {
  font-size: 2em; /*36px*/
}

h2 {
  font-size: 1.6em; /*28.8px*/
}
```

> This sets our base font size for the document to 18px, then says that our `<h1>` elements should be twice that size and our `<h2>`’s should be 1.6 times bigger. If we (or the user) ever wanted to make the base font bigger or smaller, em units would allow our entire page to scale accordingly.

### **CSS hierarchy for every web page**

* The browser’s default stylesheet
* User-defined stylesheets
* External stylesheets (that’s us) (css files)
* Page-specific styles (that’s also us) (`<style></style>` tag in html file)
* Inline styles (that could be us, but it never should be) <`style=""` like attr in tag>

This is ordered from least to most precedence, which means styles defined in each subsequent step override previous ones. For example, inline styles will always make the browser ignore its default styles.

*External stylesheets are by far the best place to define the appearance of your website.*

### **Multiple stylesheets**

**The order** of the `<link/>` elements **matters**. Stylesheets that come later will override styles in earlier ones. 

> Typically, you’ll put your “base” or “default” styles in a global stylesheet (styles.css) and supplement them with section-specific stylesheets. **This allows you to organize CSS rules into manageable files while avoiding the perils of page-specific and inline styles**.
