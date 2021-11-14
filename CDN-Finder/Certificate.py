from socket import socket
import ssl
import OpenSSL

Is_cloudflare = 0

from  Analyz_certificate import Analyz_certificate

def timer_handler(signum, frame):
    import signal
    print("This website required too much time!")
    raise Exception('end of time')

def timer_init(time_out):
    import signal
    signal.signal(signal.SIGALRM, timer_handler)
    signal.alarm(time_out)

def getCertificate(domain):
    import signal
    timer_time_out = 60 # the time that we would wait for each website in second
    timer_init(timer_time_out)
    try:
        conn = ssl.create_connection((domain, 443))
        context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        sock = context.wrap_socket(conn, server_hostname=domain)
        cert_pem = ssl.DER_cert_to_PEM_cert(sock.getpeercert(True))
    #cert_pem = ssl.get_server_certificate((s, 443))
        cert_der = ssl.PEM_cert_to_DER_cert(cert_pem)
        x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert_pem)
        return x509
    except:
        print(domain)
        return -1
    

def write_to_file(domain,Subjet_CN,Subjet_Organization,Issure_CN,Issure_Organization,signature_algorithm,public_key_ID,public_key_size,extension_type,extention_data):
    import csv
    with open('Test_certificate.csv', mode='a') as Cloudflare:
        website_writer = csv.writer(Cloudflare, delimiter=',', quotechar='"')
        print("We are writing the following in the file Test_certificate" )
        print ("domain: " + domain , " \n Subjet_CN: " + Subjet_CN + "\n Subjet_Organization: " + Subjet_Organization + "\n Issure_CN: " + str(Issure_CN) + "\n Issure_Organization: " + str(Issure_Organization) + "\n signature_algorithm: " + str(signature_algorithm))
        print ("public_key_ID: " + str(public_key_ID) + "\n public_key_ID: " + str(public_key_ID) + "\n public_key_size: " + str(public_key_size)  + "\n extension_type: "+ str(extension_type) + "\n extention_data: "+ str(extention_data)) 
        website_writer.writerow([domain,Subjet_CN,Subjet_Organization,Issure_CN,Issure_Organization,signature_algorithm,public_key_ID,public_key_size,extension_type,extention_data])
        


'''
def get_cloudflare(filename):
    import csv
    Cloudfalre_list = []
    Count_of_websites_using_Cloudflare = 0 
    with open(filename, mode='r') as website_file:
        csv_reader = csv.reader(website_file,delimiter=',')
        for row in csv_reader:
            if int(row[9]) == 1 or int(row[6]) == 1:
                Cloudfalre_list.append(row[1])
                Count_of_websites_using_Cloudflare +=1
    #print(Cloudfalre_list)
    print(Count_of_websites_using_Cloudflare)

    return Cloudfalre_list
'''    

def find_SAN_in_cert(x509):
    extension_count=x509.get_extension_count()
    extension_index=0
    while extension_index < extension_count:
        if str(x509.get_extension(extension_index).get_short_name()).lower().find("subjectAltName".lower()) != -1:
            return extension_index
        else:
            extension_index +=1
    return -1

def Handel_Certificate(x509,domain):
    subject = x509.get_subject()
    issuer = x509.get_issuer()
    signature_algorithm = x509.get_signature_algorithm()
    public_key = x509.get_pubkey()
    public_key_size = public_key.bits()
    public_key_ID= public_key.type()
    SAN_index=find_SAN_in_cert(x509)
    if SAN_index == -1:
        extension_type = "NOT FOUND"
        extention_data = "NOT FOUND"
    else:
        extension_type = x509.get_extension(SAN_index).get_short_name()
        extention_data = x509.get_extension(SAN_index)
    write_to_file(domain,subject.CN,subject.O,issuer.CN,issuer.O,signature_algorithm,public_key_ID,public_key_size,extension_type,extention_data)
    if Is_cloudflare == 1:
            Analyz_certificate(issuer.O,subject.CN, extention_data)
    '''
    print(subject.O)
    print(issuer.CN)
    print(issuer.O)
    print(signature_algorithm)
    print(public_key_ID)
    print(public_key_size)
    '''
    

def Handel_Cert(domain):

    #domain_list=get_from_database("")
    certificate=getCertificate(domain)
    if certificate != -1:
        Handel_Certificate(certificate,domain)
    else:
        print ("testing the domin %s with www" % domain)
        certificate=getCertificate("www."+domain)
        if certificate != -1:
            Handel_Certificate(certificate,domain)
        else:
            print("cannot get the certificate")
            print(domain)
        
        
def Pop_up_menu():

    global Is_cloudflare
    domain = input("enter the domain name: \n")
    cloudflare = str(input("is the website using cloudflare (default is no)? (yes/No)"))

    if cloudflare == "yes":
        Is_cloudflare = 1
    Handel_Cert(domain)


Pop_up_menu()








