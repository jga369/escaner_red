# punto de entrada
from scr.network import get_active_host
from scr.scanner import scan_ports
from scr.report import generate_report

def main():
    print(" ESCÁNER DE RED  ")
    
    target_network = input("Ingrese la red (Ej: 192.168.1.0/24)")
    
    print("\nBuscando hosts activos...")
    active_hosts = get_active_hosts(target_network)
    
    results = {}
    
    for host in active_hosts:
        print(f"\nEscaneando {host}...")
        open_ports= scan_ports(host)
        results[host]= open_ports
    
    generate_report(results)
    
    print("\nEscaneo finalizado. Reporte generado en carpeta reports")
    
if __name__ == "__main__":
    main()