# 1. Definição dos conjuntos (Exemplos de IPs)
acessos_servidor = {
    "192.168.1.10", "10.0.0.5", "185.220.101.1", "172.16.0.3",
    "192.168.1.20", "91.240.118.172", "10.0.0.12", "45.33.32.156"
}

blacklist = {
    "185.220.101.1", "45.33.32.156", "91.240.118.172",
    "23.94.5.100", "104.244.72.115"
}

ips_detectados = acessos_servidor.intersection(blacklist)


ips_seguros = acessos_servidor.difference(blacklist)


blacklist_ausente = blacklist.difference(acessos_servidor)


todos_ips = acessos_servidor.union(blacklist)


print("="*50)
print("RELATÓRIO DE SEGURANÇA DE REDE")
print("="*50)

print(f"\n[!] IPs MALICIOSOS DETECTADOS (Interseção):")
print(f"    {ips_detectados if ips_detectados else 'Nenhum'}")

print(f"\n[✓] IPs SEGUROS (Diferença - Acessos limpos):")
print(f"    {ips_seguros}")

print(f"\n[-] IPs DA BLACKLIST QUE NÃO ATACARAM (Diferença Inversa):")
print(f"    {blacklist_ausente}")

print(f"\n[Σ] TOTAL DE IPs ÚNICOS MONITORADOS (União):")
print(f"    Total: {len(todos_ips)} endereços catalogados.")

print("\n" + "="*50)