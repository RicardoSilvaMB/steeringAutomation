import boto3

ec2_ebs = boto3.client('ec2')

volumes_available_total_gb = volumes_used_total_gb = 0

#List all Available volumes (Not attached)
for vol in ec2_ebs.describe_volumes()['Volumes']:
    if vol['State'] == 'available':
        volumes_available_total_gb += vol['Size']
    else:
        volumes_used_total_gb += vol['Size']

total_size = volumes_available_total_gb + volumes_used_total_gb
#Faz para GP2 e GP3
#List snapshots total size
print ("Available: ", volumes_available_total_gb)
print ("Attached: ", volumes_used_total_gb)
print ("Total: ", total_size)
