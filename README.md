# Carapicuíba em Dados 📊

**Transparência pública em linguagem acessível**

Dashboard público que coleta automaticamente dados de APIs abertas e exibe cruzamentos de indicadores municipais de Carapicuíba em painéis visuais simples e acessíveis.

![Badge: Python](https://img.shields.io/badge/Python-3.11-blue)
![Badge: Streamlit](https://img.shields.io/badge/Streamlit-1.31-red)
![Badge: Docker](https://img.shields.io/badge/Docker-Ready-blue)

---

## 🎯 Sobre o Projeto

Este projeto tem como objetivo democratizar o acesso a dados públicos do município de Carapicuíba (SP), apresentando informações complexas de forma visual e compreensível para todos os cidadãos.

### Painéis Disponíveis

1. **💧 Saneamento vs. Saúde**
   - Pergunta: "O investimento em saneamento reduziu doenças em Carapicuíba?"
   - Cruza dados de investimento em saneamento básico com internações por doenças hídricas

2. **📚 Educação vs. Desempenho**
   - Pergunta: "O dinheiro investido em educação melhorou as notas das escolas?"
   - Relaciona gastos com educação e evolução do IDEB

3. **💰 PIB vs. Mortalidade Infantil**
   - Pergunta: "A cidade ficou mais rica mas os bebês vivem mais?"
   - Compara evolução do PIB per capita com taxa de mortalidade infantil

4. **🏥 Cobertura de Saúde**
   - Pergunta: "Tem unidade de saúde onde tem gente?"
   - Analisa distribuição de UBS em relação à densidade populacional

---

## 🚀 Quick Start

### Pré-requisitos

- Docker instalado
- Git

### Rodando com Docker (Recomendado)

```bash
# Clone o repositório
git clone https://github.com/baduba/carapicuibaemdados.git
cd carapicuibaemdados

# Build da imagem Docker
docker build -t carapicuiba-dados .

# Run do container
docker run -p 8501:8501 carapicuiba-dados
```

Acesse: **http://localhost:8501**

### Rodando localmente (sem Docker)

```bash
# Clone o repositório
git clone https://github.com/baduba/carapicuibaemdados.git
cd carapicuibaemdados

# Instale as dependências
pip install -r requirements.txt

# Execute o Streamlit
streamlit run app.py
```

---

## 📁 Estrutura do Projeto

```
carapicuibaemdados/
├── app.py                          # Página inicial
├── data_collectors.py              # Módulo de coleta de dados
├── pages/                          # Painéis do dashboard
│   ├── 1_saneamento_vs_saude.py
│   ├── 2_educacao_vs_desempenho.py
│   ├── 3_pib_vs_mortalidade.py
│   ├── 4_cobertura_saude.py
│   └── 5_sobre.py
├── data/                           # Dados de fallback (CSV)
│   ├── saneamento.csv
│   ├── saude_internacoes.csv
│   ├── educacao_gastos.csv
│   ├── ideb.csv
│   ├── mortalidade_infantil.csv
│   └── ubs_regiao.csv
├── Dockerfile                      # Container Docker
├── requirements.txt                # Dependências Python
├── .streamlit/
│   └── config.toml                 # Configurações do Streamlit
└── README.md
```

---

## 📊 Fontes de Dados

- **IBGE/SIDRA**: PIB per capita, população, densidade demográfica
- **DataSUS**: Internações, mortalidade infantil, cadastro de UBS (CNES)
- **SNIS**: Sistema Nacional de Informações sobre Saneamento
- **INEP**: IDEB (Índice de Desenvolvimento da Educação Básica)
- **Portal da Transparência**: Gastos municipais com educação

---

## 🐳 Deploy Automático

O projeto está configurado para deploy automático no **Sliplane**. A cada commit na branch principal, o projeto é automaticamente construído e deployado.

### Configuração Sliplane

1. Conecte seu repositório GitHub ao Sliplane
2. Configure as variáveis de ambiente (se necessário)
3. O Dockerfile será usado automaticamente para build
4. A aplicação estará disponível na URL fornecida pelo Sliplane

---

## 🌍 Alinhamento com ODS da ONU

Este projeto monitora indicadores relacionados aos seguintes Objetivos de Desenvolvimento Sustentável:

- **ODS 3**: Saúde e Bem-Estar
- **ODS 4**: Educação de Qualidade
- **ODS 6**: Água Potável e Saneamento
- **ODS 11**: Cidades e Comunidades Sustentáveis

---

## 💻 Tecnologias Utilizadas

- **Python 3.11**: Linguagem principal
- **Streamlit**: Framework para dashboard
- **Plotly**: Visualizações interativas
- **Pandas**: Manipulação de dados
- **Docker**: Containerização
- **GitHub + Sliplane**: CI/CD

---

## 🎨 Identidade Visual

- **Cor primária**: `#5B2D8E` (roxo)
- **Cor secundária**: `#00C4B4` (verde-água)
- **Fonte**: Sans serif (padrão Streamlit)

---

## 🤝 Como Contribuir

Contribuições são bem-vindas! Este é um projeto de código aberto voltado para o bem público.

### Formas de contribuir:

1. **Melhorias nos dados**: Sugira novas fontes ou indicadores
2. **Novos painéis**: Proponha novos cruzamentos de dados
3. **Correções**: Reporte bugs ou problemas
4. **Documentação**: Melhore explicações
5. **Acessibilidade**: Sugira melhorias de usabilidade

### Como contribuir:

```bash
# Fork o projeto
# Crie uma branch
git checkout -b feature/nova-funcionalidade

# Faça suas alterações e commit
git commit -m "Adiciona nova funcionalidade"

# Push para sua branch
git push origin feature/nova-funcionalidade

# Abra um Pull Request
```

---

## 📝 Licença

Domínio Público - Livre para uso educacional e cívico.

Os dados são provenientes de fontes oficiais e obedecem às respectivas licenças de cada órgão.

---

## 📧 Contato

**GitHub**: https://github.com/baduba/carapicuibaemdados  
**Projeto**: Carapicuíba em Dados  
**Ano**: 2026

---

## 🌟 Agradecimentos

Agradecemos a todos os órgãos públicos que disponibilizam dados abertos:
- IBGE
- Ministério da Saúde (DataSUS)
- INEP
- SNIS
- Prefeitura de Carapicuíba

---

**"Dados abertos são a base para uma sociedade mais justa e transparente"**
