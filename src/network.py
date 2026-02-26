# Detecta hosts activos usando ping

import subprocess
import ipaddress

def get_active_hosts(network):
    active_hosts=[]
    
    net= ipaddress.ip_network(network, strict=False)
    
    for ip in net.hosts():
        ip_str= str(ip)
        
        try:
            result= subprocess.run(
                ["ping", "-n","1","-w", "500", ip_str],
                stdout=subprocess.DEVNULL
            )
            if result.returncode == 0:
                print(f"Host activo: {ip_str}")
                active_hosts.append(ip_str)
        
        except Exception:
            pass
        
    return active_hosts