## About
This code is a Python program that uses sockets to query the whois information of any domain name entered by the user. Here is a line-by-line explanation of what the code does:
## **Importing the socket module**
- The first line imports the socket module, which provides access to the low-level network interface in Python.
- The second line asks the user to enter a domain name, such as `python.org`, and converts it to lowercase.
- The next four lines remove any unwanted characters from the domain name, such as `http://`, `https://`, or `www.`, which are not part of the domain name itself.
- The next line splits the domain name by the dot (`.`) character and takes the last element, which is the top-level domain (TLD) of the domain name, such as `org`, `com`, or `net`.
  ## **Getting the user input for the domain name**
- The next six lines define a dictionary that maps some common TLDs to their corresponding whois servers, which are the servers that store the whois information for those domains. For example, the whois server for `org` domains is `whois.pir.org`, and the whois server for `com` and `net` domains is `whois.verisign-grs.com`. The dictionary also has a default value of `whois.iana.org`, which is the whois server for the Internet Assigned Numbers Authority (IANA).
- The next line uses the `get` method of the dictionary to find the whois server for the given TLD, or use the default value if the TLD is not in the dictionary.
- The next line creates a socket object, which is an endpoint of a network communication. The socket object is initialized with two parameters: `socket.AF_INET` and `socket.SOCK_STREAM`. The first parameter specifies the address family of the socket, which is `AF_INET` for IPv4 addresses. The second parameter specifies the socket type, which is `SOCK_STREAM` for TCP sockets.
- The next four lines use a try-except block to handle any errors that may occur during the socket operation. The try block contains the code that performs the socket communication, and the except block handles the `socket.error` exception, which is raised when a socket error occurs.
- The first line in the try block uses the `connect` method of the socket object to establish a connection to the whois server on port 43, which is the standard port for whois protocol. The `connect` method takes a tuple as an argument, which contains the host name and the port number of the server.
- The next line uses the `send` method of the socket object to send the domain name to the whois server, followed by a carriage return (`\r`) and a newline (`\n`) characters, which indicate the end of the request. The `send` method takes a bytes object as an argument, so the domain name is encoded using utf-8 encoding before sending.
- The next line initializes an empty bytes object, which will store the received data from the whois server.
- The next five lines use a while loop to receive all the data from the whois server until the socket is closed. The loop condition is `True`, which means it will run indefinitely until a `break` statement is executed.
- The first line in the loop uses the `recv` method of the socket object to receive up to 4096 bytes of data at a time from the whois server. The `recv` method takes an integer as an argument, which specifies the maximum number of bytes to receive. The `recv` method returns a bytes object, which is assigned to the variable `data`.
- The next line checks if the `data` variable is empty, which means no more data is available from the server. If this is the case, the loop is terminated by a `break` statement.
   ## **Decoding the message object**
- The next line appends the received data to the `msg` object, which accumulates all the data from the server.
- The next line in the try block uses the `close` method of the socket object to close the connection to the whois server. This is a good practice to free up the resources used by the socket.
- The next line decodes the `msg` object to a string using utf-8 encoding, which is the standard encoding for whois information. The decoded string is assigned to the same variable `msg`.
  ## **Printing the whois information**
- The next line prints the `msg` string to the standard output, which is the console by default. The `msg` string contains the whois information of the domain name, such as the registrant, the registrar, the creation date, the expiration date, the name servers, and other details.
- The first line in the except block prints the `socket.error` exception to the standard output, which contains the error message and the error code of the socket error.

## Windows
- A prerequisite for working with a domain is to install whois:

https://learn.microsoft.com/en-us/sysinternals/downloads/whois
## Linux
- Update your .deb repos by running:

`$ sudo apt update`
- Apply any pending security or apps updates to your Linux box:

`$ sudo apt upgrade`

![whois](https://github.com/codes369/Domain/assets/93201875/a6247467-3e55-4d48-ab11-6631b6067446)

- Then install the whois client on Debian or Ubuntu Linux using the apt command or apt-get command:

`$ sudo apt install whois`

![whois](https://github.com/codes369/Domain/assets/93201875/3311628e-dba8-4027-82c4-54a84c4a0ff2)

- Test it using the whois command for IP address lookup. For example:

`whois 142.250.192.78`

`whois 2404:6800:4007:817::200e`

- Then you can also do the domain name lookup. For instance:

`$ whois domain-name-here` 

`$ whois cyberciti.biz`

`$ whois google.com`

`$ whois nixcraft.com`
## License
Copyright (c) Microsoft Corporation. All rights reserved.

Licensed under the MIT license.
