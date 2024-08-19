from scapy.all import sniff, IP, TCP, UDP

def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto

        # Determine protocol type
        if protocol == 6:  # TCP
            proto_type = "TCP"
            if packet[TCP].payload:
                payload = packet[TCP].payload
            else:
                payload = "No Payload"
        elif protocol == 17:  # UDP
            proto_type = "UDP"
            if packet[UDP].payload:
                payload = packet[UDP].payload
            else:
                payload = "No Payload"
        else:
            proto_type = "Other"
            payload = "N/A"

        print(f"[+] Source: {ip_src} -> Destination: {ip_dst} | Protocol: {proto_type} | Payload: {payload}")

# Capture packets on interface (you may need to replace 'eth0' with your network interface name)
sniff(prn=packet_callback, store=0, filter="ip")
