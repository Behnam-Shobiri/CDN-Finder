# CDN-Finder
This is a simple python script that finds out if a website is using a known CDN or not. We use 3 different features to detect the websites that are using CDN. The features are: CNAME record in the CDN, reverse DNS, and HTTP headers. 



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

The tool will check all the features and it will show the result for each one. 

## Change in DNS 
The DNS server may choose to limit access to CNAME. Therefore, the website that the tool used to be able to detect, will not be detected. 


## Disclaimer

This tool was meant for our research on Alexa top 1 million websites and the CDNs that they are using. The features may change over time and CDNs may also delete some features. Thus, this tool is offered "AS-IS" and without any warranties.

Notably, some websites may choose to change the CDN that they are using; therefore, the detected CDN can change over time.







