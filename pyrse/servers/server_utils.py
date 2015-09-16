

def parseCommand(cmd_string):
	n = 2
	groups = cmd_string.split()
	cmd = groups[0]
	key = groups[1]
	data = ' '.join(groups[n:])
	return cmd.strip().lower(), key.strip(), data
