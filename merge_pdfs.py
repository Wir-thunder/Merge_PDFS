from PyPDF2 import PdfMerger
import os

# Configuração - AJUSTE ESTES VALORES
pasta = r"C:\Users\metal\Desktop\Documentos_niss"
arquivos = [
    "icaro.pdf",
    "CamScanner 12-05-2025 14_21.pdf",  # Verifique se o nome está exato
    "CamScanner 12-05-2025 14.21 (3).pdf"
]

# Verificação
for arquivo in arquivos:
    caminho = os.path.join(pasta, arquivo)
    if not os.path.exists(caminho):
        print(f"ERRO: Arquivo não encontrado - {caminho}")
        print("Arquivos disponíveis na pasta:")
        for f in os.listdir(pasta):
            if f.lower().endswith('.pdf'):
                print(f" - {f}")
        exit()

# Processamento
try:
    merger = PdfMerger()
    for arquivo in arquivos:
        merger.append(os.path.join(pasta, arquivo))
    
    output = os.path.join(pasta, "merged.pdf")
    merger.write(output)
    print(f"Sucesso! PDF criado em: {output}")

except Exception as e:
    print(f"Erro durante a mesclagem: {str(e)}")
finally:
    merger.close()