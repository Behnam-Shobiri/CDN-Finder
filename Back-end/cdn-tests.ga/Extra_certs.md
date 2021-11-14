
# Special Certificates
How to create a certificate depends/varies based on the CA that you are using. We used [LetsEncrypt](letsencrypt.org) using their default configuration (with shell access) on Ubuntu 18.04. 

For NULL certificates you can use the command line and insert "\x00" in the CN to obtain a certificate with the NULL character. If you need to check, you should register the corresponding domain as well. This attack was first presented in Black Hat 2009; for more information see [This Link](https://hackaday.com/2009/07/29/black-hat-2009-breaking-ssl-with-null-characters/)
 For SAN extension, you can use the same process but you should the wild card certificates using [CertBot](https://certbot.eff.org/). Then put the same '\x00" in the SAN extension. Finally, you can confirm it similarly. 

For revoking the certificate using Letsecrypt you can revoke using the private key or the certificate.


If you are using the same account:
```bash
certbot revoke --cert-path /etc/letsencrypt/archive/${YOUR_DOMAIN}/cert1.pem --reason keycompromise
```
If you are using different account: 
```bash
certbot revoke --cert-path /PATH/TO/cert.pem --key-path /PATH/TO/key.pem --reason keycompromise
```

for more info see [This link](https://letsencrypt.org/docs/revoking/)


