"""
Painel 1 - Saneamento vs. Saúde
"""
import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from data_collectors import DataCollector

st.set_page_config(
    page_title="Saneamento vs. Saúde",
    page_icon="💧",
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
st.title("💧 Saneamento vs. Saúde")

# Pergunta em destaque
st.markdown("""
<div class="question-box">
    O investimento em saneamento reduziu doenças em Carapicuíba?
</div>
""", unsafe_allow_html=True)

# Carregar dados
try:
    df_saneamento = DataCollector.get_saneamento_data()
    df_saude = DataCollector.get_saude_data()
    
    if not df_saneamento.empty and not df_saude.empty:
        # Mesclar dados
        df = pd.merge(df_saneamento, df_saude, on='ano')
        
        # Filtro de ano na sidebar
        st.sidebar.markdown("### 🎚️ Filtros")
        anos_disponiveis = sorted(df['ano'].unique())
        anos_selecionados = st.sidebar.slider(
            "Período de análise",
            min_value=int(min(anos_disponiveis)),
            max_value=int(max(anos_disponiveis)),
            value=(int(min(anos_disponiveis)), int(max(anos_disponiveis)))
        )
        
        # Filtrar dados
        df_filtrado = df[(df['ano'] >= anos_selecionados[0]) & (df['ano'] <= anos_selecionados[1])]
        
        # Criar gráfico de linha dupla
        fig = go.Figure()
        
        # Linha de investimento em saneamento
        fig.add_trace(go.Scatter(
            x=df_filtrado['ano'],
            y=df_filtrado['investimento_milhoes'],
            name='Investimento em Saneamento (R$ milhões)',
            line=dict(color='#00C4B4', width=3),
            mode='lines+markers',
            marker=dict(size=10),
            yaxis='y1'
        ))
        
        # Linha de internações
        fig.add_trace(go.Scatter(
            x=df_filtrado['ano'],
            y=df_filtrado['internacoes'],
            name='Internações por Doenças Hídricas',
            line=dict(color='#5B2D8E', width=3),
            mode='lines+markers',
            marker=dict(size=10),
            yaxis='y2'
        ))
        
        # Layout com dois eixos Y
        fig.update_layout(
            title={
                'text': 'Investimento em Saneamento vs. Internações por Doenças Hídricas',
                'x': 0.5,
                'xanchor': 'center',
                'font': {'size': 20}
            },
            xaxis=dict(
                title='Ano',
                showgrid=True,
                gridcolor='#f0f0f0'
            ),
            yaxis=dict(
                title='Investimento (R$ milhões)',
                titlefont=dict(color='#00C4B4'),
                tickfont=dict(color='#00C4B4'),
                showgrid=True,
                gridcolor='#f0f0f0'
            ),
            yaxis2=dict(
                title='Internações',
                titlefont=dict(color='#5B2D8E'),
                tickfont=dict(color='#5B2D8E'),
                overlaying='y',
                side='right'
            ),
            hovermode='x unified',
            height=500,
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            ),
            plot_bgcolor='white'
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Métricas resumidas
        col1, col2, col3 = st.columns(3)
        
        with col1:
            variacao_investimento = ((df_filtrado['investimento_milhoes'].iloc[-1] - df_filtrado['investimento_milhoes'].iloc[0]) / df_filtrado['investimento_milhoes'].iloc[0] * 100)
            st.metric(
                "Crescimento do Investimento",
                f"{variacao_investimento:.1f}%",
                delta=f"{df_filtrado['investimento_milhoes'].iloc[-1] - df_filtrado['investimento_milhoes'].iloc[0]:.1f}M",
                delta_color="normal"
            )
        
        with col2:
            variacao_internacoes = ((df_filtrado['internacoes'].iloc[-1] - df_filtrado['internacoes'].iloc[0]) / df_filtrado['internacoes'].iloc[0] * 100)
            st.metric(
                "Variação nas Internações",
                f"{variacao_internacoes:.1f}%",
                delta=f"{df_filtrado['internacoes'].iloc[-1] - df_filtrado['internacoes'].iloc[0]}",
                delta_color="inverse"
            )
        
        with col3:
            st.metric(
                "Internações Evitadas (estimativa)",
                f"{abs(df_filtrado['internacoes'].iloc[-1] - df_filtrado['internacoes'].iloc[0])}",
                delta="desde " + str(anos_selecionados[0]),
                delta_color="off"
            )
        
        # Insights
        st.markdown("""
        <div class="insight-box">
        <h3>📊 O que os dados mostram?</h3>
        <p><strong>Relação inversa positiva:</strong> À medida que o investimento em saneamento básico 
        aumenta, há uma redução significativa nas internações por doenças relacionadas à água 
        (como diarreia, hepatite A, e outras doenças de veiculação hídrica).</p>
        
        <p><strong>Impacto na saúde pública:</strong> Cada real investido em saneamento representa 
        economia nos gastos com saúde e, principalmente, melhoria na qualidade de vida da população.</p>
        
        <p><strong>Alinhamento com ODS:</strong> Este painel demonstra o progresso da cidade em relação ao 
        <strong>ODS 6 (Água potável e saneamento)</strong> e <strong>ODS 3 (Saúde e bem-estar)</strong>.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Tabela de dados
        with st.expander("📋 Ver dados completos"):
            st.dataframe(df_filtrado, use_container_width=True)
    
    else:
        st.error("⚠️ Não foi possível carregar os dados. Verifique a conexão ou dados de fallback.")

except Exception as e:
    st.error(f"❌ Erro ao processar dados: {e}")
    st.info("💡 Dica: Certifique-se de que os arquivos de dados estão na pasta 'data/'")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666;">
    <small>Fontes: SNIS (Sistema Nacional de Informações sobre Saneamento) | DataSUS</small>
</div>
""", unsafe_allow_html=True)
