0x09. Web infrastructure design

Task 0. Simple web stack
	Solution;
		This is my simple one server web infrastructure that hosts the website that is reachable via www.foobar.com. 
A server is a structure that can be a computer hardware or software, that provides functionality to other programs or devices. The role of a server is to share data as well as to share resources and distribute work.  
The domain name serves as the unique address of a website on the internet. It is used to identify and locate websites, making it easier for users to access specific web pages. 
The "www" in a domain like "www.foobar.com" is usually a subdomain indicating the web server hosting the site. In DNS records, the "www" subdomain is often shown by a CNAME (Canonical Name) record. This CNAME record directs to the domain of the web server hosting the site, enabling users to reach the site by entering "www" before the domain. 
The primary function of the web server is to deliver web pages, images, and other content to users who access the website.  The application server is responsible for executing the business logic of a web application. The database is a storage system that stores and manages the data used by the web application. 
The server uses a protocol called HTTP (Hypertext Transfer Protocol) to communicate with the computer of the user requesting the website.
ISSUES
1.	Single Point of Failure (SPOF): The entire web infrastructure relies on a single server. If that server fails, experiences hardware issues, or faces any other problems, the entire website becomes inaccessible. Impact could include downtime, loss of user access, and potential data loss.
2.	Downtime During Maintenance: When maintenance tasks, such as deploying new code, are performed, the web server may need to be restarted. This results in downtime during which the website is unavailable to users. Impact includes user inconvenience, potential loss of business, and negative impact on user experience.
3.	Cannot Scale with Incoming Traffic: The infrastructure may struggle to handle a large volume of incoming traffic efficiently due to its single-server nature. Impacts include performance degradation, slow response times, and potential denial of service under high-traffic conditions.

