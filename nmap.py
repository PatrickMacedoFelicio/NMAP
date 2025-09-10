
import socket
import ipaddress

def scan_tcp(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0)
    try:
        sock.connect((ip, port))
        return "open"
    except socket.timeout:
        return "filtered"
    except:
        return "closed"
    finally:
        sock.close()

def scan_udp(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(0)
    try:
        sock.sendto(b"teste", (ip, port))
        sock.recvfrom(1024)
        return "open"
    except socket.timeout:
        return "open|filtered"
    except:
        return "closed"
    finally:
        sock.close()

def main():
    print("="*50)
    print("      Scanner de Portas TCP/UDP - Faixa de Portas")
    print("="*50)

    alvo = input("Digite o IP ou rede (ex: 192.168.0.1 ou 192.168.0.0/24): ").strip()
    porta_inicial = int(input("Porta inicial: "))
    porta_final = int(input("Porta final: "))

    try:
        rede = ipaddress.ip_network(alvo, strict=False)
        hosts = [str(ip) for ip in rede.hosts()]
    except ValueError:
        hosts = [alvo]

    for host in hosts:
        print(f"\n[+] Escaneando {host} (TCP/UDP) portas {porta_inicial}-{porta_final}...")
        for porta in range(porta_inicial, porta_final + 1):
            tcp_status = scan_tcp(host, porta)
            udp_status = scan_udp(host, porta)
            print(f"  Porta {porta}/TCP - {tcp_status}")
            print(f"  Porta {porta}/UDP - {udp_status}")

    print("\nVarredura concluída!")
    input("\nPressione ENTER para sair...")

if __name__ == "__main__":
    main()
