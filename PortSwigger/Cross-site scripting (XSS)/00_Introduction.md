<head>
  <style>
    body {
      font-family: "Georgia", serif;
      text-align: justify;
    }
  </style>
</head>

# Penetration Testing Intro.
A Penetration test or pentest is an ethically-driven attempt to test and analyse the security defences to protect these assets and pieces of information. A penetration test involves using the same tools, techniques, and methodologies that someone with malicious intent would use and is similar to an audit.

Hackers are sorted into three hats, where their ethics and motivations behind their actions determine what hat category they are placed into. Let's cover these three in the table below:
| Hat Category       | Description     | Example      |
|-----------|----------|-----------|
| White Hat| Considered the "good people". They remain within the law and use their skills to benefit others.| A penetration tester performing an authorised engagement on a company.|
| Grey Hat| Use their skills to benefit others often; however, they do not respect/follow the law or ethical standards at all times.| Someone taking down a scamming site.|
| Black Hat| Criminals and often seek to damage organisations or gain some form of financial benefit at the cost of others.| Ransomware authors infect devices with malicious code and hold data for ransom.|

#### Rules of Engagement (ROE)
The ROE is a document that is created at the initial stages of a penetration testing engagement. This document consists of three main sections (explained in the table below), which are ultimately responsible for deciding how the engagement is carried out. 

The steps a penetration tester takes during an engagement is known as the methodology. Here's the general theme of stages:
| Stage| Description|
|-----------|----------|
| Information Gathering| Collecting as much publically accessible information about a target/organisation as possible, for example, OSINT and research. <br><b>Note:</b> This does not involve scanning any systems.|
| Enumeration/Scanning| Discovering applications and services running on the systems. For example, finding a web server that may be potentially vulnerable.|
| Exploitation| Leveraging vulnerabilities discovered on a system or application. This stage can involve the use of public exploits or exploiting application logic.|
| Privilege Escalation| Once you have successfully exploited a system or application (known as a foothold), this stage is the attempt to expand your access to a system. You can escalate horizontally and vertically, where horizontally is accessing another account of the same permission group (i.e. another user), whereas vertically is that of another permission group (i.e. an administrator).|
| Post-exploitation| Few sub-stages: <ul>1. What other hosts can be targeted (pivoting)</ul> <ul>2. What additional information can we gather from the host now that we are a privileged user</ul> <ul>3.  Covering your tracks</ul> <ul>4. Reporting</ul>

