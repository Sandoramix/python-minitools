#! WIP
def bitsNeededPerHosts(hosts=2):
	count=0
	while True:
		hosts_per_count=2**count-2
		if (hosts_per_count>=hosts):
			return (count,hosts_per_count)
		count+=1

def intToBinary(number:int):
	return str(bin(number)[2:])


def binaryToInt(binary:str):
	return int(binary,2)

def decimalIpToBinary(ip_array:list[int]):
	# result:list[str]=[]
	result=''
	for part in ip_array:
			binary=intToBinary(part)
			# result.append(("0"*(8-len(binary)))+binary)
			result+=("0"*(8-len(binary)))+binary
	return result

def binaryIpToDecimal(ip:str):
	if len(ip)!=32:
		return[]
	return [binaryToInt(ip[i:i+8]) for i in range(0,32,8)]
	# return [binaryToInt]


def get_ip_range(ip,sm,hostBits):
	binaryIp=decimalIpToBinary(ip)
	last_ip_bits=intToBinary(binaryToInt(binaryIp)+binaryToInt("0"*(32-hostBits) + "1"*hostBits))
	print(binaryIp)
	broadcast=binaryIpToDecimal(last_ip_bits)
	first_ip=ip[:3]+[ip[3]+1]
	last_ip=broadcast[:3]+[broadcast[3]-1]
	print(f"\tSTART IP: {forgeIp(ip)} /{32-hostBits}")
	print(f"\t\tFIRST IP: {forgeIp(first_ip)}")
	print(f"\t\tLAST IP: {forgeIp(last_ip)}")
	print(f"\t\tBROADCAST IP: {forgeIp(broadcast)}")
	print(f"\t\tSM : {forgeIp(sm)}")

	nextip=binaryIpToDecimal(intToBinary(binaryToInt(decimalIpToBinary(broadcast))+1))
	return nextip


def forgeIp(ip_array: list[int|str]):
  return (".".join(str(i) for i in ip_array))






if __name__=="__main__":
	# raw=input(f"INITIAL NETWORK [IP /SM] [example: 192.168.0.0 /24] : ")
	raw='192.168.1.0/24'
	splitted=raw.split("/")
	if len( splitted)!=2:
			exit("wrong syntax")
			
	sm=int(splitted[1])
	#print(sm)
	initial_ip=[int(i) for i in splitted[0].replace(" ","").split(".")]

	#print(raw)

	hosts=[]
	n_host=int(input("N of subnets: "))
	for i in range(n_host):
			hosts.append(int(input(f"[{i+1}]Subnet, hosts: ")))
	2

	next_ip=initial_ip
	hosts=sorted(hosts,reverse=True)
	for i in range(n_host):
			print(f"{i+1}: {hosts[i]} hosts:")
			host=hosts[i]
			query=bitsNeededPerHosts(host)
			print(query)
			host_bits=query[0]
			net_bits=32-host_bits

			subnet_mask_bits="1"*net_bits + "0"*host_bits
			subnet_mask_decimal=binaryIpToDecimal(subnet_mask_bits)

			start_ip=[next_ip[i]&subnet_mask_decimal[i] for i in range(4)]

			
			
			
			next_ip=get_ip_range(start_ip,subnet_mask_decimal,host_bits)