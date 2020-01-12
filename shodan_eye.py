#!/usr/bin/env python3

# Author: Jolanda de Koff
# Bulls Eye: https://github.com/BullsEye0
# linkedin: https://www.linkedin.com/in/jolandadekoff
# Facebook: facebook.com/jolandadekoff
# Facebook Group: https://www.facebook.com/groups/ethicalhacking.hacker
# Facebook Page: https://www.facebook.com/ethical.hack.group

# Created April - August 2019 | Copyright (c)2019 Jolanda de Koff.
# Your Shodan API Key can be found here: https://account.shodan.io

# A notice to all nerds and n00bs...
# If you will copy developers work it will not make you a hacker..!
# Resepect all developers, we doing this because it's fun... :)

# Modified by: Samiux
# Infosec Ninjas: https://samiux.github.io
# Banner Spec: https://developer.shodan.io/api/banner-specification
#
# Version 1.2.0a
# Released on OCT 05, 2019 GMT+8
# [+] Modified to Python 3.7.x
# [+] Write output to file
# [+] Minor improvement
# [+] Minor Bug fixed
# [+] Add free API Key
#
# Version 1.2.0b
# Released on OCT 10, 2019 GMT+8
# [+] Minor modification

import os
import time
import random
import shodan
import sys

# Shodan Eye v1.2.0b

outfile = "result.txt"
banner1 = """

\033[1;31m

  ██████ ██░ ██ ▒█████ ▓█████▄ ▄▄▄      ███▄    █    ▓████▓██   ██▓█████
▒██    ▒▓██░ ██▒██▒  ██▒██▀ ██▒████▄    ██ ▀█   █    ▓█   ▀▒██  ██▓█   ▀
░ ▓██▄  ▒██▀▀██▒██░  ██░██   █▒██  ▀█▄ ▓██  ▀█ ██▒   ▒███   ▒██ ██▒███
  ▒   ██░▓█ ░██▒██   ██░▓█▄  █░██▄▄▄▄██▓██▒  ▐▌██▒   ▒▓█  ▄ ░ ▐██▓▒▓█  ▄
▒██████▒░▓█▒░██░ ████▓▒░▒████▓ ▓█   ▓██▒██░   ▓██░   ░▒████▒░ ██▒▓░▒████▒
▒ ▒▓▒ ▒ ░▒ ░░▒░░ ▒░▒░▒░ ▒▒▓  ▒ ▒▒   ▓▒█░ ▒░   ▒ ▒    ░░ ▒░ ░ ██▒▒▒░░ ▒░ ░
░ ░▒  ░ ░▒ ░▒░ ░ ░ ▒ ▒░ ░ ▒  ▒  ▒   ▒▒ ░ ░░   ░ ▒░    ░ ░  ▓██ ░▒░ ░ ░  ░
░  ░  ░  ░  ░░ ░ ░ ░ ▒  ░ ░  ░  ░   ▒     ░   ░ ░       ░  ▒ ▒ ░░    ░
      ░  ░  ░  ░   ░ ░    ░         ░  ░        ░       ░  ░ ░       ░  ░
                        ░                                  ░ ░  v1.2.0b

\033[1;m
            \033[1;31mShodan Eye v1.2.0b\033[0m

    The author is not responsible for any damage, misuse of the information..!
    This tool shall only be used to expand knowledge and not for
    causing malicious or damaging attacks.
    Performing any hacks without written permission is illegal.

            Author: Jolanda de Koff
            Bulls Eye | https://github.com/BullsEye0

            Modified by: Samiux
            Infosec Ninjas | https://samiux.github.io

            \033[1;31mHi there, Shall we play a game..?\033[0m 😃
        """

