import boto3

##Here we gather all the S3 names that client have#############################################
s3_names = boto3.client('s3')
allbuckets = s3_names.list_buckets()
list_bucket_names = []
for bucket in allbuckets['Buckets']:
    list_bucket_names.append(bucket['Name'])

print (list_bucket_names)
################################################################################################

##Now we having the names, we can go to each one and take the ammount of storage each one have##
s3_getGB = boto3.resource('s3')
totalsize_GB = size_byte_total =0

for bucket in list_bucket_names:
    object = s3_getGB.Bucket(bucket)
    for my_bucket_object in object.objects.all():
        size_byte_total += my_bucket_object.size   
    totalsize_GB += size_byte_total / (1024 * 1024 * 1024)
    totalsize_GB = round(totalsize_GB, 4)
#Faz para cada tipo de S3
print(size_byte_total, "Bytes") 
print (totalsize_GB , "GB")
################################################################################################