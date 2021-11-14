
list_of_all_CAs = []
def Analyz_cloudflare_ca(CN,SAN):
    if str(CN).lower().find("sni.cloudflaressl.com") != -1 or str(SAN).lower().find("sni.cloudflaressl.com") != -1:
        return 1
    elif str(CN).lower().find("cloudflaressl") != -1 or str(SAN).lower().find("cloudflaressl") != -1:
        return 2
    elif str(CN).lower().find("cloudflare") != -1 or str(SAN).lower().find("cloudflare") != -1:
        print(CN)
        return 3
    else:
        return -1

def Categorize_CA(Issuer_organization):
    find = -1
    for CA in list_of_all_CAs:
        if Issuer_organization in CA:
            CA[1] = int(CA[1]) +1
            find = 1
            break
    if find != 1:
        list_of_all_CAs.append([Issuer_organization,1])

def Analyz_certificate(issure_organization,CN, SAN):

    Cloudflare_CA =0
    Cloudflare_SNI =0
    Other_CA = 0
    Cloudflare_CA_with_cloudflaressl=0
    Cloudflare_CA_with_cloudflare =0
    Other_CA_Cloudflare_SNI =0
    Other_CA_with_cloudflaressl =0 
    Other_CA_with_cloudflare =0

    if str(issure_organization).lower().find("CloudFlare".lower()) != -1:
        Cloudflare_CA +=1
        Cloudflare_CA_Result=Analyz_cloudflare_ca(CN,SAN)
        if Cloudflare_CA_Result ==1:
            print("The certificate was issued by Cloudflare and has the corresponding Cloudflare SNI")
            Cloudflare_SNI +=1
        if Cloudflare_CA_Result ==2:
            print("The certificate was issued by Cloudflare and has the corresponding cloudflaressl CA")
            Cloudflare_CA_with_cloudflaressl +=1
        if Cloudflare_CA_Result ==3:
            print("The certificate was issued by Cloudflare and has the corresponding cloudflare CA")
            Cloudflare_CA_with_cloudflare +=1
    else:
        Other_CA +=1
        Other_CA_Result=Analyz_cloudflare_ca(CN,SAN)
        Categorize_CA(issure_organization) #issure's organization
        if Other_CA_Result ==1:
            print("The certificate was NOT issued by Cloudflare and has the corresponding Cloudflare SNI")
            Other_CA_Cloudflare_SNI +=1
        if Other_CA_Result ==2:
            print("The certificate was NOT issued by Cloudflare and has the corresponding cloudflaressl CA")
            Other_CA_with_cloudflaressl +=1
        if Other_CA_Result ==3:
            print("The certificate was NOT issued by Cloudflare and has the corresponding cloudflare CA")
            Other_CA_with_cloudflare +=1
    
    return Cloudflare_CA,Cloudflare_SNI,Other_CA,Cloudflare_CA_with_cloudflaressl,Other_CA_Cloudflare_SNI,Other_CA_with_cloudflaressl,Cloudflare_CA_with_cloudflare,Other_CA_with_cloudflare

def print_if_more_than_threshold(my_list,threshold):
    tem_my_list = []
    for item in my_list:
        if item[1] > threshold:
            tem_my_list.append(item)
    print(tem_my_list)


def print_all_info():
    
    print ("ALL the Cloudflare_CA certificates are:",Cloudflare_CA)
    print ("ALL the Cloudflare_SNI certificates are:",Cloudflare_SNI)
    print ("ALL the Cloudflare_CA_with_cloudflaressl certificates are:",Cloudflare_CA_with_cloudflaressl)
    print ("ALL the Cloudflare_CA_with_cloudflare certificates are:",Cloudflare_CA_with_cloudflare)

    print ("ALL the Other_CA certificates are:",Other_CA)
    print ("ALL the Other_CA_Cloudflare_SNI certificates are:",Other_CA_Cloudflare_SNI)
    print ("ALL the Other_CA_with_cloudflaressl certificates are:",Other_CA_with_cloudflaressl)
    print ("ALL the Other_CA_with_cloudflare certificates are:",Other_CA_with_cloudflare)

    print_if_more_than_threshold(list_of_all_CAs,100)


'''
line_count += temp_count
Cloudflare_CA +=temp_C_CA
Cloudflare_SNI +=temp_C_SNI
Other_CA +=temp_O_CA
Cloudflare_CA_with_cloudflaressl += temp_Cloudflare_CA_with_cloudflaressl
Other_CA_Cloudflare_SNI+=temp_Cloudflare_CA_with_cloudflaressl
Other_CA_with_cloudflaressl+=temp_Other_CA_with_cloudflaressl
Cloudflare_CA_with_cloudflare += temp_Cloudflare_CA_with_cloudflare 
Other_CA_with_cloudflare += temp_Other_CA_with_cloudflare 

print_all_info()
#file_names = ['Cloudflare11.csv','Cloudflare22.csv','Cloudflare33.csv','Cloudflare44.csv'] #file names
line_count = 0 
Cloudflare_CA =0
Cloudflare_SNI =0
Cloudflare_CA_with_cloudflaressl =0
Other_CA = 0
Other_CA_Cloudflare_SNI =0
Other_CA_with_cloudflaressl =0 
Other_CA_with_cloudflare =0
Cloudflare_CA_with_cloudflare =0
'''
