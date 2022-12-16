#! WIP
def first_closest(num):
    res=1
    i=0
    while True:
        if res-2>num:
            return (i,res)
        res=res*2
        i+=1


def int_bin(n):
    return str(bin(n))[2:]

def bin_int(n):
    return int(n,2)

def dec_array_to_bin(ip_array):
    out=''
    for i in ip_array:
        binary=int_bin(i)
        out+="0"*(8-len(binary))+binary
    return out


def get_ip_range(ip,sm,host_bits):
    ip_bits=dec_array_to_bin(ip)
    last_ip_bits=int_bin(bin_int(ip_bits)+bin_int("0"*(32-host_bits) + "1"*host_bits))

    broadcast=bin_str_to_dec_array(last_ip_bits)
    first_ip=ip[:3]+[ip[3]+1]
    last_ip=broadcast[:3]+[broadcast[3]-1]
    print(f"\tSTART IP: {dec_array_to_bin_str(ip)} /{32-host_bits}")
    print(f"\t\tFIRST IP: {dec_array_to_bin_str(first_ip)}")
    print(f"\t\tLAST IP: {dec_array_to_bin_str(last_ip)}")
    print(f"\t\tBROADCAST IP: {dec_array_to_bin_str(broadcast)}")
    print(f"\t\tSM : {dec_array_to_bin_str(sm)}")

    nextip=bin_str_to_dec_array(int_bin(bin_int(dec_array_to_bin(broadcast))+1))
    return nextip

def bin_str_to_dec_array(ip):
    if len(ip)!=32:
        return[]
    return [bin_int(ip[i:i+8]) for i in range(0,32,8)]

def dec_array_to_bin_str(ip_array):
    return (".".join(str(i) for i in ip_array))






if __name__=="__main__":
	raw=input(f"MAIN NETWORK [IP /SM] [example: 192.168.0.0 /24] : ")
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
			query=first_closest(host)
			print(query)
			host_bits=query[0]
			net_bits=32-host_bits

			subnet_mask_bits="1"*net_bits + "0"*host_bits
			subnet_mask_decimal=bin_str_to_dec_array(subnet_mask_bits)

			start_ip=[next_ip[i]&subnet_mask_decimal[i] for i in range(4)]

			
			
			
			next_ip=get_ip_range(start_ip,subnet_mask_decimal,host_bits)