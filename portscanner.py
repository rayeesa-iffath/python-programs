from scapy.all import IP, TCP
# Stack an IP layer on top of a TCP layer
packet = IP(dst="192.168.1.1") / TCP(dport=80)
print(f"[+] Packet structure: {packet.summary()}")
