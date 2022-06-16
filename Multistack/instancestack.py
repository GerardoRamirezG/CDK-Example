from aws_cdk import (
aws_ec2 as ec2,
core, App
)

from constructs import Construct

class Ec2Stack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, referenced_function: ec2.main_function , **kwargs):

        super().__init__(scope, id, **kwargs)
        
        amzn_linux = ec2.MachineImage.latest_amazon_linux(
        generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
        edition=ec2.AmazonLinuxEdition.STANDARD,
        virtualization=ec2.AmazonLinuxVirt.HVM,
        storage=ec2.AmazonLinuxStorage.GENERAL_PURPOSE,
    )
        prod = ec2.Instance(
        self,
        "instance",
        instance_type=ec2.InstanceType("t2.micro"),
        machine_image=amzn_linux,
        vpc=referenced_function
    )