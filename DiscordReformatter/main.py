import time

def inviteReformat():
    choice = input("Are you wanting to remove the discord.gg/ or add it?").lower()
    while choice not in ("add", "remove"):
        choice = input("Invalid choice. Please use 'add' or 'remove'")
        
    if choice == "add":
        invites = open("invites.txt", 'r')
        inviteCodes = invites.readlines()
        if len(inviteCodes) == 0:
            print("No invites were found in the invites.txt file")
            exit()
        hyperlink = input("Do you want them to be hyperlinked (https://)? 'yes' or 'no'").lower()
        while hyperlink not in ("yes", "no"):
            print("Invalid choice. Please use 'yes' or 'no'")
            hyperlink = input("")
        with open('invitesOutput.txt', 'w') as w:
            for invite in inviteCodes:
                with open('invitesOutput.txt', 'a') as f:
                    if hyperlink == "yes":
                        f.write("https://discord.gg/" + invite)
                    elif hyperlink == "no":
                        f.write("discord.gg/" + invite)
        print("Successfully reformatted invites and saved them to invitesOutput.txt")
        time.sleep(3)
    elif choice == "remove":
        with open ("invites.txt", "r") as inviteremover:
            codes = inviteremover.read()
            if len(codes) == 0:
                print("No invites were found in the invites.txt file")
                exit()
            codes = codes.replace("discord.gg/", "").replace("http://discord.gg/", "").replace("https://discord.gg/", "")
            with open ("invitesOutput.txt", "w") as file:
                file.write(codes)
        print("Successfully reformatted invites and saved them to invitesOutput.txt")
        time.sleep(3)

  
def vccReformatting():
    vccReformatChoice = input("""Which format do you want?
1) [Egyptian VCCs]:

Online Payment Card Details: 
Card value: 1.00 EGP 
Card number: 5170614524050805 
Exp Date: 07/24 
CVC: 168 
Ref number: 340050250 
Card is valid for one use within 24 hours and for local and international websites.
For ET Cash wallet services survey call 77714#

2) [Requested Layout]:

Number
Expiry
CVC
""")
    while vccReformatChoice not in ('1', '2'):
        vccReformatChoice = input("That was not a valid choice. Please choice '1' or '2'")
    if vccReformatChoice == "1":
        vccReformat()
    elif vccReformatChoice == "2":
        vccReformat2()


def vccReformat():
    with open("vccs.txt", "r") as inputfile:
        input = inputfile.readlines()
    if not input:
        print("There was no input to be found")
        exit()
    for i in input:
        i.replace("\n", "")
        if(i.find("URL:") != -1):
            input.remove(i)
        if(i.find("Online Payment Card Details: ") != -1):
            input.remove(i)
        if(i.find("Card value: 1.00 EGP ") != -1):
            input.remove(i)
    lol = ""
    for i in input:
        if(i.find("Card number: ") != -1):
            lol = lol + i.replace("Card number: ", "").replace("\n", "")
        if(i.find("Exp Date: ") != -1):
            lol = lol + ":" + i.replace("Exp Date: ", "").replace("\n", "")
        if(i.find("CVC: ") != -1):
            lol = lol + ":" + i.replace("CVC: ", "")
    lol = lol.replace(' ', '').replace('/','')
    with open("vccsOutput.txt", "w") as f:
        f.write(lol)
        f.close
        print("Successfully reformatted VCCs and saved them to vccsOutput.txt")
        time.sleep(3)
        
def vccReformat2():
    with open ("vccs.txt", "r") as test:
        vccs = test.read()
    if len(vccs) == 0:
        print("No vccs were found in the test.txt file")
        exit()
    vccs = vccs.replace("\n\n", "temp").replace("\n", ":").replace(" ", "").replace("/", "").replace("temp", "\n")
    with open ("vccsOutput.txt", "w") as file:
        file.write(vccs)
        print("Successfully reformatted VCCs and saved them to vccsOutput.txt")
        time.sleep(3)





def tokenReformatting():
    format = input("Are your tokens using an email:password:token format? 'yes' or 'no'").lower()
    while format not in ('yes', 'no'):
        print("Invalid response. Please use 'yes' or 'no'")
        format = input("")
    if format == "no":
        exit()
    format2 = input("Which format do you want? \n1) Token \n2) Token:Pass ")
    while format2 not in ("1", "2"):
        print("Invalid choice. Please choose '1' or '2' ")
        format2 = input("")
    if format2 == "1":
        tokenReformat()
    elif format2 == "2":
        tokenReformat2()

def tokenReformat():
    tokens_file = open("tokens.txt", 'r')
    tokens = tokens_file.readlines()
    if len(tokens) == 0:
        print("No tokens were found in the tokens.txt file")
        return
    with open('tokensOutput.txt', 'w') as w:
        w.write("")
        w.close()
    for token in tokens:
        with open('tokensOutput.txt', 'a') as f:
            f.write(token.split(":")[2])
            f.close()
    print("Your tokens were successfully saved to tokensOutput.txt")
    time.sleep(3)


def tokenReformat2():
    tokens_file = open("tokens.txt", 'r')
    tokens = tokens_file.readlines()
    if len(tokens) == 0:
        print("No tokens were found in the tokens.txt file")
        return
    with open('tokensOutput.txt', 'w') as w:
        w.write("")
        w.close()
    for token in tokens:
        with open('tokensOutput.txt', 'a') as f:
            f.write(token.split(":")[2]+":"+token.split(":")[1])
            f.close()
    print("Your tokens were successfully saved to tokensOutput.txt")
    time.sleep(3)




choice = input("What would you like to reformat? \n1) Email:Password:Tokens \n2) VCCs \n3) Invite Links\n>>")
while choice not in ("1", "2", "3"):
    print("Invalid choice. Please choose '1', '2' or '3'")
    choice = input("")
import os
os.system('cls')
if choice == "1":
    tokenReformatting()
elif choice == "2":
    vccReformatting()
elif choice == "3":
    inviteReformat()
