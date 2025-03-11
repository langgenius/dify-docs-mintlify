# Deploy with aaPanel

## Prerequisites

> Before installing Dify, make sure your machine meets the following minimum system requirements:
>
> * CPU >= 2 Core
> * RAM >= 4 GiB

| Operating System           | Software                       | Explanation                                                                                                                                              |
| -------------------------- | ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Linux platforms            | <p>aaPanel 7.0.11 or later</p> | Please refer to the [aaPanel installation guide](https://www.aapanel.com/new/download.html#install) for more information on how to install aaPanel.      |

## Deployment

1. Log in to aaPanel and click `Docker` in the menu bar

2. The first time you will be prompted to install the `Docker` and `Docker Compose` services, click Install Now. If it is already installed, please ignore it.
  
3. After the installation is complete, find `Dify` in `One-Click Install` and click `install`  

4. configure basic information such as the domain name, ports to complete the installation
> \[!IMPORTANT]
>
> The domain name is optional, if the domain name is filled, it can be managed through [Website]--> [Proxy Project], and you do not need to check [Allow external access] after filling in the domain name, otherwise you need to check it before you can access it through the port

5. After installation, enter the domain name or IP+ port set in the previous step in the browser to access.
- Name: application name, default `Dify-characters`
- Version selection: default `latest`
- Domain name: If you need to access directly through the domain name, please configure the domain name here and resolve the domain name to the server
- Allow external access: If you need direct access through `IP+Port`, please check. If you have set up a domain name, please do not check here.
- Port: Default `8088`, can be modified by yourself


6. After submission, the panel will automatically initialize the application, which will take about `1-3` minutes. It can be accessed after the initialization is completed.

### Access Dify

Access administrator initialization page to set up the admin account:

```bash
# If you have set domain
http://yourdomain/install

# If you choose to access through `IP+Port`
http://your_server_ip:8088/install
```

Dify web interface address:

```bash
# If you have set domain
http://yourdomain/

# If you choose to access through `IP+Port`
http://your_server_ip:8088/
```
