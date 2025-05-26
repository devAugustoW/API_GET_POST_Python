# 🚀 API Python com Testes e CI/CD

## 📋 Visão Geral

Este projeto demonstra o desenvolvimento de uma **API REST em Python** , incluindo testes automatizados, CI/CD e testes de performance.

### 🎯 Objetivos da Atividade
- Desenvolver API REST com endpoints GET e POST
- Implementar testes unitários com pytest
- Configurar pipeline CI/CD com GitHub Actions
- Realizar testes de stress/performance
- Aplicar boas práticas de desenvolvimento

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Versão | Propósito |
|------------|--------|-----------|
| **Python** | 3.9+ | Linguagem principal |
| **Flask** | 2.3.3 | Framework web para API |
| **pytest** | 7.4.3 | Testes unitários |
| **Locust** | 2.17.0 | Testes de performance |
| **GitHub Actions** | - | CI/CD Pipeline |

---


## 📁 Estrutura do Projeto

```
atividade_api/
├── .github/
│ └── workflows/
│ └── ci.yml 
├── app/
│ ├── init.py
│ └── main.py 
├── tests/
│ ├── init.py
│ ├── test_main.py 
│ └── test_stress.py 
├── .gitignore
├── requirements.txt 
└── README.md 
```

## 📋 Etapas do Desenvolvimento

### 1. 🔧 Configuração do Ambiente
- Criação da estrutura de pastas do projeto
- Configuração do ambiente virtual Python
- Definição das dependências no `requirements.txt`
- Configuração inicial do Git

### 2. 🚀 Criação da API
- Implementação do servidor Flask básico
- Criação de endpoints GET e POST
- Estruturação de dados em memória
- Tratamento de erros HTTP

**Endpoints implementados:**
```python
GET  /api/items        # Lista todos os itens
GET  /api/items/<id>   # Busca item por ID
POST /api/items        # Adiciona novo item
```

### 3. 🧪 Testes Manuais
- Teste dos endpoints via navegador
- Teste de requisições POST via Insomnia
- Verificação de respostas e status codes
- Validação do comportamento da API

**Testes realizados:**
```bash
# Teste GET - Listar itens
http://localhost:5000/api/items

# Teste GET - Buscar por ID
http://localhost:5000/api/items/1

# Teste GET - Item não encontrado
http://localhost:5000/api/items/999

# Teste POST - Adicionar item (via Insomnia)
POST /api/items
{
  "id": 4,
  "nome": "Python",
  "preco": 25.00
}
```

### 4. 🧪 Testes Automatizados com pytest
- Configuração do ambiente de testes
- Criação de testes unitários para cada endpoint
- Implementação de assertions para validar comportamento
- Execução e análise dos resultados

**Testes implementados:**
```python
def test_get_items()           # Testa listagem de itens
def test_get_item_by_id()      # Testa busca por ID
def test_get_item_not_found()  # Testa erro 404
def test_post_new_item()       # Testa criação de item
```

### 5. ⚙️ CI/CD com GitHub Actions
- Criação do workflow de CI/CD
- Configuração de execução automática de testes
- Definição de triggers (push, pull request)
- Implementação de pipeline de qualidade

**Pipeline implementado:**
1. **Checkout do código** - Baixa o código do repositório
2. **Setup Python** - Configura ambiente Python
3. **Instalar dependências** - Instala bibliotecas do requirements.txt
4. **Executar testes** - Roda pytest automaticamente
5. **Verificar qualidade** - Análise de código

### 6. 💪 Testes de Performance com Locust
- Instalação e configuração do Locust
- Criação de cenários de teste de carga
- Simulação de usuários simultâneos
- Análise de métricas de performance


**Cenários testados:**
```python
@task(3) def get_items()      # Simula listagem (peso 3)
@task(1) def get_item_by_id() # Simula busca (peso 1)  
@task(1) def create_item()    # Simula criação (peso 1)
```

## 🎯 Conclusão
Este projeto construi me permitiu compreender como os testes manuais, workflows de CI/CD no github e testes de estresse funcionam na prática!

