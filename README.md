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

## 📜 Código-Fonte (`scanner_auto.py`)

Resumo das funções principais:

* `scan_tcp()` → realiza conexão TCP simples (connect scan).
* `scan_udp()` → envia sondagem UDP básica.
* Resultados exibidos no terminal para cada IP/porta.

> O código completo está incluído no arquivo `scanner_auto.py` deste repositório.

---

## 🚀 Como Executar

1. Instale o **Python 3** em sua máquina: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Baixe o arquivo `scanner_auto.py` do repositório.
3. Abra o terminal ou prompt de comando na pasta do arquivo.
4. Execute:

```bash
python3 scanner_auto.py
```

ou, se estiver no Linux e o script for executável:

```bash
./scanner_auto.py
```

5. Digite o IP ou rede que deseja escanear:

```
Ex.: 192.168.0.1 ou 192.168.0.0/24
```

> O script exibirá o status das portas e, ao final, aguardará que você pressione **ENTER** para encerrar.

---

## 📊 Exemplo de Saída

```
==================================================
      Scanner de Portas TCP/UDP - Automático
==================================================
Digite o IP ou rede: 192.168.2.141

[+] Escaneando 192.168.2.141 (TCP/UDP) nas portas comuns...
  Porta 22/TCP - open
  Porta 22/UDP - closed
  Porta 80/TCP - open
  Porta 80/UDP - open|filtered
Varredura concluída!
Pressione ENTER para sair...
```

---

## ✅ Critérios Atendidos

* Varredura **TCP e UDP**.
* Suporte a **IP único ou rede inteira**.
* Detecção de **portas abertas, fechadas e filtradas**.
* Funciona em **Linux** e **Windows**.
* Código organizado, funcional e documentado.
