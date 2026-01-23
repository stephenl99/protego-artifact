###
### config_remote.py - configuration for remote servers
###

NODES = [
    "128.110.218.177",
"128.110.218.224",
"128.110.218.218",
"128.110.218.189",
"128.110.218.219",
"128.110.218.225",
"128.110.218.235",
"128.110.218.221",
"128.110.218.220",
"128.110.218.238",
"128.110.218.165",
]

# Public domain or IP of server
SERVERS = NODES[0:1]
# Public domain or IP of intemediate
INTNODES = []
# Public domain or IP of client and agents
CLIENTS = NODES[1:]
# Public domain or IP of client
CLIENT = CLIENTS[0]
AGENTS = CLIENTS[1:]

# Public domain or IP of monitor
MONITOR = ""

# Username and SSH credential location to access
# the server, client, and agents via public IP
USERNAME = "slinder"
KEY_LOCATION = "/users/slinder/.ssh/id_rsa"

# Location of Shenango to be installed. With "", Shenango
# will be installed in the home direcotry
ARTIFACT_PARENT = ""

KERNEL_NAME = "caladan"

### End of config ###

ARTIFACT_PATH = ARTIFACT_PARENT
if ARTIFACT_PATH != "":
    ARTIFACT_PATH += "/"
ARTIFACT_PATH += "bw_caladan"