banner2 = """

\033[1;31m


   ▄▄▄▄▄    ▄  █ ████▄ ██▄   ██      ▄       ▄███▄ ▀▄    ▄ ▄███▄
  █     ▀▄ █   █ █   █ █  █  █ █      █      █▀   ▀  █  █  █▀   ▀
▄  ▀▀▀▀▄   ██▀▀█ █   █ █   █ █▄▄█ ██   █     ██▄▄     ▀█   ██▄▄
 ▀▄▄▄▄▀    █   █ ▀████ █  █  █  █ █ █  █     █▄   ▄▀  █    █▄   ▄▀
              █        ███▀     █ █  █ █     ▀███▀  ▄▀     ▀███▀
             ▀                 █  █   ██                       v1.2.0b

                              ▀
\033[1;m
        \033[1;31mShodan Eye v1.2.0b\033[0m

    The author is not responsible for any damage, misuse of the information..!
    This tool shall only be used to expand knowledge and not for
    causing malicious or damaging attacks.
    Performing any hacks without written permission is illegal.

        Author: Jolanda de Koff
        Bulls Eye | https://github.com/BullsEye0

        Modified by: Samiux
        Infosec Ninjas | https://samiux.github.io

        \033[1;31mHi there, Shall we play a game..?\033[0m 😃
        """

choi = (banner1, banner2)

print (random.choice(choi))
time.sleep(0.5)

