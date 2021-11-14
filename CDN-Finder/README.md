# CDN-Finder
This is a python script that identifies the websites that are using a known CDN. We used the result of this tool to determine the impact of our finding regarding vulnerabilities in certain CDNs. However, researchers are welcome to use this tool to identify if a website is using certain CDN for any measurements or vulnerability. We use 3 different features to detect the websites that are using CDN. The features are: CNAME record in the CDN, reverse DNS, and HTTP headers. 

A demo of our tool can be found [Here](https://www.youtube.com/watch?v=al0FBobfl9Y).
**To reproduce our finding regarding the connection between the CDN and origin server, check the back-end directory.** 


# Features

There are 4 files as a database. We fill these data with our scan over the top 1 million Alexa websites and clustering the most referred features. Subsequently, we checked to see if these features belong to a CDN and if they are a CDN, we add the features to the files. 

The names of the files are very clear! the CNAME, reverse DNS is showing the data for both of the features. The HTTP headers are using 2 separate files, the "Server_header.txt" one that is for using the `Server` header and "HTTP_headers.txt" is for all the other headers (obviously the headers are unique for each CDN).

You edit the data in the files (it is a simple CSV file). The first value is the CDN and the second one is the value of the feature. If you have multiple values that you wish to add just use multiple entries under the same CDN name. 

If you are aware of more features or more CDNs, you are welcome to open an issue and we will add the data to the files. 



##  Prerequisites 

For the code to work you should install  `dnspython`
You can install it using pip.

## Run
You just need to enter the domain name that you want to check. You should **not** enter the  protocol; i.e. HTTP:// or HTTPS://

`python3 CDN_finder.py`

The tool will check all the features and it will show the result for each one. `CDN_finder.py` is the main file and is used for identifying the CDN. 

# Certificates 

There is the `Certificate.py` file that stores the certificate (also supports the SNI extension). 
This script will work for all the websites and store the certificate in the local database. It will extract/store parts of the certificate that relates to the CDN or can give us some hint about the CDN. We further implement `Analyz_certificate.py` that is used for analyzing the certificate; currently, this file only works with Cloudflare and according to their documentation. Note that we support all the variates that Cloudflare handles the certificate (based on the customers levels). You can make sure that the website is using Cloudflare by using the main file and then turn on this flag for the domain. If you are not sure about the CDN, the default is no for Cloudflare CDN.

## Run


`python3 Certificate.py`


## Change in DNS 
The DNS server may choose to limit access to CNAME. Therefore, the website that the tool used to be able to detect, will not be detected. 


## Disclaimer

This tool was meant for our research on Alexa top 1 million websites and the CDNs that they are using. The features may change over time and CDNs may also delete some features. Thus, this tool is offered "AS-IS" and without any warranties.

Notably, some websites may choose to change the CDN that they are using; therefore, the detected CDN can change over time.
