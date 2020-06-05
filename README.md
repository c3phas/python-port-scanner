#### A basic implementation of a port scanner in python
The program will such for open ports in the specified target.
If the port is well known its service will be listed as well.

#### TODO
**ERROR HANDLING ON THE SOCKET FUNCTION**
This program will make use of threads to improve the speed of the scan.
The default ports are set to *1-1024* and the default host is *localhost* ie
to scan your own machine for open ports between 1-1024 run
**python3 portScanner.py**

To specify the Target(host) use the option -T <host> and to specify the port range iuse -p <port>
 *note the -p option will run all the ports between 1 and what you specify*

