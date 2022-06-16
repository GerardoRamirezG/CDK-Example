from aws_cdk import (
aws_ec2 as ec2,
core,
)

from constructs import Construct

class VPCStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs):

        super().__init__(scope, id, **kwargs)

        vpc = ec2.Vpc(
            self,
            "VPC",
            nat_gateways=0,
            subnet_configuration=[
                ec2.SubnetConfiguration(name="public", subnet_type=ec2.SubnetType.PUBLIC)
            ],
        )

        http =ec2.SecurityGroup(self, 'http', vpc=vpc, security_group_name='htt_sg')
        https = ec2.SecurityGroup(self, 'https', vpc=vpc, security_group_name='htts_sg')
        ssh = ec2.SecurityGroup(self, 'ssh', vpc=vpc, security_group_name='ssh_sg')
    
        http.add_ingress_rule(
        ec2.Peer.any_ipv4(), #0.0.0.0/0
        connection=ec2.Port.tcp(80),
        description="allow traffic from anywhere thru the port 80"
       )
    
        https.add_ingress_rule(
        ec2.Peer.any_ipv4(), #0.0.0.0/0
        connection=ec2.Port.tcp(443),
        description="allow traffic from anywhere thru the port 80"
       )
    
        ssh.add_ingress_rule(
        ec2.Peer.any_ipv4(), #0.0.0.0/0
        connection=ec2.Port.tcp(22),
        description="allow traffic from anywhere thru the port 80"
       )
       
      