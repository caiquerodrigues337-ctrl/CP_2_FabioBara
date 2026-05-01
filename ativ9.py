# Exemplo de lista de logs para processamento
logs_brutos = [
    "[2025-02-20 08:15:01] [INFO] Login ok - IP: 192.168.1.10",
    "[2025-02-20 08:15:03] [WARNING] Area restrita - IP: 10.0.0.5",
    "[2025-02-20 08:15:10] [ERROR] Falha auth - IP: 185.220.101.1",
    "[2025-02-20 08:15:15] [INFO] Arquivo acessado - IP: 192.168.1.10",
    "[2025-02-20 08:15:22] [ERROR] Conexao recusada - IP: 185.220.101.1",
    "[2025-02-20 08:15:30] [WARNING] Certificado SSL - IP: 172.16.0.3",
    "[2025-02-20 08:15:35] [ERROR] Falha auth - IP: 10.0.0.5",
    "log malformado sem formato correto",
    "[2025-02-20 08:15:45] [ERROR] Timeout - IP: 185.220.101.1",
    "[2025-02-20 08:15:50] [WARNING] CPU alta - IP: 192.168.1.20",
    "[2025-02-20 08:16:01] [ERROR] Falha auth - IP: 185.220.101.1",
    "[2025-02-20 08:16:05] [INFO] Firewall ok - IP: 192.168.1.10",

]

contagem_niveis = {"INFO": 0, "WARNING": 0, "ERROR": 0}
erros_por_ip = {}
logs_processados = []

print("--- Iniciando Processamento de Logs ---")

for log in logs_brutos:
    try:
        partes = log.split(" - ")
        
        if len(partes) < 3:
            raise ValueError("Formato de log desconhecido")
            
        nivel = partes[0].strip()
        ip = partes[1].strip()
        mensagem = partes[2].strip()

        dados_log = {
            "nivel": nivel,
            "ip": ip,
            "mensagem": mensagem
        }
        logs_processados.append(dados_log)

        if nivel in contagem_niveis:
            contagem_niveis[nivel] += 1

        if nivel == "ERROR":
            erros_por_ip[ip] = erros_por_ip.get(ip, 0) + 1

    except Exception as e:
        print(f"[!] Erro ao processar linha: '{log}' | Motivo: {e}")

ip_mais_critico = None
max_erros = 0

for ip, total in erros_por_ip.items():
    if total > max_erros:
        max_erros = total
        ip_mais_critico = ip

print("\n" + "="*40)
print("RELATÓRIO FINAL DE ANÁLISE")
print("="*40)

print(f"Total de logs processados com sucesso: {len(logs_processados)}")

print("\nFrequência por Nível:")
for nivel, total in contagem_niveis.items():
    print(f"- {nivel}: {total}")

print("\nAnálise Crítica:")
if ip_mais_critico:
    print(f"O IP com mais erros detectados é {ip_mais_critico} com {max_erros} ocorrências.")
else:
    print("Nenhum erro foi detectado nos logs.")
print("="*40)