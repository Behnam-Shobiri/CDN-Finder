
"""
This simple project is finding a given website CDN 
We are now covering 26 diffrent CDN I would add new CDNs as I find them you can also email me or 
creat issue in the github if you are aware of any other CDN.
for the most updated version see my github page

All rights all reserved for the creator and Madiba Security Lab 
happy hacking!
"""

def DNS_REV(IP_ADD):
    import socket
    status=-1
    try:
        reversed_dns = socket.gethostbyaddr(IP_ADD)
        status =1
    except:
        reversed_dns=[0,0,IP_ADD]
        status=-1
    finally:
        return reversed_dns[0],status

        
def Normal_DNS(Domain):
    import dns.resolver
    IP_list = []
    status =1
    try:
        answer=dns.resolver.query(Domain, "A")
        for data in answer:
            IP_list.append(data.address)
    except:
        status = -1
    finally:
        return IP_list, status

# The DNS server may limit the CNAME visibility
def Find_DNS_CNAME(Domain):
    import dns.resolver
    CNAME_list = []
    status = -1
    try:
        answer=dns.resolver.query(Domain,"CNAME")
        for data in answer:
            CNAME_list.append(data.target)
        status = 1
    except:
        status = -1
    finally:
        return CNAME_list, status


def Read_keys_values(file_name):
    keys_values = []
    import csv
    with open(file_name, mode='r') as keys:
        csv_reader = csv.reader(keys,delimiter=',')
        for row in csv_reader:
            keys_values.append(list((str(row[0]),str(row[1]).strip())))
    
    return keys_values


def Find_with_DNS_Reverse(DNS_Reverse_response):
    status = -1
    print ("DNS reverse is:", DNS_Reverse_response)
    for row in reverse_DNS_values:

        #the 0 index is the key and the 1 index is the value we need to search for
        if DNS_Reverse_response.lower().find(row[1]) != -1: 
            print("Find with DNS Reverse and the CDN is:", row[0])
            print ("Matched with the following DNS Reverse of the CDN", row[1])
            status =1
            return status

    return status


def Find_with_CNAME(CNAME):
    status = -1
    print ("Cname is :", CNAME)
    for row in CNAME_values:
        
        #the 0 index is the key and the 1 index is the value we need to search for
        if CNAME.lower().find(row[1]) != -1: 
            print("Find with CNAME and the CDN is:", row[0])
            print ("Matched with the following CNAME of the CDN", row[1])
            status = 1
            return status
        
    return status
    

def Get_Headers(Domain): # domain should be WITHOUT protocol (e.g. http)
    import requests
    status =-1
    response = -1
    try:
        response = requests.get('https://' + Domain,allow_redirects= True)
        status =1
    except:
        try:
            response = requests.get( 'http://' +Domain,allow_redirects= True)
        except Exception as error:
            status =-1 
            print (error.args)
            raise Exception

    return response,status


def Find_With_Headers(response):
    status = -1
    server_header_value = ""
    #print (response.headers)
    if 'Server' in response.headers:
        print("server header is :", response.headers['Server'])
        server_header_value = response.headers['Server']
        for row in HTTP_header_server:
            if response.headers['Server'].lower().find(row[1].lower()) != -1:
                print("Find with Headers and the CDN is:", row[0])
                print ("Matched with the following Header of the CDN Server:", row[1])
                print (server_header_value)
                status =1
                return status

    for row in HTTP_header:
        if str(row[1]) in response.headers:
            print("Find with Headers and the CDN is:", row[0])
            print ("Matched with the following Header of the CDN ", row[1])
            status =1
            return status

    return status

def Find_CDN_for_domain(domain):

    (IP_list, IP_Status) = Normal_DNS(domain)
    if IP_Status != -1:
        for ip in IP_list:
            print("Domain:",domain,"has IP:",ip)

            #DNS REVERSE CHECK
            print("Checking DNS reverse")
            (reverse,Reverse_status)=DNS_REV(ip)
            Find_with_DNS_Reverse_status =-1
            if Reverse_status != -1:
                Find_with_DNS_Reverse_status=Find_with_DNS_Reverse(reverse)
                # IF WE CAN DISTINGUISH WITH DNS REVERSE
                if Find_with_DNS_Reverse_status != 1:
                    print ("Has DNS reverse but we cannot find ID")
                    print ("the DNS reverse Respond",reverse)
                

            #CNAME CHECK
            print("Checking CNAME")
            (CNAME_list, CNAME_Status) = Find_DNS_CNAME(domain)
            CNAME_number_status = -1
            CNAME =""
            if CNAME_Status != -1:
                for CNAME in CNAME_list:
                    CNAME_number_status =Find_with_CNAME(str(CNAME))
                    if CNAME_number_status != 1:
                        print ("Has CNAME but we cannot find ID")
                        print ("Cname is:", str(CNAME))
            

            #HEADER CHECK
            print("Checking Headers")
            (Header_response, Header_Status)= Get_Headers(domain)
            print(Header_response)
            if Header_Status != -1:
                Find_with_Header_Status=Find_With_Headers(Header_response)
                if Find_with_Header_Status != 1:
                    print("Cannot distinguish with Headers ")
                

def Pop_up_menu():
    domain = input("enter the domain name: \n")
    Find_CDN_for_domain(domain)

#### load the values for features
CNAME_values = Read_keys_values("Features/CNAME.txt")
reverse_DNS_values = Read_keys_values("Features/Reverse_DNS.txt")
HTTP_header_server = Read_keys_values("Features/Server_header.txt")
HTTP_header =  Read_keys_values("Features/HTTP_headers.txt")

Pop_up_menu()




