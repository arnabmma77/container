🚀 Running a Streamlit App in Docker on AWS EC2
📜 Table of Contents
🛠 Setting Up a VPC, Subnet, Route Table, and Internet Gateway
🖥️ Launching and Configuring an EC2 Instance
🔗 Connecting to EC2 Instance via EC2 Instance Connect
🔑 Setting Permissions for the PEM Key
🐳 Installing and Configuring Docker on EC2
📂 Copying Project Files to EC2
🏗️ Building and Running the Docker Container
🌐 Accessing the Streamlit App
🔄 Managing the Docker Container
1️⃣ Setting Up a VPC, Subnet, Route Table, and Internet Gateway
To ensure a well-structured networking setup, follow these steps in the AWS Management Console.

1.1 Create a New VPC
Navigate to AWS Console → VPC Dashboard.
Click Create VPC.
Enter:
Name: MyCustomVPC
IPv4 CIDR block: 10.0.0.0/16
Click Create VPC.
1.2 Create a Subnet
Go to VPC Dashboard → Subnets → Create Subnet.
Select MyCustomVPC.
Enter:
Subnet name: MyPublicSubnet
CIDR block: 10.0.1.0/24
Availability Zone: Select any zone.
Click Create Subnet.
1.3 Enable Auto-Assign Public IPv4
Go to Subnets.
Select MyPublicSubnet.
Click Actions → Edit Subnet Settings.
Enable Auto-assign public IPv4 address.
Click Save changes.
1.4 Create an Internet Gateway
Go to VPC Dashboard → Internet Gateways.
Click Create Internet Gateway.
Name it MyIGW and click Create.
Attach it to MyCustomVPC:
Select MyIGW.
Click Actions → Attach to VPC → Select MyCustomVPC.
Click Attach.
1.5 Create a Route Table
Go to VPC Dashboard → Route Tables.
Click Create Route Table.
Name it MyPublicRouteTable, select MyCustomVPC, and click Create.
Select MyPublicRouteTable, go to the Routes tab.
Click Edit routes → Add route:
Destination: 0.0.0.0/0
Target: Select MyIGW.
Click Save changes.
1.6 Associate the Subnet with the Route Table
Go to Route Tables.
Select MyPublicRouteTable.
Click Subnet Associations → Edit Subnet Associations.
Select MyPublicSubnet and click Save.
2️⃣ Launching and Configuring an EC2 Instance
2.1 Create an EC2 Instance
Go to EC2 Dashboard → Instances → Launch Instance.
Configure:
Name: Streamlit-EC2
AMI: Select Amazon Linux 2023
Instance Type: t2.micro (Free Tier)
Key Pair: Create or use an existing key pair.
Network Settings:
VPC: Select MyCustomVPC.
Subnet: Select MyPublicSubnet.
Auto-assign public IP: Enabled.
Security Group:
Allow SSH (port 22).
Allow HTTP (port 80, optional).
Allow Streamlit (port 8501).
Click Launch Instance.
3️⃣ Connecting to EC2 Using EC2 Instance Connect
Go to EC2 Dashboard → Instances.
Select Streamlit-EC2.
Click Connect.
Choose EC2 Instance Connect.
Click Connect (Opens a browser-based terminal).
4️⃣ Setting Permissions for the PEM Key
Move your .pem key to your work directory:

mv /path/to/your-key.pem ~/your-work-directory/
Or copy-paste it into your work directory.

Set the correct permissions:

chmod 600 your-key.pem
Streamlit on AWS EC2

5️⃣ Installing and Configuring Docker on EC2
Update packages:

sudo yum update -y
Install Docker:

sudo yum install -y docker
Streamlit on AWS EC2 - Step 2

Enable and start Docker:

sudo systemctl enable docker
sudo systemctl start docker
Streamlit on AWS EC2 - Step 3

6️⃣ Copying Project Files to EC2
Transfer files using SCP:

scp -i your-key.pem app.py Dockerfile requirements.txt mushroom.cv ec2-user@your-ec2-public-ip:/home/ec2-user/
Streamlit on AWS EC2 - Step 4

7️⃣ Building and Running the Docker Container
Navigate to the directory:

cd /home/ec2-user/
Build the Docker image:

sudo docker build -t streamlit-app .
Run the container:

sudo docker run -d -p 8501:8501 --name streamlit_container streamlit-app
Streamlit on AWS EC2 - Step 5

8️⃣ Accessing the Streamlit App
Open your browser and go to:

http://your-ec2-public-ip:8501
The Streamlit app should now be accessible.

Streamlit on AWS EC2 - Step 6

9️⃣ Managing the Docker Container
Check running containers:

sudo docker ps
Stop the container:

sudo docker stop streamlit_container
Remove the container:

sudo docker rm streamlit_container
Restart the container:

sudo docker start streamlit_container
🎯 Conclusion
This documentation provides a step-by-step guide to:

✅ Set up a custom VPC, subnet, and Internet Gateway

✅ Launch an EC2 instance and enable IPv4 assignment

✅ Install Docker and deploy the Streamlit app in a Docker container

✅ Access the app via a public IP

This setup ensures scalability, security, and reliability for your project. 🚀
