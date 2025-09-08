#!/usr/bin/env python3
import socket
import ipaddress

# Portas mais comuns a serem testadas
PORTAS_COMUNS = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3389]

def scan_tcp(ip, port):
    """Varredura básica TCP (connect scan)"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
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
    """Varredura básica UDP (sondagem simples)"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(1)
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
    print("      Scanner de Portas TCP/UDP - Automático")
    print("="*50)

    alvo = input("Digite o IP ou rede (ex: 192.168.0.1 ou 192.168.0.0/24): ").strip()

    # Gera lista de hosts a partir de IP único ou rede
    try:
        rede = ipaddress.ip_network(alvo, strict=False)
        hosts = [str(ip) for ip in rede.hosts()]
    except ValueError:
        hosts = [alvo]

    for host in hosts:
        print(f"\n[+] Escaneando {host} (TCP/UDP) nas portas comuns...")
        for porta in PORTAS_COMUNS:
            tcp_status = scan_tcp(host, porta)
            udp_status = scan_udp(host, porta)
            print(f"  Porta {porta}/TCP - {tcp_status}")
            print(f"  Porta {porta}/UDP - {udp_status}")

    print("\nVarredura concluída!")
    input("\nPressione ENTER para sair...")

if __name__ == "__main__":
    main()
