from aws_cdk import (
aws_ec2 as ec2,
core, App
)

from Multistack.instancestack import Ec2Stack
from Multistack.vpcstack import VPCStack



app = App()
env={'region': 'us-west-2'}
infra = VPCStack(app, "infrastructure", env=env)
application = Ec2Stack(app, "application", referenced_function=infra.main_function, env=env)

app.synth()