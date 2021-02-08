# Easy Duo Authentication

A Chrome extension that allows users to authenticate with the Duo Prompt on a computer in one click. Developed during UCLA HOTH 8 Hackathon. 

## Overview

[The Duo Authentication](https://guide.duo.com/prompt) uses a one-time password algorithm called [HOTP (HMAC-based One-time Password)](https://tools.ietf.org/html/rfc4226) to generate passcodes. For HOTP, the authenticator and the authenticated share a secret key K (an arbitrary byte string) and a counter C. Each one-time passcode is calculated as such:

```
HOTP(K, C) = truncate(HMACH(K, C))
C += 1
```

Once the authenticated inputs a passcode, the authenticator will verify the passcode by calculating HOTP(K, C) for C in a reasonable interval [C, C+n]. If a match is found, then the authentication succeeds. Therefore, if we manage to get the secret key from Duo, we can calculate the exact same passcodes as Duo would. 

## Set Up
1. Download the codes as ZIP or clone this repository.
2. In Google Chrome, navigate to ```chrome://extensions```, enable ```Developer Mode```, click ```Load Unpacked```, and select the downloaded/cloned folder. Pin the extension for later convenience. 
3. Open a Duo authentication page, click ```Add a new device```. Choose ```Tablet```, choose either ```iOS``` or ```Android```, and click ```Continue```. Then, click ```I have Duo Mobile installed```, and click ```Email me a one-time activation link instead```. Enter your email and get an activation link (in the form ```https://m-*.duosecurity.com/*```). 
4. Open terminal, run the following and get a HOTP Secret. 
 ```bash
 pip install requests
 ```
 ```bash
 python3 generateHOTPSecret.py https://m-(your activation link)
 ```
5. In Chrome, click the extension and input the HOTP Secret. 
6. Back to the ```Activate Duo Mobile by Email``` page, click ```Continue```, and you may change the device name to something like ```Easy Duo Authentication```. Also, set it to the ```Default Device``` for convenience. 
  

## Notes
1. Due to the CORS (Cross-Origin Resource Sharing) HTTP-header mechanism, I cannot fetch data directly from Duo using JavaScript, resulting in the extra step using Python. I also cannot get DOM elements inside <iframe> and thus cannot make advanced features like auto-login.  
2. This project was developed in one day so it does not contain many codes that check for error/bad inputs. If you feel that something is wrong or the extension does not work properly, you could remove it from Chrome and do the Set Up again. 
