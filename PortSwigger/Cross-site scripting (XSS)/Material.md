<head>
  <style>
    body {
      font-family: "Georgia", serif;
      text-align: justify;
    }
  </style>
</head>

# Which sinks can lead to DOM-XSS vulnerabilities?
#### The following are some of the main sinks that can lead to DOM-XSS vulnerabilities:

<code>
document.write()<br>
document.writeln()<br>
document.domain<br>
element.innerHTML<br>
element.outerHTML<br>
element.insertAdjacentHTML<br>
element.onevent
</code>

#### The following jQuery functions are also sinks that can lead to DOM-XSS vulnerabilities:

<code>
add()<br>
after()<br>
append()<br>
animate()<br>
insertAfter()<br>
insertBefore()<br>
before()<br>
html()<br>
prepend()<br>
replaceAll()<br>
replaceWith()<br>
wrap()<br>
wrapInner()<br>
wrapAll()<br>
has()<br>
constructor()<br>
init()<br>
index()<br>
jQuery.parseHTML()<br>
$.parseHTML()<br>
</code>

#### How to prevent DOM-XSS vulnerabilities
In addition to the general measures described on the DOM-based vulnerabilities page, you should avoid allowing data from any untrusted source to be dynamically written to the HTML document.