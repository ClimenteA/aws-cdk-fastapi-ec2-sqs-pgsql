import aws_cdk as cdk
import aws_cdk.aws_ec2 as ec2
import aws_cdk.aws_iam as iam
from constructs import Construct


class EC2DeployStack(cdk.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        webServerRole = iam.Role(
            self, "ec2Role", assumed_by=iam.ServicePrincipal("ec2.amazonaws.com")
        )

        # IAM policy attachment to allow access to
        webServerRole.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name(
                "AmazonSSMManagedInstanceCore"
            )
        )

        # webServerRole.add_managed_policy(
        #     iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AmazonEC2RoleforAWSCodeDeploy")
        # )

        # This VPC has 3 public subnets, and that's it
        vpc = ec2.Vpc(
            self,
            "main_vpc",
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    cidr_mask=24, name="pub01", subnet_type=ec2.SubnetType.PUBLIC
                ),
                ec2.SubnetConfiguration(
                    cidr_mask=24, name="pub02", subnet_type=ec2.SubnetType.PUBLIC
                ),
                ec2.SubnetConfiguration(
                    cidr_mask=24, name="pub03", subnet_type=ec2.SubnetType.PUBLIC
                ),
            ],
        )

        # Security Groups
        # This SG will only allow HTTP traffic to the Web server
        webSg = ec2.SecurityGroup(
            self,
            "web_sg",
            vpc=vpc,
            description="Allows Inbound HTTP traffic to the web server.",
            allow_all_outbound=True,
        )
        webSg.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.tcp(80))

        # the AMI to be used for the EC2 Instance
        ami = ec2.AmazonLinuxImage(
            generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2023,
            cpu_type=ec2.AmazonLinuxCpuType.X86_64,
        )

        # The actual Web EC2 Instance for the web server
        webServer = ec2.Instance(
            self,
            "web_server",
            vpc=vpc,
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.T2, ec2.InstanceSize.MICRO
            ),
            machine_image=ami,
            security_group=webSg,
            role=webServerRole,
        )

        # User data - used for bootstrapping
        with open("cdk_ec2_start.sh", "r") as sh:
            webSGUserData = sh.read()

        webServer.add_user_data(webSGUserData)

        # Tag the instance
        cdk.Tags.of(webServer).add("application-name", "python-web")
        cdk.Tags.of(webServer).add("stage", "prod")

        # Output the public IP address of the EC2 instance
        cdk.CfnOutput(self, "IP Address", value=webServer.instance_public_ip)




if __name__ == "__main__":
    from config import cfg

    app = cdk.App()

    EC2DeployStack(
        app,
        "EC2SimpleStack",
        env=cdk.Environment(account=cfg.CDK_ACCOUNT, region=cfg.CDK_REGION),
    )

    app.synth()
