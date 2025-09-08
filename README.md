# 🖥️ Scanner de Portas TCP/UDP

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python\&logoColor=white)

---

## 🎯 Objetivo

Desenvolver uma ferramenta capaz de realizar a varredura de portas **TCP** e **UDP** em um ou mais endereços IP.
A ferramenta indica se as portas estão **abertas**, **fechadas** ou **filtradas**.

---

## 🛠️ Ferramenta Desenvolvida

* Implementada em **Python 3**, utilizando apenas bibliotecas padrão (`socket`, `ipaddress`).
* Aceita **um IP único** ou **uma rede inteira** (ex.: `192.168.0.0/24`).
* Realiza varredura **automática** em TCP e UDP.
* Testa um conjunto de **portas comuns**.
* Exibe os estados:

  * `open` → Porta aberta
  * `closed` → Porta fechada
  * `filtered` → Sem resposta (possível firewall)
  * `open|filtered` → No UDP, pode estar aberta ou filtrada

---

## 📜 Código-Fonte (`nmap.py`)

Resumo das funções principais:

* `scan_tcp()` → realiza conexão TCP simples (connect scan).
* `scan_udp()` → envia sondagem UDP básica.
* Resultados exibidos no terminal para cada IP/porta.

> O código completo está incluído no arquivo `nmap.py` deste repositório.

---

## 🚀 Como Executar

1. Instale o **Python 3** em sua máquina: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Baixe o arquivo `nmap.py` do repositório.
3. Abra o terminal ou prompt de comando na pasta do arquivo.
4. Execute:

```bash
python3 nmap.py
```

ou, se estiver no Linux e o script for executável:

```bash
./nmap.py
```

5. Digite o IP ou rede que deseja escanear:

```
Ex.: 192.168.0.1 ou 192.168.0.0/24
```

> O script exibirá o status das portas e, ao final, aguardará que você pressione **ENTER** para encerrar.


