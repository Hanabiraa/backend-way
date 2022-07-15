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

### **Block elements and inline elements**

Each HTML element rendered on the screen is a box, and they come in two flavors: “block” boxes and “inline“ boxes.
![](./assets/inline-vs-block-boxes-f3e662.png)

* **Block boxes always appear below the previous block element**. This is the “natural” or “static” flow of an HTML document when it gets rendered by a web browser.

* **The width of block boxes is set automatically based on the width of its parent container**. In this case, our blocks are always the width of the browser window.

* **The default height of block boxes is based on the content it contains.** When you narrow the browser window, the `<h1>` gets split over two lines, and its height adjusts accordingly.

* **Inline boxes don’t affect vertical spacing**. They’re not for determining layout—they’re for styling stuff inside of a block.

* **The width of inline boxes is based on the content it contains**, not the width of the parent element.

### **Changing box behavior**

We can override the default box type of HTML elements with the CSS `display` property. For example, if we wanted to make our `<em>` and `<strong>` elements blocks instead of inline elements, we could update our rule in box-styles.css like so:

```
em, strong {
  background-color: #B2D6FF;
  display: block;  /* default inline */
}
```

### **Content, padding, border, and margin**

* **Content** – The text, image, or other media content in the element.
* **Padding** – The space between the box’s content and its border.
* **Border** – The line between the box’s padding and margin.
* **Margin** – The space between the box and surrounding boxes.

![](./assets/css-box-model-73a525.png)


### **Border like debugging tool**

Borders are common design elements, but they’re also invaluable for debugging. When you’re not sure how a box is being rendered, add a `border: 1px solid red;` declaration to it.

### **Choice between margin and padding**

Margins and padding can accomplish the same thing in a lot of situations, making it difficult to determine which one is the “right” choice. The most common reasons why you would pick one over the other are:

* The padding of a box has a background, while margins are always transparent.
* Padding is included in the click area of an element, while margins aren’t.
* Margins collapse vertically, while padding doesn’t (we’ll discuss this more in the next section).

### **vertical margin collapse**

Another quirk of the CSS box model is the “vertical margin collapse”. When you have two boxes with vertical margins sitting right next to each other, they will collapse. Instead of adding the margins together like you might expect, only the biggest one is displayed.

For example, let’s add a top margin of 25 pixels to our <p> element:

```
p {
  padding: 20px 0 20px 10px;

  margin-top: 25px;
  margin-bottom: 50px;
}
```


Each paragraph should have 50 pixels on the bottom, and 25 pixels on the top. That’s 75 pixels between our <p> elements, right? Wrong! There’s still only going to be 50px between them because the smaller top margin collapses into the bigger bottom one.

This behavior can be very useful when you’re working with a lot of different kinds of elements, and you want to define their layout as the minimum space between other elements.

![](./assets/vertical-margin-collapse-bba78e.png)


### **preventing margin collapse**

It can also be really annoying. Sometimes you do want to prevent the margins from collapsing. All you need to do is put another invisible element in between them:

```
<p>Paragraphs are blocks, too. <em>However</em>, &lt;em&gt; and &lt;strong&gt;
elements are not. They are <strong>inline</strong> elements.</p>

<div style='padding-top: 1px'></div>  <!-- Add this -->

<p>Block elements define the flow of the HTML document, while inline elements
do not.</p>
```

The important part here is that only consecutive elements can collapse into each other. Putting an element with non-zero height (hence the padding-top) between our paragraphs forces them to display both the 25px top margin and the 50px bottom margin.

> Remember that padding doesn’t ever collapse, so an alternative solution would be to use padding to space out our paragraphs instead of the margin property. However, this only works if you’re not using the padding for anything else (at the moment, we are, so let’s stick to the <div> option).

> A third option to avoid margin collapse is to stick to a bottom-only or top-only margin convention. For instance, if all your elements only define a bottom margin, there’s no potential for them to collapse.

> *Finally, the `flexbox layout` scheme doesn’t have collapsing margins, so this isn’t really even an issue for modern websites.*

### **`<div>` and `<span>`**

**Both are “container” elements that don’t have any affect on the semantic structure of an HTML document**. They do, however, provide a hook for adding CSS styles to arbitrary sections of a web page.

*The only real difference between a `<div>` and a `<span>` is that the former is for block-level content while the latter is meant for inline content.*

### ** content boxes and border boxes **

The width and height properties only define the size of a box’s content. Its padding and border are both added on top of whatever explicit dimensions you set. This explains why you’ll get an image that’s 244 pixels wide when you take a screenshot of our button, despite the fact that it has a `width: 200px` declaration attached to it.

![](./assets/box-sizing-content-box-09f48a.png)

Fortunately, CSS lets you change how the width of a box is calculated via the `box-sizing` property. By default, it has a value of `content-box`, which leads to the behavior described above. Let’s see what happens when we change it to `border-box`

This forces the actual width of the box to be 200px—including padding and borders. Of course, this means that the content width is now determined automatically:

![](./assets/box-sizing-border-box-ace2be.png)

### **aligning boxes**

There are three methods for horizontally aligning block-level elements: 
1) `auto-margins` for center alignment
   > When you set the left and right margin of a block-level element to auto, it will center the block in its parent element.

   ```
    margin: 20px auto; /* Vertical  Horizontal */
   ```

2) `floats` for left/right alignment
3) `flexbox` for complete control over alignment. 
  
Yes, unfortunately block-level alignment is totally unrelated to the text-align property.

### **resetting styles**

Different browsers have different default styles for all of their HTML elements, making it difficult to create consistent stylesheets.

It’s usually a good idea to override default styles to a predictable value using the “universal” CSS selector (*).:

```
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
```