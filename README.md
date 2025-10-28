Exp2
$ git
$ sudo apt update
password for ubuntu
$ sudo apt install git
If error copy the above command $ apt --fix broken install
$ git --version
$ git config --global user.name “Vidisha3005”
$ git config --global user.email “mayekarvidisha@gmail.com”
$ git config --list
$ pwd
$ mkdir workspace
$ cd workspace/
$ git clone add_repository_https_link
$ ls
$ cd hello_test/
 $ ls    (output README.md)
$ touch hello.txt
$ ls             (readme.md hello.txt)
$   gedit hello.txt
$ git status
$ git add hello.txt


$ git status
$ git commit -m “Initial commit”
$ git status
$ git push origin main
Give github username and password
Go to profile then click on settings then developer settings 
Then personal acess tokens
Then classic tokens
Generate new tokens 
Generate new token classic
Select all scopes
Generate token
Copy token
$ git remote set-url origin https://token>@github.com/<username>/<repo>
$ git push origin main


**docker**
sudo apt-get update
sudo apt install docker
sudo apt install docker.io
sudo systemctl enable docker
sudo systemctl status docker
sudo systemctl start docker
sudo docker run hello-world



sudo systemctl stop systemd-resolved
sudo systemctl disable systemd-resolved

sudo nano /etc/resolv.conf

Add Google DNS (8.8.8.8) or Cloudflare DNS(1.1.1.1) at the top:


nameserver 8.8.8.8
nameserver 8.8.4.4

Ctrl O   enter ctrl X

sudo systemctl restart docker
sudo docker run hello-world

groups $USER
sudo usermod -aG docker $USER
sudo systemctl restart docker
docker login

ls -l /var/run/docker.sock
sudo chmod 660 /var/run/docker.sock
docker --version
docker login



newgrp docker
docker login

docker search apache
docker search redis
docker run docker/whalesay cowsay Hello everyone 
docker ps
docker pull nginx

**slave master**
user@user-H81M-S:~$ sudo mkdir -p /var/jenkins
[sudo] password for user:
user@user-H81M-S:~$ sudo chown user:user /var/jenkins
user@user-H81M-S:~$ ls -ld /var/jenkins
drwxr-xr-x 2 user user 4096 Sep 17 12:20 /var/jenkins
user@user-H81M-S:~$ ssh user@agent-ip
ssh: Could not resolve hostname agent-ip: Temporary failure in name resolution
user@user-H81M-S:~$ curl -sO http://localhost:8080/jnlpJars/agent.jar
user@user-H81M-S:~$ java -version
openjdk version "17.0.15" 2025-04-15
OpenJDK Runtime Environment (build 17.0.15+6-Ubuntu-0ubuntu120.04)
OpenJDK 64-Bit Server VM (build 17.0.15+6-Ubuntu-0ubuntu120.04, mixed mode, sharing)
user@user-H81M-S:~$ java -jar agent.jar -url http://localhost:8080/ -secret 64041d799f1dd88a84bbc1be521322fc9019f8a89e24459fa7a6fb9c5d9987a6 -name "slave-1" -workDir "/var/jenkins"
Sep 17, 2025 12:29:25 PM org.jenkinsci.remoting.engine.WorkDirManager initializeWorkDir
INFO: Using /var/jenkins/remoting as a remoting work directory
Sep 17, 2025 12:29:25 PM org.jenkinsci.remoting.engine.WorkDirManager setupLogging
INFO: Both error and output logs will be printed to /var/jenkins/remoting
Sep 17, 2025 12:29:25 PM hudson.remoting.Launcher createEngine
INFO: Setting up agent: slave-1
Sep 17, 2025 12:29:25 PM hudson.remoting.Engine startEngine
INFO: Using Remoting version: 3301.v4363ddcca_4e7
Sep 17, 2025 12:29:25 PM org.jenkinsci.remoting.engine.WorkDirManager initializeWorkDir
INFO: Using /var/jenkins/remoting as a remoting work directory
Sep 17, 2025 12:29:25 PM hudson.remoting.Launcher$CuiListener status
INFO: Locating server among [http://localhost:8080/]
Sep 17, 2025 12:29:25 PM org.jenkinsci.remoting.engine.JnlpAgentEndpointResolver resolve
INFO: Remoting server accepts the following protocols: [JNLP4-connect, Ping]
Sep 17, 2025 12:29:25 PM hudson.remoting.Launcher$CuiListener status
INFO: Agent discovery successful
  Agent address: localhost
  Agent port:    50000
  Identity:      c1:3f:85:6f:72:69:d5:68:f4:72:35:24:9b:e6:02:a9
Sep 17, 2025 12:29:25 PM hudson.remoting.Launcher$CuiListener status
INFO: Handshaking
Sep 17, 2025 12:29:25 PM hudson.remoting.Launcher$CuiListener status
INFO: Connecting to localhost:50000
Sep 17, 2025 12:29:25 PM hudson.remoting.Launcher$CuiListener status
INFO: Server reports protocol JNLP4-connect-proxy not supported, skipping
Sep 17, 2025 12:29:25 PM hudson.remoting.Launcher$CuiListener status
INFO: Trying protocol: JNLP4-connect
Sep 17, 2025 12:29:25 PM org.jenkinsci.remoting.protocol.impl.BIONetworkLayer$Reader run
INFO: Waiting for ProtocolStack to start.
Sep 17, 2025 12:29:26 PM hudson.remoting.Launcher$CuiListener status
INFO: Remote identity confirmed: c1:3f:85:6f:72:69:d5:68:f4:72:35:24:9b:e6:02:a9
Sep 17, 2025 12:29:26 PM hudson.remoting.Launcher$CuiListener status
INFO: Connected
