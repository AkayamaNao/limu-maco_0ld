import subprocess

proc = subprocess.Popen('printenv DATABASE_URL', stdout=subprocess.PIPE, shell=True)
maco_db = proc.stdout.read().decode('utf-8').strip()

#print(maco_db)

#maco_db = {
#    'user': 'vojmwqggktbwcq',
#    'password': 'b68a7729d76ef371569e77a475f9aeab3ef371aa15b3ba128c3ab828cedf5bf8',
#    'host': 'ec2-54-83-201-84.compute-1.amazonaws.com:5432',
#    'database': 'ddm0m8tb2f57j8',
#    'charset': 'utf8mb4',
#}
