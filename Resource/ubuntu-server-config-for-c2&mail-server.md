

# Ubuntu Server Configuration for C2 and Mail Server

This guide provides instructions to set up an Ubuntu server as a Command and Control (C2) and mail server.

## 1. Server Setup

1. **Update and Upgrade the Server**
    ```bash
    sudo apt-get update && sudo apt-get upgrade -y
    ```
    Install Docker

    ```bash
    sudo apt-get install -y docker.io
    ```
2. Mail Server Setup

We are using Docker to set up an internal mail server.

> Pull and Run Mailhog Container

   ```bash
    sudo docker pull mailhog/mailhog
    sudo docker run -d -p 8025:8025 -p 1025:1025 mailhog/mailhog
   ```
3. Apache2 for Payload Download

    Install Apache2

    ```bash
    sudo apt-get install apache2 -y
    ```
Start Apache2 Service

```bash
sudo systemctl start apache2
```
Move the Payload Move the payload to /var/www/html, so the user can click and download the payload from the email.

```bash
sudo mv /path/to/payload /var/www/html/
```
### Conclusion

> With this setup, you have a basic C2 and mail server configuration on your Ubuntu server. The Mailhog server handles internal mail, while Apache2 serves payloads for download.