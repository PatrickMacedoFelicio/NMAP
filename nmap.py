#!/usr/bin/env python3
import socket
import ipaddress

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
    print("="*45)
    print("   Scanner de Portas TCP/UDP - Versão Didática")
    print("="*45)

    alvo = input("Digite o IP ou rede (ex: 192.168.0.1 ou 192.168.0.0/24): ").strip()
    tipo = input("Digite o tipo de varredura (tcp/udp): ").strip().lower()
    inicio = int(input("Porta inicial: "))
    fim = int(input("Porta final: "))

    # Gera lista de hosts
    try:
        rede = ipaddress.ip_network(alvo, strict=False)
        hosts = [str(ip) for ip in rede.hosts()]
    except ValueError:
        hosts = [alvo]

    for host in hosts:
        print(f"\n[+] Escaneando {host} ({tipo.upper()}) portas {inicio}-{fim}...")
        for porta in range(inicio, fim + 1):
            status = scan_tcp(host, porta) if tipo == "tcp" else scan_udp(host, porta)
            print(f"  Porta {porta}/{tipo.upper()} - {status}")

    print("\nVarredura concluída!")

if __name__ == "__main__":
    main()
