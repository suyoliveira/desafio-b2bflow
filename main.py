import os
import requests
from dotenv import load_dotenv
from supabase import create_client


load_dotenv()

URL_SUPABASE = os.getenv("SUPABASE_URL")
CHAVE_SUPABASE = os.getenv("SUPABASE_KEY")
ID_ZAPI = os.getenv("ZAPI_INSTANCE_ID")
TOKEN_ZAPI = os.getenv("ZAPI_TOKEN")


supabase = create_client(URL_SUPABASE, CHAVE_SUPABASE)

def pegar_contatos():
    try:
        print("Buscando a lista de contatos no Supabase...")

        query = supabase.table("contatos").select("nome, telefone").limit(3).execute()
        return query.data
    except Exception as erro:
        print(f"Erro ao ler dados do Supabase: {erro}")
        return []

def disparar_mensagem(nome, telefone):
    endpoint = f"https://api.z-api.io/instances/{ID_ZAPI}/token/{TOKEN_ZAPI}/send-text"
    
    headers = {
        "Content-Type": "application/json"
    }
    

    texto_mensagem = f"Olá, {nome} tudo bem com você?"
    
    corpo_requisicao = {
        "phone": telefone,
        "message": texto_mensagem
    }
    
    try:
        req = requests.post(endpoint, json=corpo_requisicao, headers=headers)
        
        if req.status_code in [200, 201]:
            print(f"Sucesso: Mensagem enviada para {nome} ({telefone})")
        else:
            print(f"Aviso: Status {req.status_code} ao enviar para {nome}. Detalhes: {req.text}")
            
    except Exception as erro:
        print(f"Erro de conexão com a Z-API ao tentar enviar para {nome}: {erro}")

if __name__ == "__main__":
    print("--- Iniciando Script de Envio ---")
    
    lista_contatos = pegar_contatos()
    
    if not lista_contatos:
        print("Nenhum contato encontrado no banco de dados. Encerrando o programa.")
    else:
        print(f"Foram encontrados {len(lista_contatos)} contatos.")
        

        for item in lista_contatos:
            nome_cliente = item.get("nome")
            num_telefone = item.get("telefone")
            
            if nome_cliente and num_telefone:
                disparar_mensagem(nome_cliente, num_telefone)
            else:
                print("Aviso: Encontrou um registro com nome ou telefone faltando.")
                
    print("--- Script Finalizado ---")