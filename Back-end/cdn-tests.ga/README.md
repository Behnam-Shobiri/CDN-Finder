

 # Reproducing the CDN vulnerabilities

You can see a Demo of our attack in  [`this link`](https://www.youtube.com/watch?v=x26sffsd8fc). Although this demo is for Cloudflare, the attack is similar for all the other CDNs. To reproduce the general overview is that first, we set the origin on insecure configuration (and confirm it with browser). Then we point to the CDN such that it would use the website as the origin. If we can see the CDN-powered website using the modern browser, it means that the CDN accepted the insecure back-end configuration. 
You can find a step-by-step guide on how to configure the CDN and reproduce our result below.

To check our findings or test a specific CDN follow these instructions: 

0. Set up a server with a specific insecure TLS configuration (you can use our code as explained in the server header)
2.  Register a domain name. (we use free domains from [`freenom`](“freenom.com”)).
    

3.  Manage the DNS for the domain to point to your server. Note that if you are using a specific test (such as a subdomain), make sure that the wildcard DNS for (e.g., *.cdn-tests.ga) is set in the DNS. 
    

4.  Set up your websites to have the configuration that you want to test. DH size, cipher suites, certificate. Alternately, you can use cdn-tests.ga and their subdomain (or use their GitHub code to set up your own server).
    

5.  Use a browser to go to the domain name (if you are using cdn-tests.ga each vulnerable subdomain that you want to reproduce). You should be able to see the webpage shows a warning due to insecure configuration (This would act as the origin server for the next step, thus, the back-end connection would be insecure).
    

6.  Configure the CDN to point to the IP/Domain that has the insecure configuration. This step depends on the CDN that you are using. Some CDNs generate a new URL that you can use (which will be enough for the test). Few CDNs (such as Cloudflare) requires changing the DNS server (as was done in the demo)
    

7.  Use a browser to go to the domain name provided with  CDN. You should be able to see the webpage without warning if CDN accepts the insecure configuration. (Although the origin server is insecure in the back-end and the browser did not accept the same insecure configuration (setp4)).

# Server  
The following code is using [`badssl.com`](https://badssl.com/) and the codes that are provided by the same URL. However, there are some changes that  will be explained in the rest. 


There are some subdomains that obviously need valid CA; however, we do not have access to a CA such that it would issue us the malformed certificate. Moreover, we have added some extra test that we did not find in the badssl. These include: 

- Mismatch certificate
- Null certificates (both in SAN and CN field) 
- Revoked certificate 

Obviously, we cannot share the valid certificates and their private key; nevertheless, we have added the guide on how to issue each of them (See [This file](https://github.com/DTRAP2021/CDN-finder/blob/master/Back-end/cdn-tests.ga/Extra_certs.md)).  

Visit [`badssl.com`](https://badssl.com/) and their GitHub page [`badssl-github`](https://github.com/chromium/badssl.com) related to them. 

## Server Setup

If you are using a different URL, grep the configs for cdn-tests.ga and simply replace them. 
Stock Ubuntu VM, DNS A records for `cdn-tests.ga.` and `*.cdn-tests.ga.` pointing to the VM.

Some notes to keep in mind, while we tried to keep the code as generic as we could, you still need to change it if you want to use it for your URL.
 You can use the docker file and we tried to fix the Java version problem that we encounter during our testing; however, this is system-specific and you can check badssl GitHub issues if you still need help. 

### Testing and development

1. Follow the instructions to [install Docker.](https://www.docker.com/get-docker)
2. Clone into the repo.  
3. In order to access the various  subdomains locally you will need to add them to your [system hosts file](https://bencane.com/2013/10/29/managing-dns-locally-with-etchosts/). Run `make list-hosts` and copy and paste the output into `/etc/hosts`.
4. Start Docker by running `make serve`.
5. You can now navigate to `cdn-tests.test` in your browser, and you should see a certificate error.
6. The badssl root certificate is at `certs/sets/test/gen/crt/ca-root.crt`. In order to get the rest of the badssl subdomains working, you will need to add this to your machine's list of trusted certificates.
    - On `macOS`, drag `certs/sets/test/gen/crt/ca-root.crt` into the login section of the program Keychain Access. A Root Certificate Authority entry should appear in the list. Double-click on this entry and select "Always Trust" from the drop-down menu next to "Secure Sockets Layer (SSL)." Close the window to save your changes.

      If you are already familiar with this process, you can instead run this command:

      ```sh
      security add-trusted-cert -r trustRoot -p ssl \
        -k "$HOME/Library/Keychains/login.keychain" certs/sets/test/gen/crt/ca-root.crt
      ```

7. In order to preserve the client and root certificates even after running `make clean`, run:

```sh
cd certs/sets/test
mkdir -p pregen/crt pregen/key
cp gen/crt/ca-root.crt pregen/crt/ca-root.crt
cp gen/crt/client.crt pregen/crt/client.crt
cp gen/crt/client-ca-root.crt pregen/crt/client-ca-root.crt
cp gen/key/ca-root.key pregen/key/ca-root.key
cp gen/key/client.key pregen/key/client.key
cp gen/key/client-ca-root.key pregen/key/client-ca-root.key
```



## Disclaimer

 The website/code and all the certificates are tested; however, they are offered "AS-IS" and without any warranties.

