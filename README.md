# Easy Duo Authentication

A Chrome extension that allows users to authenticate with the Duo Prompt on a computer in one click. Developed during UCLA HOTH 8 Hackathon. 

## Overview

[The Duo Authentication](https://guide.duo.com/prompt) uses a one-time password algorithm called [HOTP (HMAC-based One-time Password)](https://tools.ietf.org/html/rfc4226) to generate passcodes. For HOTP, the authenticator and the authenticated share a secret key K (an arbitrary byte string) and a counter C. Each one-time passcode is calculated as such:

```
HOTP(K, C) = truncate(HMACH(K, C))
C += 1
```

Once the authenticated inputs the passcode, the authenticator will verify the passcode by calculating HOTP(K, C) for C in a reasonable interval [C, C+n]. If a match is found, then the authentication succeeds. Therefore, if we manage to get the secret key from Duo, we can calculate the exact same passcodes as Duo would. 

## Set Up
### 1. 
