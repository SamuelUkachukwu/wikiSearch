import os
from dotenv import load_dotenv
import paramiko

# Load variables from .env
load_dotenv()

instance_ip = os.getenv("EC2_IP")
securityKeyFile = os.getenv("EC2_KEY")
ec2_user = os.getenv("EC2_USER")
wiki_file_location = os.getenv("WIKI_FILE")
venv_path = os.getenv("VENV_PATH")

# will change search term later
# query = "Barack Obama"
def run_wiki_on_ec2(query):
    """
    Connects to EC2, runs wiki.py with the search query,
    and returns the output as a single string.
    """

    # Command to activate venv and run wiki.py
    cmd = f"source {venv_path} && python {wiki_file_location} '{query}'"

    try:
        # Connect/ssh to EC2 instance
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        key = paramiko.RSAKey.from_private_key_file(securityKeyFile)
        client.connect(hostname=instance_ip, username=ec2_user, pkey=key)

        # Execute a command(cmd) after connecting/ssh to an instance
        stdin, stdout, stderr = client.exec_command(cmd)
        stdin.close()

        errors = stderr.readlines()
        if errors:
            print("EC2 ERRORS:", errors)

        # Get/Use the result
        output = stdout.readlines()
        output_as_string = "".join(output)

        # Close the client connection once the job is done
        client.close()

        return output_as_string

    except Exception as e:
        print("Exception:", e)
