-- HEAD --

description = [[
This is a script that determines whether or not a port is open.
]]

author = "Null Byte"
link = "https://null-byte.wonderhowto.com/how-to/get-started-writing-your-own-nse-scripts-for-nmap-0187403/"

-- RULE --

portrule = function(host, port)
	return port.protocol == "tcp"
		and port.state == "open"
end

-- ACTION --

action = function(host, port)
	return "Hey, this port is open!"
end
