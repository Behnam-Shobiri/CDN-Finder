# Welcome to the CDN-Finder Project
When a website is using CDN , there is  connection between the CDN-edge server and end-user (front-end) and connection between the CDN and origin (back-end connection). This project is aim to investigate both front-end connection and back-end connection.

This project was part of the following research paper that investigated security issues in CDNs' connections. You can download the paper for free from ['ACM website'](https://dl.acm.org/doi/10.1145/3499428).

## Overview
Each part has its own ReadMe file which also links to a few demo videos uploaded on Youtube. For more information check it out. Here is an overview of the project. 

### Front-end 
For the front-end connection refer to the [`CDN-Finder`](https://github.com/DTRAP2021/CDN-finder/tree/master/CDN-Finder) directory.
For the front-end connection we want to Identifing the websites that are using a CDN based on the features that we extract. To the best of our knowledge there is no central database for the features; therefore the features can be very helpful for the researchers. Moreover the tool use 4 text file as known features; hence, if it can be easily updated. The tool is very easy to use and there is Demo on how to use the tool.  

### Back-end
The back-end connection is collection of the problems that can go wrong with TLS configuration (see [`back-end`](https://github.com/DTRAP2021/CDN-finder/tree/master/Back-end/cdn-tests.ga)) . There are tests regarding the key exchange (such as Diffe Hellman), cipher suites and certificate related issues. 
We have also added a guide on how to check the back-end connection for the CDNs. Moreover, we create demo for the back-end configurations.  

