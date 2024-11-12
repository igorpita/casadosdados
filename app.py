import requests
import json

def pesquisar_cnpj(termo):
    url = "https://api.casadosdados.com.br/v2/public/cnpj/search"

    
    headers={
       "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
       "Accept": "application/json",
       "Content-Type": "application/json",
       "Cookie": "Cookie_1=value; Path=/; Expires=Mon, 10 Nov 2025 22:48:05 GMT;",
       # Se houver autenticação, inclua o token:
        # "Authorization": "Bearer YOUR_API_TOKEN"
   }
    
    # Crie uma sessão para armazenar cookies
    session = requests.Session()
    # Etapa 1: Fazer uma requisição inicial ao domínio para receber os cookies
    url_inicial = "http://casadosdados.com.br"
    session.get(url_inicial, headers=headers)  # Isso deve armazenar os cookies na sessão

    # Defina o cookie específico
    cookies = {
        "Cookie_1": "Cookie_1=value; Path=/; Expires=Mon, 10 Nov 2025 22:48:05 GMT;"
    }


    # Corpo da requisição
    payload = {
        "query": {
            "termo": [termo],
            "page": 1
        }
    }
    
    try:
        # Envia a requisição POST
        response = requests.post(url, headers=headers, cookies=cookies, data=json.dumps(payload))
        
        # Verifica se a resposta foi bem-sucedida
        if response.status_code == 200:
            data = response.json()
            # Verifica se há dados retornados
            if data.get("results"):
                return data["results"]
            else:
                print("Nenhuma empresa encontrada para o termo fornecido.")
                return []
        else:
            print(f"Erro na requisição: {response.status_code} - {response.text}")
            return []

    except requests.exceptions.RequestException as e:
        print(f"Erro na conexão: {e}")
        return []

# Exemplo de uso
termo_pesquisa = input("Digite o termo de pesquisa para o CNPJ: ")
resultados = pesquisar_cnpj(termo_pesquisa)

# Exibe os resultados em formato JSON
if resultados:
    print(json.dumps(resultados, indent=4, ensure_ascii=False))
