<head>
  <style>
    body {
      font-family: "Georgia", serif;
      text-align: justify;
    }
  </style>
</head>

## Basic XSS

<br>

# 01. Reflected XSS into HTML context with nothing encoded
#### Lab: https://portswigger.net/web-security/cross-site-scripting/reflected/lab-html-context-nothing-encoded
<b>Problem:</b> This lab contains a simple reflected cross-site scripting vulnerability in the search functionality.

To solve the lab, perform a cross-site scripting attack that <b>calls the alert function</b>.

The steps used to perform can be reached below (sequence).
1. https://0ad8005d03f0bcaf805c0d3b00d6003d.web-security-academy.net/
2. https://0ad8005d03f0bcaf805c0d3b00d6003d.web-security-academy.net/?search=a
3. <p>We can inspect elements on the form, since the input shows our input and wraped on <code>h1</code> tag, then we can try <code>'</h1><img src=a onerror=alert(1)></code>https://0ad8005d03f0bcaf805c0d3b00d6003d.web-security-academy.net/?search=%27%3C%2Fh1%3E%3Cimg+src%3Da+onerror%3Dalert%281%29%3E

<br></br>

# 02. Stored XSS into HTML context with nothing encoded
#### Lab: https://portswigger.net/web-security/cross-site-scripting/stored/lab-html-context-nothing-encoded
<b>Problem:</b> This lab contains a stored cross-site scripting vulnerability in the comment functionality.

To solve this lab, submit a comment that <b>calls the alert function when the blog post is viewed</b>.

The steps used to perform can be reached below (sequence).
1. https://0ae800b5046c0f9c82013310008d0098.web-security-academy.net/.
2. https://0ae800b5046c0f9c82013310008d0098.web-security-academy.net/post?postId=4. On this page there are a few form that might injectable or vulnerable.
3. We can explore and try to give value for all forms (https://0ae800b5046c0f9c82013310008d0098.web-security-academy.net/post/comment/confirmation?postId=4).
4. Since we can put comment, then we can try to bypass the tag. Since our comment wraped on paragraph tag, we can try to close the paragraph tag and peform XSS.
I used simple form input, first is the escape script, then the rest are formalities to submit the form.
<!-- ```</p><script>alert(1)</script>``` -->
  &nbsp;&nbsp;&nbsp;1. <code>&lt;/p&gt;&lt;script&gt;alert(1)&lt;/script&gt;</code>
  &nbsp;&nbsp;&nbsp;2. a
  &nbsp;&nbsp;&nbsp;3. a@a
  &nbsp;&nbsp;&nbsp;4. http:a.com

<br></br>

# 03. DOM XSS in <code>document.write</code> sink using source <code>location.search</code>
#### Lab: https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-document-write-sink
<b>Problem:</b> This lab contains a DOM-based cross-site scripting vulnerability in the search query tracking functionality. It uses the JavaScript document.write function, which writes data out to the page. The document.write function is called with data from location.search, which you can control using the website URL.

To solve this lab, perform a cross-site scripting attack that <b>calls the alert function</b>.

The steps used to perform can be reached below (sequence).
1. https://0aa500ea044aa2dc801c217d00f70042.web-security-academy.net/
2. https://0aa500ea044aa2dc801c217d00f70042.web-security-academy.net/?search=a
3. Since our input can be showen on the page, we can inspect that part. Our input wraped on <code>h1</code> tag, we can try to escape it. Same as before, we can use <code>```'</h1><script>alert(1)</script>```</code>. Unfortunately they use sanitation let's try use <code>```'</h1><img src=a onerror=alert(1)>```</code>, but the result is same.
4. Let's inspect, then we can see that our input also placed on <code>img</code> tag, so we can try another trick by adding <code>"</code>. <code>```"><img src=a onerror=alert(1)>```</code> (https://0aa500ea044aa2dc801c217d00f70042.web-security-academy.net/?search=%22%3E%3Cimg+src%3Da+onerror%3Dalert%281%29%3E).

<br></br>

# 04. DOM XSS in <code>innerHTML</code> sink using source <code>location.search</code>
#### Lab: https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-innerhtml-sink
<b>Problem:</b> This lab contains a DOM-based cross-site scripting vulnerability in the search blog functionality. It uses an innerHTML assignment, which changes the HTML contents of a div element, using data from location.search.

To solve this lab, perform a cross-site scripting attack that <b>calls the alert function</b>.

The steps used to perform can be reached below (sequence).
1. https://0aec00df044a71a88021b26400270068.web-security-academy.net/
2. https://0aec00df044a71a88021b26400270068.web-security-academy.net/?search=a
3. Our input wraped on <code>span</code> tag, let's try to use <code>```</span><img src=a onerror=alert(1)>```</code> (https://0aec00df044a71a88021b26400270068.web-security-academy.net/?search=%3C%2Fspan%3E%3Cimg+src%3Da+onerror%3Dalert%281%29%3E), it worked.

<br></br>

# 05. DOM XSS in jQuery anchor href attribute sink using location.search source
#### Lab: https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-jquery-href-attribute-sink
<b>Problem:</b> This lab contains a DOM-based cross-site scripting vulnerability in the submit feedback page. It uses the jQuery library's $ selector function to find an anchor element, and changes its href attribute using data from location.search.

To solve this lab, make the <b>"back" link alert document.cookie</b>.

The steps used to perform can be reached below (sequence).
1. https://0aba009c03f064e2822a42c900d60015.web-security-academy.net/
2. https://0aba009c03f064e2822a42c900d60015.web-security-academy.net/feedback?returnPath=/
3. Since on the previous page the form not returned our input, then we can change for other page such as https://0aba009c03f064e2822a42c900d60015.web-security-academy.net/post?postId=3. 
4. After try to submit the form, our input showed on the page and wraped by paragraph tag, we can try to escape it by using <code>```></p><img src=a onerror=alert(document.cookie)>```</code> on the comment section, and fill the rest to perform attack. However, still nothing, now let's back to the feedback page and inspect it to gain informations.
5. After inspecting, we can see there is script that grab the link and set it to return path, so we can try to change the URL from <code>/</code> to <code>javascript:alert(document.cookie)</code>. This because they're using href, so we can execute this script.