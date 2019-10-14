<h3>A basic implementation of a port scanner in python.</h3>
<p>The program will such for open ports in the specified target.</p>
<p> if the port is well known its service will be listed as well</p>

<h2>TODO</h2>
<b>ERROR HANDLING ON THE SOCKET FUNCTION</b>

<pre>This program will make use of threads to improve the speed of the scan
The default ports are set to 1-1024 and the default host is localhost ie
to scan your own machine for open ports between 1-1024 run
python3 portScanner.py 
</pre>
<b>To specify the Target(host) use the option -T <host> and to specify the port range iuse -p <port></b>
  <b>note the -p option will run all the ports between 1 and what you specify</b>

