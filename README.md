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
- `cdk deploy` - this will deploy this application. Note: Here we are using a public github url - for private repos you need to change `cdk.py` to handle that. After `cdk deploy` finishes you'll get connection details to the API and Database - save them somewhere safe;
- `cdk destroy` - the stack will be destroyed; 


After deploy save the output somewhere safe and switch IP here:
- http://3.71.80.85:3000/docs - the rest api swagger;
- http://3.71.80.85:15432     - the pgadmin UI; 


Optimizations:
- PostgreSQL on a separate EC2;
- Use AWS SQS instead of Starlette's Background task;
- Prometheus/Grafana [observability](https://github.com/Blueswen/fastapi-observability);
- Tests;


## Load testing

Considering that on AWS t2.micro instance was used with 1 CPU and 1 GB of RAM and the entire app ran on that small EC2 results are pretty good. 

Load tested with 1000 users at peak concurency - 1k users at the same time on an app is not common.
The t2.micro machine got 22 failed requests out of 13577 post requests made (0.16% failure rate) which is pretty good.  
Average response time was 324ms (we must take into consideration some latency - server in Frankfurt me in Iasi, Romania).
The response time will be bigger from someone on another continent (lots of cable for that post request to travel), but with another EC2 instance close to the user will make it better. 


Checkout locust.py and load_testing_reports.

Locust ui config:
![locust ui config](/load_testing_reports/locust-ui-config.png)


## Results on localhost I7, 16GB RAM:
![localhost](/load_testing_reports/localhost-results.png)

## Results on AWS t2.micro:
![t2micro](/load_testing_reports/results-t2-micro.png)

## Resources for T2 MICRO are 1CPU 1GB RAM
![t2microlist](/load_testing_reports/t2-list.png)
