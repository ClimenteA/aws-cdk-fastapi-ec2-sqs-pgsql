# LogsApi

This is a extra small rest api made in Python FastAPI with PostgreSQL as a database. 
SQLAlchemy async ORM is used to intereact with the database. 
The entire app runs on a AWS EC2 instance and exposes a POST request which saves a log message to PostgreSQL. PGAdmin is also available to see the data saved and perform custom queries.

In `cdk.py` - Amazon Cloud Deployment Kit (AWS CDK) is used to create the AWS EC2 stack on which this dockerized rest api will run.

In case something goes wrong `logs.log` contains all the errors needed for debugging (enter in api container with `sudo docker-compose exec app bash` there check the logs.log with `cat logs.log`). 

You can SSH in the EC2 instance from the aws console (search EC2 > Instances > Select Instance > Connect > Click `Connect` button on first Tab `EC2 Instance Connect`). 

If you need to do some live debugging SSH into the EC2 and do a `sudo docker-compose logs -ft app` for the restapi or `-ft pgsql` for Postgres. 

Basic, but does the job.


*If you are new to AWS go thru these resources:*
- [Getting started tutorial for AWS](https://www.youtube.com/watch?v=CjKhQoYeR4Q); 
- [Install aws cli](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html);
- [Cloud Development Kit Docs](https://docs.aws.amazon.com/cdk/v2/guide/work-with-cdk-python.html);
- [Getting started tutorial for AWS CDK](https://www.youtube.com/watch?v=nlb8yo7SZ2I&list=PL9nWRykSBSFhYIHZfX4xA1oAstNW5QleC);
- [ec2 aws cdk tutorial](https://community.aws/content/2duq9xSYespeSBQ5R1WiuOcCvMj/using-ec2-userdata-to-bootstrap-python-web-app)


With aws cli and cdk cli available in your terminal do:
- `cdk bootstrap` - if you are running this on a new account and didn't ran this before;
- `cdk deploy` - this will deploy this application (Note: Here we are using a public github url - for private repos you need to change `cdk.py` to handle that);
- `cdk destroy` - the stack will be destroyed; 


After deploy save the output somewhere safe and switch IP here:
- http://3.76.216.129:3000/docs - the rest api swagger;
- http://3.76.216.129:15432     - the pgadmin UI; 


TODO:
- PostgreSQL on a separate EC2;
- Use AWS SQS instead of Starlette's Background task;
- Prometheus/Grafana [observability](https://github.com/Blueswen/fastapi-observability)
- Tests;
