WEB SERVER PROJECT; done during Full Stack Software Engineering at ALX.

Files							Description
0-transfer_file						transfers a file from our client to a server
							accepts 4 parameters: 
								The path to the file to be transferred
								The IP of the server we want to transfer the file to
								The username scp connects with
								The path to the SSH private key that scp uses
1-install_nginx_web_server				configures an Ubuntu machine to install NGINX web server
							Requirements:

								Install nginx on your web-01 server
								Nginx should be listening on port 80
								When querying Nginx at its root / with a GET request (requesting a page) using curl, 
									it must return a page that contains the string Hello World!
								As an answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements 
									(this script will be run on the server itself)
								You can't use systemctl for restarting nginx
2-setup_a_domain_name					