def showdam():
    if os.path.exists("api.txt") and os.path.getsize("api.txt") > 0:
        with open("api.txt", "r") as file:
            shodan_api_key = file.readline().rstrip("\n")
    else:
        file = open("api.txt", "w")
        shodan_api_key = input("[!] Please enter a valid Shodan API Key: ")
        file.write(shodan_api_key)
        print ("[~] File written: api.txt")
        file.close()

    api = shodan.Shodan(shodan_api_key)
    time.sleep(0.4)

    # however, it will print 100 records maximium
    limit = 999  # Just a number
    counter = 1

    try:
        print ("[~] Checking Shodan.io API Key...")
        api.search("b00m")
        time.sleep(0.5)
        print ("[✓] API Key Authentication: SUCCESS..!")
        time.sleep(0.5)
        b00m = input("\n[+] Enter your 'filter:keyword' : ")

        result = api.search(b00m)
        # for business users (NOT TESTED!)
        #exploit = api.exploits.search(b00m)

        # wait for the search to complete
        time.sleep(5)

        # save to file
        if result["total"] > 0:
            f = open(outfile, "a")
            f.write("\nTotal record found        : {}".format(result["total"]) + "\n")
            #f.write("\nTotal Vulnerability found : {}".format(exploit["total"]) + "\n")
            f.flush()
            f.close()
        # to display
        print ("\nTotal record found        : {}".format(result["total"]))
        #print ("\nTotal vulnerability found : {}".format(exploit["total"]))

        for service in result["matches"]:
            # save to file
            f = open(outfile, "a")
            f.write("\n[✓] Result: %s. Search query: %s" % (str(counter), str(b00m)) + "\n")
            f.write("+" * 60 + "\n")
            f.write("[+] IP           : {}".format(service["ip_str"]) + "\n")
            f.write("[+] Port         : {}".format(service["port"]) + "\n")
            f.write("[+] Organization : {}".format(service["org"]) + "\n")
            f.write("[+] Location     : {}".format(service["location"]) + "\n")
            f.write("[+] Layer        : {}".format(service["transport"]) + "\n")
            f.write("[+] Domains      : {}".format(service["domains"]) + "\n")
            f.write("[+] Hostnames    : {}".format(service["hostnames"]) + "\n")
            f.write("[+] ISP          : {}".format(service["isp"]) + "\n")
            f.write("[+] OS           : {}".format(service["os"]) + "\n")
            f.write("[+] Collected on : {}".format(service["timestamp"]) + "\n")
            f.write("[+] The response of the service : \n\n" + (service["data"]))
            '''
            # for vulnerabilities (NOT TESTED!)
            for vuln in exploit["matches"]:
                f.write("[+] Bugtraq ID   : {}".format(vuln["bid"]) + "\n")
                f.write("[+] CVE          : {}".format(vuln["cve"]) + "\n")
                f.write("[+] MSB ID       : {}".format(vuln["msb"]) + "\n")
                f.write("[+] OSVDB        : {}".format(vuln["osvdb"]) + "\n")
                f.write("[+] Description  : {}".format(vuln["description"]) + "\n")
                f.write("[+] Source       : {}".format(vuln["source"]) + "\n")
                f.write("[+] Platform     : {}".format(vuln["platform"]) + "\n")
                f.write("[+] Type         : {}".format(vuln["type"]) + "\n")
                f.write("[+] Rank         : {}".format(vuln["rank"]) + "\n")
            '''
            time.sleep(0.1)
            f.flush()
            f.close()

            # display out
            print ("\n[✓] Result: %s. Search query: %s" % (str(counter), str(b00m)))
            print ("+" * 60 + "\n")
            print ("[+] \033[1;31mIP           : \033[1;m {}".format(service["ip_str"]))
            print ("[+] \033[1;31mPort         : \033[1;m {}".format(service["port"]))
            print ("[+] \033[1;31mOrganization : \033[1;m {}".format(service["org"]))
            print ("[+] \033[1;31mLocation     : \033[1;m {}".format(service["location"]))
            print ("[+] \033[1;31mLayer        : \033[1;m {}".format(service["transport"]))
            print ("[+] \033[1;31mDomains      : \033[1;m {}".format(service["domains"]))
            print ("[+] \033[1;31mHostnames    : \033[1;m {}".format(service["hostnames"]))
            print ("[+] \033[1;31mISP          : \033[1;m {}".format(service["isp"]))
            print ("[+] \033[1;31mOS           : \033[1;m {}".format(service["os"]))
            print ("[+] \033[1;31mCollected on : \033[1;m {}".format(service["timestamp"]))
            print ("[+] \033[1;31mThe response of the service: \033[1;m\n\n" + (service["data"]))
            time.sleep(0.1)
            '''
            # for vulnerabilities (NOT TESTED!)
            for vuln in exploit["matches"]:
                print ("[+] \033[1;31mBugtraq ID   : \033[1;m {}".format(vuln["bid"]))
                print ("[+] \033[1;31mCVE          : \033[1;m {}".format(vuln["cve"]))
                print ("[+] \033[1;31mMSB ID       : \033[1;m {}".format(vuln["msb"]))
                print ("[+] \033[1;31mOSVDB        : \033[1;m {}".format(vuln["osvdb"]))
                print ("[+] \033[1;31mDescription  : \033[1;m {}".format(vuln["description"]))
                print ("[+] \033[1;31mSource       : \033[1;m {}".format(vuln["source"]))
                print ("[+] \033[1;31mPlatform     : \033[1;m {}".format(vuln["platform"]))
                print ("[+] \033[1;31mType         : \033[1;m {}".format(vuln["type"]))
                print ("[+] \033[1;31mRank         : \033[1;m {}".format(vuln["rank"]))
            '''

            if counter >= limit:
                f = open(outfile, "a")
                f.write("\nTotal record printed >= {}".format(limit) + "\n")
                f.flush()
                f.close()
                print ("\nTotal record printed >= {}".format(limit) + "\n")
                exit()

            counter += 1

        # write and display total result
        if (counter - 1) > 0:
            f = open(outfile, "a")
            f.write("\nTotal record printed : {}".format(counter - 1) + "\n")
            f.flush()
            f.close()
            print ("\nTotal record printed : {}".format(counter - 1) + "\n")

    except KeyboardInterrupt:
            print ("\n")
            print ("\033[1;91m[!] User Interruption Detected..!\033[0")
            time.sleep(0.5)
            print ("\n\n\t\033[1;91m[!] I like to See Ya, Hacking\033[0m\n\n")
            time.sleep(0.5)
            sys.exit(1)

    except shodan.APIError as oeps:
            print ("[✘] Error: %s" % (oeps))
            sha_api = input("[*] Would you like to change the API Key? <Y/n>: ").lower()
            if sha_api.startswith("y" or "Y"):
                file = open("api.txt", "w")
                shodan_api_key = input("[✓] Please enter valid Shodan.io API Key: ")
                file.write(shodan_api_key)
                print ("[~] File written: api.txt")
                file.close()
                print ("[~] Restarting the Platform, Please wait... \n")
                time.sleep(1)
                showdam()
            else:
                print ("")
                print ("[•] Exiting Platform... \033[1;91m[!] I like to See Ya, Hacking\033[0m\n\n")
                sys.exit()

    print ("\n\n\tShodan Eye \033[1;91mI like to See Ya, Hacking \033[0m\n\n")


# =====# Main #===== #
if __name__ == "__main__":
    showdam()

