from netmiko import  connectHandler
file = open("router.txt", "r")
data =file.readlines()
for host in data:
    host = host.strip()
    ssh = ConnectHandler(username='cisco', password='cisco123',  host=host,device_type='cisco')
    while True:
        print("you are connected to router",host)
        print("1.want to execute any show command:\n" \
              "2.want to configure any interface:\n" \
              "3.want to configure ospf:\n" \
              "4.Exit"
              )
        choice = input("enter your choice:")
        if choice == "1":
            command = input("enter show command:")
            output = ssh.send_command(command)
            print(output)
        elif choice == "2":
            int_name = input("enter interface name:")
            int_ip = int(input("enter interface ip:"))
            int_mask = input("enter interface mask:")
            int_desc = input("enter interface description:")
            int_config = [
                f"interface {int_name}",
                f"ip {int_ip}",
                f"mask {int_max}",
                f"description {int_desc}"
                f"no shutdown"
            ]
            output = ssh.send_config_set(int_config)
            print(output)
        elif choice == "3":
            ospf_process_id = input("enter ospf process id:")
            ospf_network = input("enter ospf network id:")
            ospf_wildcard = input("enter ospf wildcard mask:")
            ospf_area = input("enter ospf area id:")
            ospf_config = [
                f"router ospf {ospf_process_id}",
                f"network {ospf_network} {ospf_wildcard} area{ospf_area}"
            ]
            output = ssh.send_config_set(ospf_config)
            print(output)
        elif choice == "4":
            break
        else:
          print("you are not connected to router")