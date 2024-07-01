# LogsApi

Basic restapi example for spinning up an aws restapi in AWS Cloud Development Kit (infrastructure as code).

Here is dockerized code deployed on a EC2 machine from the aws UI (with Launch Instance button).


- [Youtube tutorial](https://www.youtube.com/watch?v=Mz10Qliu1eo) on how to create an EC2 instance and get the .pem file to connect to the virtual machine;
- After the EC2 instance is created, enter in the EC2 machine with `ssh -i "ec2ui.pem" ubuntu@ec2-18-153-74-127.eu-central-1.compute.amazonaws.com`;
- Install docker with snap;
- Clone the github repo in the EC2 (if it was a private repo create some ssh keys for the EC2 on github - same as we do on a new laptop/fresh OS install);
- Change the .env file with secure passwords and Caddyfile to point to the required domains (api and pgadmin) - in this case I used ROMARG DNS because I have some domains from them;
- Exposed domains:
- https://servicebell.api.softgata.com/docs
- https://servicebell.admin.softgata.com/browser/



<!-- 

- [fastapi-observability](https://github.com/Blueswen/fastapi-observability)
- [ec2 aws cdk tutorial](https://community.aws/content/2duq9xSYespeSBQ5R1WiuOcCvMj/using-ec2-userdata-to-bootstrap-python-web-app)


- `alembic init migrations`;
- `alembic revision --autogenerate -m "Initial migration"`;
- `alembic upgrade head` - run before starting the app; 

-->


