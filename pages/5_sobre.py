"""
Página Sobre - Fontes, Metodologia e ODS
"""
import streamlit as st

st.set_page_config(
    page_title="Sobre o Projeto",
    page_icon="ℹ️",
    layout="wide"
)

# CSS customizado
st.markdown("""
    <style>
    .card {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #5B2D8E;
        margin-bottom: 1rem;
    }
    .card-highlight {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #00C4B4;
        margin-bottom: 1rem;
    }
    .ods-box {
        background-color: #fff;
        padding: 1rem;
        border-radius: 5px;
        border: 2px solid #5B2D8E;
        margin: 0.5rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Título
st.title("ℹ️ Sobre o Projeto")

st.markdown("""
<div class="card-highlight">
<h2>Carapicuíba em Dados</h2>
<p><strong>Transparência pública em linguagem acessível</strong></p>
<p>Dashboard desenvolvido para promover o acesso democrático a dados públicos do município de Carapicuíba, 
apresentando informações complexas de forma visual e compreensível para todos os cidadãos.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Objetivo do projeto
st.markdown("### 🎯 Objetivo")

st.markdown("""
Este projeto tem como missão:
- **Democratizar o acesso** a dados públicos municipais
- **Facilitar a compreensão** de informações técnicas através de visualizações intuitivas
- **Promover a participação cidadã** através do conhecimento baseado em evidências
- **Monitorar o progresso** da cidade em indicadores essenciais de desenvolvimento
- **Alinhar com as metas globais** dos Objetivos de Desenvolvimento Sustentável (ODS) da ONU
""")

st.markdown("---")

# Fontes de dados
st.markdown("### 📊 Fontes de Dados")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
    <h4>🏛️ IBGE - Instituto Brasileiro de Geografia e Estatística</h4>
    <p><strong>Dados utilizados:</strong></p>
    <ul>
        <li>PIB per capita municipal</li>
        <li>População estimada</li>
        <li>Densidade demográfica</li>
    </ul>
    <p><strong>API:</strong> <code>servicodados.ibge.gov.br</code></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
    <h4>📚 INEP - Instituto Nacional de Estudos e Pesquisas Educacionais</h4>
    <p><strong>Dados utilizados:</strong></p>
    <ul>
        <li>IDEB (Índice de Desenvolvimento da Educação Básica)</li>
        <li>Notas por etapa de ensino</li>
    </ul>
    <p><strong>Site:</strong> <code>www.gov.br/inep</code></p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    <h4>🏥 DataSUS - Departamento de Informática do SUS</h4>
    <p><strong>Dados utilizados:</strong></p>
    <ul>
        <li>Internações por doenças hídricas</li>
        <li>Taxa de mortalidade infantil</li>
        <li>Cadastro Nacional de Estabelecimentos de Saúde (CNES)</li>
    </ul>
    <p><strong>Site:</strong> <code>datasus.saude.gov.br</code></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
    <h4>💧 SNIS - Sistema Nacional de Informações sobre Saneamento</h4>
    <p><strong>Dados utilizados:</strong></p>
    <ul>
        <li>Investimentos em saneamento básico</li>
        <li>Cobertura de água e esgoto</li>
    </ul>
    <p><strong>Site:</strong> <code>www.snis.gov.br</code></p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Metodologia
st.markdown("### 🔬 Metodologia")

st.markdown("""
<div class="card">
<h4>Coleta e Processamento de Dados</h4>

<p><strong>1. Coleta Automática:</strong> O sistema tenta coletar dados diretamente das APIs públicas oficiais.</p>

<p><strong>2. Dados de Fallback:</strong> Em caso de indisponibilidade das APIs, o sistema utiliza dados 
mockados realistas armazenados localmente, garantindo que o dashboard sempre funcione.</p>

<p><strong>3. Atualização:</strong> Os dados são carregados a cada acesso à página, garantindo informações 
sempre atualizadas quando as APIs estão disponíveis.</p>

<p><strong>4. Visualização:</strong> Utilizamos a biblioteca Plotly para criar gráficos interativos que 
permitem exploração detalhada dos dados.</p>

<p><strong>5. Linguagem Acessível:</strong> Cada painel apresenta uma pergunta clara e interpretações 
em linguagem simples, sem jargões técnicos.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ODS - Objetivos de Desenvolvimento Sustentável
st.markdown("### 🌍 Alinhamento com os ODS da ONU")

st.markdown("""
Os **Objetivos de Desenvolvimento Sustentável (ODS)** são 17 metas globais estabelecidas pela 
Organização das Nações Unidas para serem alcançadas até 2030, abordando os principais desafios 
da humanidade.

Este dashboard monitora indicadores relacionados aos seguintes ODS:
""")

col_a, col_b = st.columns(2)

with col_a:
    st.markdown("""
    <div class="ods-box">
    <h4>🩺 ODS 3 - Saúde e Bem-Estar</h4>
    <p><strong>Meta 3.2:</strong> Reduzir mortalidade infantil</p>
    <p><strong>Meta 3.8:</strong> Cobertura universal de saúde</p>
    <p><strong>Painéis relacionados:</strong> Saneamento vs. Saúde, PIB vs. Mortalidade, Cobertura de Saúde</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="ods-box">
    <h4>💧 ODS 6 - Água Potável e Saneamento</h4>
    <p><strong>Meta 6.1:</strong> Acesso universal à água potável</p>
    <p><strong>Meta 6.2:</strong> Saneamento e higiene adequados</p>
    <p><strong>Painéis relacionados:</strong> Saneamento vs. Saúde</p>
    </div>
    """, unsafe_allow_html=True)

with col_b:
    st.markdown("""
    <div class="ods-box">
    <h4>📚 ODS 4 - Educação de Qualidade</h4>
    <p><strong>Meta 4.1:</strong> Educação primária e secundária de qualidade</p>
    <p><strong>Meta 4.5:</strong> Igualdade de acesso à educação</p>
    <p><strong>Painéis relacionados:</strong> Educação vs. Desempenho</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="ods-box">
    <h4>🏙️ ODS 11 - Cidades e Comunidades Sustentáveis</h4>
    <p><strong>Meta 11.1:</strong> Acesso a serviços básicos</p>
    <p><strong>Meta 11.6:</strong> Reduzir impacto ambiental</p>
    <p><strong>Painéis relacionados:</strong> Cobertura de Saúde, Saneamento vs. Saúde</p>
    </div>
    """, unsafe_allow_html=True)

st.info("""
💡 **Por que os ODS são importantes?**  
Os ODS fornecem um framework global para medir progresso e desenvolvimento. Ao alinhar os indicadores 
municipais com os ODS, Carapicuíba pode comparar seu desempenho com padrões internacionais e identificar 
áreas prioritárias para investimento.
""")

st.markdown("---")

# Tecnologias utilizadas
st.markdown("### 💻 Tecnologias Utilizadas")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    **Frontend & Backend:**
    - Python 3.11
    - Streamlit
    - Pandas
    - Plotly
    """)

with col2:
    st.markdown("""
    **Deploy & Infraestrutura:**
    - Docker
    - Sliplane (CI/CD)
    - GitHub
    """)

with col3:
    st.markdown("""
    **Fontes de Dados:**
    - APIs REST públicas
    - Arquivos CSV (fallback)
    - Coleta automática
    """)

st.markdown("---")

# Estrutura do projeto
st.markdown("### 📁 Estrutura do Projeto")

st.code("""
carapicuibaemdados/
├── app.py                          # Página inicial
├── data_collectors.py              # Módulo de coleta de dados
├── pages/                          # Painéis do dashboard
│   ├── 1_saneamento_vs_saude.py
│   ├── 2_educacao_vs_desempenho.py
│   ├── 3_pib_vs_mortalidade.py
│   ├── 4_cobertura_saude.py
│   └── 5_sobre.py
├── data/                           # Dados de fallback
│   ├── saneamento.csv
│   ├── saude_internacoes.csv
│   ├── educacao_gastos.csv
│   ├── ideb.csv
│   ├── mortalidade_infantil.csv
│   └── ubs_regiao.csv
├── Dockerfile                      # Container Docker
├── requirements.txt                # Dependências Python
└── .streamlit/
    └── config.toml                 # Configurações do Streamlit
""", language="text")

st.markdown("---")

# Contribuindo
st.markdown("### 🤝 Como Contribuir")

st.markdown("""
Este é um projeto de código aberto voltado para o bem público. Contribuições são bem-vindas!

**Formas de contribuir:**
1. **Melhorias nos dados:** Sugira novas fontes de dados ou indicadores
2. **Novos painéis:** Proponha novos cruzamentos de dados relevantes
3. **Correções:** Reporte bugs ou problemas de visualização
4. **Documentação:** Melhore explicações e interpretações dos dados
5. **Acessibilidade:** Sugira melhorias para tornar o dashboard mais acessível

**Repositório:** [github.com/baduba/carapicuibaemdados](https://github.com/baduba/carapicuibaemdados)
""")

st.markdown("---")

# Contato e Licença
st.markdown("### 📧 Contato e Licença")

col_x, col_y = st.columns(2)

with col_x:
    st.markdown("""
    **Desenvolvido por:** Comunidade Carapicuíba em Dados  
    **GitHub:** https://github.com/baduba/carapicuibaemdados  
    **Ano:** 2026
    """)

with col_y:
    st.markdown("""
    **Licença:** Domínio Público  
    **Dados:** Licenças específicas de cada fonte oficial  
    **Uso:** Livre para fins educacionais e cívicos
    """)

st.markdown("---")

# Footer motivacional
st.markdown("""
<div style="text-align: center; padding: 2rem; background-color: #5B2D8E; color: white; border-radius: 10px;">
    <h3>🌟 "Dados abertos são a base para uma sociedade mais justa e transparente" 🌟</h3>
    <p>Obrigado por usar o Carapicuíba em Dados e contribuir para uma cidade mais informada e participativa!</p>
</div>
""", unsafe_allow_html=True)
