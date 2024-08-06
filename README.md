# FACEMASH - FACEBOOK BRUTE FORCE PREMIUM

![Facemash](https://github.com/user-attachments/assets/bb09eb6b-b863-4ef5-843a-5986984e7e8c)

[**Facemash**](https://github.com/RozhakXD/Facemash) is an advanced and educational tool crafted to illustrate the vulnerabilities of Facebook accounts with weak passwords. Originally released on January 1, 2023, Facemash is designed to showcase the techniques used in ethical hacking for educational purposes only. This latest and final version integrates various powerful features, providing users with a comprehensive understanding of account security.

## Features

Facemash is an advanced educational tool designed to illustrate the vulnerabilities of Facebook accounts with weak passwords. With a robust set of features, it allows users to simulate various ethical hacking scenarios. Whether you're searching for accounts by name, accessing friend lists, or targeting followers, Facemash provides the tools you need. The script also supports cracking accounts from group members and post comments, verifying checkpoint options, and converting usernames to Facebook IDs.

<details>
  <summary>Show Image Features</summary>
  <img src="https://github.com/user-attachments/assets/a0b9b0eb-c92b-4d3c-9817-85be6166c014" alt="Facemash Features">
</details>

In addition to these core features, Facemash offers functionalities for viewing all cracking results, targeting group admins, and cracking accounts using random email addresses. Users can even search for Dana Kaget links associated with accounts. Each feature is crafted to provide a comprehensive understanding of account security, making Facemash a powerful resource for ethical hacking education.

<details>
  <summary>Show Login Image</summary>
  <img src="https://github.com/user-attachments/assets/290c47be-d6ac-4683-ba2d-752e5db3e8eb" alt="Facemash Login">
</details>

The program includes certain password methods and options to enhance its functionality. Users can choose from several password approaches: full password, default password, manual password, and combined password. Furthermore, Facemash offers various methods for solving the problem, including asynchronous and regular methods via various Facebook URLs, and Ad Manager or developer methods.

## Installation

* [Linux](https://drive.google.com/file/d/1IbP1CHRwOzUKHyq0AZz9MbuzjQKhGdtL/view?usp=drivesdk) - [Termux](https://f-droid.org/repo/com.termux_118.apk)

  ```
  >> pkg update -y && pkg upgrade -y
  >> pkg install python-pip clang binutils git libffi openssl libsodium iproute2 build-essential
  >> SODIUM_INSTALL=system pip install pynacl
  >> apt install python-cryptography
  >> git clone --depth 1 https://github.com/RozhakXD/Facemash.git
  >> cd "Facemash"
  >> python -m pip install -r requirements.txt
  >> chmod +x Run
  >> ./Run
  ```
  - Running on Termux

    ```
    >> cd "$HOME/Facemash"
    >> ./Run
    ```

## Problems and Solutions

This section provides an overview of common problems you may encounter while using the program and how to address them. We will discuss typical issues such as receiving only checkpoints, encountering no results, or facing dump failures. By understanding these common issues and referring to the detailed solutions provided below, you can better diagnose and resolve any problems to ensure effective use of the program.

### **1. Targeting Requirements and Guidelines?**

- **Likes or Comments**: The targeted post must have at least 1000 likes or 500 comments. Avoid posts from cover photos or profile photos.
- **Friends**: The target account should have more than 300 friends and the profile must be visible to the public. Avoid professional or business accounts.
- **Group**: The target group should have active members and must not be set to private.
- **Followers**: The target account should have more than 500 followers and should not be a professional or business account.

### **2. Achieving Successful Results?**

- **Choose a Target Account**: Look for a target with a newly created account and ensure that the account is either weak or has a poor password.
- **Use Effective Methods**: Utilize recommended methods such as `WEB`, `ADS MANAGER`, and `MOBILE` for better results.
- **Select Reliable Providers**: Opt for reliable service providers like `INDOSAT` and `AXIS` for more effective targeting.
- **Consider Geographic Proximity**: It’s advisable to target accounts within the same geographical area as you to increase your chances of success.
- **Use a Strong User-Agent**: Employ user-agent strings from reputable brands like `REALME`, `OPPO`, `SAMSUNG`, `ONEPLUS`, `POCO`, `XIAOMI`, `HUAWEI`, and `VIVO` to improve your success rate.
- **Note**: We have also observed that successful results are often achieved with accounts that have been recently created. Targeting newer accounts may increase your likelihood of success.

### **3. Troubleshooting No Results?**

- **Strong Passwords**: The target account may have a strong password that is difficult to crack.
- **Incorrect Password List**: You might have entered the password list incorrectly. It's recommended to use the automatic password option.
- **Airplane Mode Not Used**: Ensure you activate **"Airplane Mode"** every 200 usernames to avoid detection.
- **Blocked IP Address**: Your IP address might be blocked or flagged for suspicious activity.
- **Facebook System Issues**: There could be temporary issues with the Facebook system that prevent successful cracking.
- **Problematic Target**: If there are no results at all, the issue might be with the target account itself.

### **4. Why My Account Is Checkpointed?**

- **Open Checkpointed Accounts**: If your account is hit by a checkpoint, open it to ensure it remains active and lasts longer.
- **Use Fake or New Accounts**: It's recommended to use a fake account or a newly created account for these activities.
- **Secure Your Account**: Ensure your Facebook account has a phone number, email, and two-factor authentication enabled.
- **Retrieve Cookies**: Keep the Facebook account online in the browser to retrieve cookies effectively.
- **Refresh Regularly**: Open [**`Facebook Web`**](https://web.facebook.com) in desktop mode during the Dump process and refresh the page every few minutes.

### **5. Understanding Dump Failures?**

- **Account Blocked or Spammed**: Your Facebook account might be blocked from dumping for 24 hours or flagged for spamming.
- **Account Checkpointed or Locked**: Your Facebook account could be checkpointed or temporarily locked.
- **Incorrect Target**: The target you entered might be incorrect. Ensure the target meets all necessary requirements.

### **6. Only Getting Checkpoints?**

- **Poor Target Selection**: The target you selected may not be suitable, or you might be experiencing bad luck with the target.
- **Previously Used Target**: The target account may have already been compromised by someone else.
- **Unsuitable Provider**: Your internet provider may not be suitable for this script.
- **Incorrect Method or User-Agent**: The method or user-agent you selected might be inappropriate for the task.
- **Facebook System Changes**: The Facebook system may have become more challenging, making it harder to get successful results.

### **6. Trouble Logging In?**

-  **Use Cookies to Log In**: If you still can't log in, try using cookies from the cracked account. This involves copying the cookies from the web session where the account was accessed and using them to authenticate the login.
- **IP Address is Blocked**: Your IP address might be blocked, causing login issues. Consider using a VPN or switching networks.
- **Try Logging in with a Facebook App Cloner**: If you're having trouble logging in, try using a Facebook app cloner.

### **7. Common Cracking Errors?**

- **`LSD TOKEN NOT FOUND`**: This occurs because the user agent has disabled JavaScript. Don’t worry, this does not interfere with the hacking process.
- **`PUBLIC KEY NOT FOUND`**: This happens because you are using a password encryption system that cannot find the public key. However, this will not affect the results obtained.
- **`CONNECTION ERROR`**: This is definitely a problem with your internet connection. Make sure your connection is stable and strong.
- **`TOO MANY REDIRECTS`**: This error indicates an issue with the network or user agent causing continuous login redirects, suggesting that your device is not compatible with the method being used.

Every user should read this section, even if you are not currently experiencing a problem. Understanding these problems and solutions will prepare you for potential future problems and help you use the Program effectively.

## Screenshot

![Results/Ok-24-July-2023.txt](https://github.com/RozhakXD/Facemash/blob/main/Data/Ok-24-July-2023.png)

## Disclaimer

Please ensure you are aware of and comply with the laws in your country. As the developer, I am not responsible for any consequences that may arise from using this Program. Any misuse or legal issues are the sole responsibility of the user.

##

```python
print("Happy Hacking Day!")
```
##
