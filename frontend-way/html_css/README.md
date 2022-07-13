# A hint summary

* ```<!DOCTYPE html>``` - this tag is required for the browser to understand that we are using HTML5

* **structure versus presentation (`<strong>` and `<em>` VS `<b>` and `<i>`)** - You might be wondering why we’re using the terms “emphasis” and “strong” instead of “italic” and “bold”. That brings us to an important distinction between HTML and CSS. HTML markup should provide semantic information about your content—not presentational information. In other words, **HTML should define the structure of your document, leaving its appearance to CSS**.

    > The pseudo-obsolete `<b>` and `<i>` elements are classic examples of this. They used to stand for “bold” and “italic”, respectively, **but HTML5 attempted to create a clear separation between a document’s structure and its presentation**. Thus, `<i>` was replaced with `<em>`, since emphasized text can be displayed in all sorts of ways aside from being italicized (e.g., in a different font, a different color, or a bigger size). Same for `<b>` and `<strong>`.

* **Empty elements** - Like `<br/>`, `<hr/>` should carry meaning—don’t use it when you just want to display a line for the sake of aesthetics. For that, you’ll want to use the CSS `border` property

    > The `<hr/>` element is a “horizontal rule”, which represents a thematic break. The transition from one scene of a story into the next or between the end of a letter and a postscript are good examples of when a horizontal rule may be appropriate. 