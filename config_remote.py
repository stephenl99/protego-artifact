###
### config_remote.py - configuration for remote servers
###

NODES = [
"128.110.218.152",
"128.110.218.194",
"128.110.218.183",
"128.110.218.158",
"128.110.218.179",
"128.110.218.197",
"128.110.218.120",
"128.110.218.162",
"128.110.218.160",
"128.110.218.164",
"128.110.218.150",
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
