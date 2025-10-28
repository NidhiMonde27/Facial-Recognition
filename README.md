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
