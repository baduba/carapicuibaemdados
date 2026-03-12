"""
Carapicuíba em Dados - Dashboard de Transparência Pública
Página Inicial
"""
import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Carapicuíba em Dados",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS customizado com cores do projeto
st.markdown("""
    <style>
    .main-header {
        color: #5B2D8E;
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 0;
    }
    .sub-header {
        color: #00C4B4;
        font-size: 1.5rem;
        text-align: center;
        margin-top: 0;
        margin-bottom: 2rem;
    }
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
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">📊 Carapicuíba em Dados</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Transparência pública em linguagem acessível</p>', unsafe_allow_html=True)

# Introdução
st.markdown("""
<div class="card-highlight">
<h3>Bem-vindo ao projeto Carapicuíba em Dados!</h3>
<p>Este dashboard apresenta dados públicos do município de Carapicuíba de forma visual e acessível, 
permitindo que cidadãos compreendam melhor a relação entre investimentos públicos e resultados na vida real.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Painéis disponíveis
st.markdown("### 🎯 Painéis Disponíveis")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
    <h4>💧 Painel 1: Saneamento vs. Saúde</h4>
    <p><strong>Pergunta:</strong> O investimento em saneamento reduziu doenças em Carapicuíba?</p>
    <p>Cruza dados de investimento em saneamento básico com internações por doenças relacionadas à água.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
    <h4>📚 Painel 2: Educação vs. Desempenho</h4>
    <p><strong>Pergunta:</strong> O dinheiro investido em educação melhorou as notas das escolas?</p>
    <p>Relaciona gastos com educação e evolução do IDEB nas escolas municipais.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    <h4>💰 Painel 3: Riqueza vs. Mortalidade Infantil</h4>
    <p><strong>Pergunta:</strong> A cidade ficou mais rica mas os bebês vivem mais?</p>
    <p>Compara evolução do PIB per capita com taxa de mortalidade infantil.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
    <h4>🏥 Painel 4: Cobertura de Saúde</h4>
    <p><strong>Pergunta:</strong> Tem unidade de saúde onde tem gente?</p>
    <p>Analisa distribuição de UBS em relação à densidade populacional por região.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Como usar
st.markdown("### 📖 Como usar este dashboard")

st.markdown("""
1. **Navegue pelos painéis** usando o menu lateral esquerdo
2. **Explore os gráficos interativos** - passe o mouse sobre os pontos para ver detalhes
3. **Aplique filtros** quando disponíveis para visualizar períodos específicos
4. **Leia as interpretações** abaixo de cada gráfico para entender o que os dados significam

**Fontes dos dados:**
- 📊 IBGE/SIDRA - Dados demográficos e econômicos
- 🏥 DataSUS - Dados de saúde pública
- 💧 SNIS - Sistema Nacional de Informações sobre Saneamento
- 📚 INEP - Instituto Nacional de Estudos e Pesquisas Educacionais
- 💵 Portal da Transparência - Gastos públicos municipais
""")

st.markdown("---")

# Footer
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem 0;">
    <p>Desenvolvido para promover transparência e participação cidadã</p>
    <p>Alinhado com os Objetivos de Desenvolvimento Sustentável (ODS) da ONU</p>
    <p style="color: #5B2D8E; font-weight: bold;">Carapicuíba em Dados © 2026</p>
</div>
""", unsafe_allow_html=True)
