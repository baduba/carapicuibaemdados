"""
Painel 2 - Educação vs. Desempenho
"""
import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from data_collectors import DataCollector

st.set_page_config(
    page_title="Educação vs. Desempenho",
    page_icon="📚",
    layout="wide"
)

# CSS customizado
st.markdown("""
    <style>
    .question-box {
        background-color: #5B2D8E;
        color: white;
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        font-size: 1.8rem;
        font-weight: bold;
        margin-bottom: 2rem;
    }
    .insight-box {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #00C4B4;
        margin-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Título
st.title("📚 Educação vs. Desempenho")

# Pergunta em destaque
st.markdown("""
<div class="question-box">
    O dinheiro investido em educação melhorou as notas das escolas?
</div>
""", unsafe_allow_html=True)

# Carregar dados
try:
    df_gastos = DataCollector.get_educacao_gastos()
    df_ideb = DataCollector.get_ideb_data()
    
    if not df_gastos.empty and not df_ideb.empty:
        # Mesclar dados
        df = pd.merge(df_gastos, df_ideb, on='ano', how='outer').sort_values('ano')
        
        # Filtro na sidebar
        st.sidebar.markdown("### 🎚️ Filtros")
        anos_disponiveis = sorted(df['ano'].unique())
        anos_selecionados = st.sidebar.slider(
            "Período de análise",
            min_value=int(min(anos_disponiveis)),
            max_value=int(max(anos_disponiveis)),
            value=(int(min(anos_disponiveis)), int(max(anos_disponiveis)))
        )
        
        mostrar_etapa = st.sidebar.multiselect(
            "Etapa de ensino",
            ["Anos Iniciais (1º-5º)", "Anos Finais (6º-9º)"],
            default=["Anos Iniciais (1º-5º)", "Anos Finais (6º-9º)"]
        )
        
        # Filtrar dados
        df_filtrado = df[(df['ano'] >= anos_selecionados[0]) & (df['ano'] <= anos_selecionados[1])]
        
        # Criar figura com subplots
        from plotly.subplots import make_subplots
        
        fig = make_subplots(
            rows=1, cols=2,
            subplot_titles=('Gastos com Educação ao longo do tempo', 'Evolução do IDEB'),
            specs=[[{"secondary_y": False}, {"secondary_y": False}]]
        )
        
        # Gráfico 1: Barras de gastos
        fig.add_trace(
            go.Bar(
                x=df_filtrado['ano'],
                y=df_filtrado['gasto_milhoes'],
                name='Gasto com Educação',
                marker_color='#5B2D8E',
                text=df_filtrado['gasto_milhoes'].round(1),
                textposition='auto',
                texttemplate='R$ %{text}M'
            ),
            row=1, col=1
        )
        
        # Gráfico 2: Linhas do IDEB
        if "Anos Iniciais (1º-5º)" in mostrar_etapa:
            fig.add_trace(
                go.Scatter(
                    x=df_filtrado['ano'],
                    y=df_filtrado['ideb_anos_iniciais'],
                    name='IDEB Anos Iniciais',
                    line=dict(color='#00C4B4', width=3),
                    mode='lines+markers',
                    marker=dict(size=12)
                ),
                row=1, col=2
            )
        
        if "Anos Finais (6º-9º)" in mostrar_etapa:
            fig.add_trace(
                go.Scatter(
                    x=df_filtrado['ano'],
                    y=df_filtrado['ideb_anos_finais'],
                    name='IDEB Anos Finais',
                    line=dict(color='#FF6B6B', width=3),
                    mode='lines+markers',
                    marker=dict(size=12)
                ),
                row=1, col=2
            )
        
        # Linha de meta do IDEB (6.0 é a meta nacional)
        fig.add_hline(y=6.0, line_dash="dash", line_color="gray", 
                      annotation_text="Meta Nacional", row=1, col=2)
        
        # Layout
        fig.update_xaxes(title_text="Ano", row=1, col=1)
        fig.update_xaxes(title_text="Ano", row=1, col=2)
        fig.update_yaxes(title_text="Gasto (R$ milhões)", row=1, col=1)
        fig.update_yaxes(title_text="IDEB", row=1, col=2, range=[0, 10])
        
        fig.update_layout(
            height=500,
            showlegend=True,
            hovermode='x unified',
            plot_bgcolor='white'
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Métricas resumidas
        col1, col2, col3, col4 = st.columns(4)
        
        # Remove linhas com NaN para o cálculo
        df_metricas = df_filtrado.dropna()
        
        with col1:
            variacao_gastos = ((df_filtrado['gasto_milhoes'].iloc[-1] - df_filtrado['gasto_milhoes'].iloc[0]) / df_filtrado['gasto_milhoes'].iloc[0] * 100)
            st.metric(
                "Crescimento do Investimento",
                f"{variacao_gastos:.1f}%",
                delta=f"R$ {df_filtrado['gasto_milhoes'].iloc[-1] - df_filtrado['gasto_milhoes'].iloc[0]:.1f}M"
            )
        
        with col2:
            if not df_metricas.empty:
                media_gasto = df_metricas['gasto_milhoes'].mean()
                st.metric(
                    "Gasto Médio Anual",
                    f"R$ {media_gasto:.1f}M"
                )
        
        with col3:
            if 'ideb_anos_iniciais' in df_metricas.columns and not df_metricas['ideb_anos_iniciais'].isna().all():
                primeiro_ideb_inicial = df_metricas['ideb_anos_iniciais'].dropna().iloc[0]
                ultimo_ideb_inicial = df_metricas['ideb_anos_iniciais'].dropna().iloc[-1]
                variacao_inicial = ultimo_ideb_inicial - primeiro_ideb_inicial
                st.metric(
                    "IDEB Anos Iniciais",
                    f"{ultimo_ideb_inicial:.1f}",
                    delta=f"{variacao_inicial:+.1f} pts"
                )
        
        with col4:
            if 'ideb_anos_finais' in df_metricas.columns and not df_metricas['ideb_anos_finais'].isna().all():
                primeiro_ideb_final = df_metricas['ideb_anos_finais'].dropna().iloc[0]
                ultimo_ideb_final = df_metricas['ideb_anos_finais'].dropna().iloc[-1]
                variacao_final = ultimo_ideb_final - primeiro_ideb_final
                st.metric(
                    "IDEB Anos Finais",
                    f"{ultimo_ideb_final:.1f}",
                    delta=f"{variacao_final:+.1f} pts"
                )
        
        # Insights
        st.markdown("""
        <div class="insight-box">
        <h3>📊 O que os dados mostram?</h3>
        <p><strong>Correlação positiva:</strong> O aumento nos investimentos em educação está 
        acompanhado de uma melhoria consistente no IDEB (Índice de Desenvolvimento da Educação Básica), 
        indicando que os recursos estão sendo bem aplicados.</p>
        
        <p><strong>Desafio dos Anos Finais:</strong> Historicamente, o desempenho dos anos finais 
        (6º ao 9º ano) é inferior aos anos iniciais, padrão observado em todo o Brasil. Isso demanda 
        estratégias específicas para essa faixa etária.</p>
        
        <p><strong>Meta Nacional:</strong> A meta do IDEB estabelecida pelo MEC é 6.0. Carapicuíba 
        mostra evolução consistente rumo a esse objetivo.</p>
        
        <p><strong>Alinhamento com ODS:</strong> Progresso em relação ao 
        <strong>ODS 4 (Educação de qualidade)</strong>.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Tabela de dados
        with st.expander("📋 Ver dados completos"):
            st.dataframe(df_filtrado, use_container_width=True)
            
            # Informação sobre IDEB
            st.info("""
            ℹ️ **Sobre o IDEB:** O Índice de Desenvolvimento da Educação Básica combina dados de 
            aprovação escolar e médias de desempenho nas avaliações SAEB. É medido em escala de 0 a 10 
            e calculado a cada 2 anos.
            """)
    
    else:
        st.error("⚠️ Não foi possível carregar os dados. Verifique a conexão ou dados de fallback.")

except Exception as e:
    st.error(f"❌ Erro ao processar dados: {e}")
    st.info("💡 Dica: Certifique-se de que os arquivos de dados estão na pasta 'data/'")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666;">
    <small>Fontes: Portal da Transparência de Carapicuíba | INEP (Instituto Nacional de Estudos e Pesquisas Educacionais)</small>
</div>
""", unsafe_allow_html=True)
