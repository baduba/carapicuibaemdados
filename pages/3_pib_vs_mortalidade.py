"""
Painel 3 - Riqueza vs. Mortalidade Infantil
"""
import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from data_collectors import DataCollector

st.set_page_config(
    page_title="PIB vs. Mortalidade Infantil",
    page_icon="💰",
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
    .alert-box {
        background-color: #FFF3CD;
        padding: 1rem;
        border-radius: 5px;
        border-left: 5px solid #FFC107;
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Título
st.title("💰 Riqueza vs. Mortalidade Infantil")

# Pergunta em destaque
st.markdown("""
<div class="question-box">
    A cidade ficou mais rica mas os bebês vivem mais?
</div>
""", unsafe_allow_html=True)

# Informação importante
st.markdown("""
<div class="alert-box">
⚠️ <strong>Atenção:</strong> Este painel utiliza dados mockados para o PIB per capita. 
Para dados reais, é necessário integração com a API do IBGE/SIDRA.
</div>
""", unsafe_allow_html=True)

# Carregar dados
try:
    # Tentar carregar PIB real da API
    df_pib = DataCollector.get_pib_per_capita()
    
    # Se falhar, usar dados mockados
    if df_pib is None or df_pib.empty:
        st.warning("⚠️ Usando dados mockados para PIB per capita")
        df_pib = pd.DataFrame({
            'ano': [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
            'pib_per_capita': [22500, 23200, 24100, 25300, 26800, 25900, 27400, 29100, 30800]
        })
    
    df_mortalidade = DataCollector.get_mortalidade_infantil()
    
    if not df_pib.empty and not df_mortalidade.empty:
        # Mesclar dados
        df = pd.merge(df_pib, df_mortalidade, on='ano')
        
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
        
        # Criar gráfico de linha dupla com eixos duais
        fig = go.Figure()
        
        # Linha PIB per capita
        fig.add_trace(go.Scatter(
            x=df_filtrado['ano'],
            y=df_filtrado['pib_per_capita'],
            name='PIB per capita (R$)',
            line=dict(color='#00C4B4', width=3),
            mode='lines+markers',
            marker=dict(size=10, symbol='circle'),
            yaxis='y1',
            fill='tozeroy',
            fillcolor='rgba(0, 196, 180, 0.1)'
        ))
        
        # Linha Mortalidade Infantil
        fig.add_trace(go.Scatter(
            x=df_filtrado['ano'],
            y=df_filtrado['taxa_por_mil_nascidos'],
            name='Mortalidade Infantil (por mil nascidos)',
            line=dict(color='#5B2D8E', width=3),
            mode='lines+markers',
            marker=dict(size=10, symbol='diamond'),
            yaxis='y2'
        ))
        
        # Layout com dois eixos Y
        fig.update_layout(
            title={
                'text': 'PIB per capita vs. Taxa de Mortalidade Infantil',
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
                title='PIB per capita (R$)',
                titlefont=dict(color='#00C4B4'),
                tickfont=dict(color='#00C4B4'),
                showgrid=True,
                gridcolor='#f0f0f0',
                tickformat=',.0f'
            ),
            yaxis2=dict(
                title='Mortalidade Infantil (por 1.000 nascidos vivos)',
                titlefont=dict(color='#5B2D8E'),
                tickfont=dict(color='#5B2D8E'),
                overlaying='y',
                side='right',
                showgrid=False
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
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            variacao_pib = ((df_filtrado['pib_per_capita'].iloc[-1] - df_filtrado['pib_per_capita'].iloc[0]) / df_filtrado['pib_per_capita'].iloc[0] * 100)
            st.metric(
                "Crescimento do PIB per capita",
                f"{variacao_pib:.1f}%",
                delta=f"R$ {df_filtrado['pib_per_capita'].iloc[-1] - df_filtrado['pib_per_capita'].iloc[0]:,.0f}"
            )
        
        with col2:
            st.metric(
                "PIB per capita atual",
                f"R$ {df_filtrado['pib_per_capita'].iloc[-1]:,.0f}",
                delta=f"{anos_selecionados[1]}",
                delta_color="off"
            )
        
        with col3:
            variacao_mortalidade = ((df_filtrado['taxa_por_mil_nascidos'].iloc[-1] - df_filtrado['taxa_por_mil_nascidos'].iloc[0]) / df_filtrado['taxa_por_mil_nascidos'].iloc[0] * 100)
            st.metric(
                "Redução na Mortalidade",
                f"{abs(variacao_mortalidade):.1f}%",
                delta=f"{df_filtrado['taxa_por_mil_nascidos'].iloc[-1] - df_filtrado['taxa_por_mil_nascidos'].iloc[0]:.1f}",
                delta_color="inverse"
            )
        
        with col4:
            st.metric(
                "Mortalidade Infantil atual",
                f"{df_filtrado['taxa_por_mil_nascidos'].iloc[-1]:.1f}",
                delta="por mil nascidos",
                delta_color="off"
            )
        
        # Análise de correlação simples
        st.markdown("### 📉 Análise de Correlação")
        
        col_a, col_b = st.columns(2)
        
        with col_a:
            correlacao = df_filtrado['pib_per_capita'].corr(df_filtrado['taxa_por_mil_nascidos'])
            
            st.markdown(f"""
            <div style="background-color: #f0f2f6; padding: 1rem; border-radius: 5px;">
                <h4>Coeficiente de Correlação</h4>
                <p style="font-size: 2rem; font-weight: bold; color: #5B2D8E;">{correlacao:.3f}</p>
                <p><small>Valor entre -1 (correlação negativa perfeita) e 1 (correlação positiva perfeita)</small></p>
            </div>
            """, unsafe_allow_html=True)
        
        with col_b:
            if correlacao < -0.5:
                interpretacao = "📊 <strong>Forte correlação negativa:</strong> À medida que o PIB per capita aumenta, a mortalidade infantil diminui significativamente."
                cor_box = "#D4EDDA"
            elif correlacao < -0.3:
                interpretacao = "📊 <strong>Correlação negativa moderada:</strong> Há uma tendência de redução da mortalidade com o aumento da riqueza."
                cor_box = "#FFF3CD"
            else:
                interpretacao = "📊 <strong>Correlação fraca:</strong> A relação entre PIB e mortalidade não é muito clara nos dados disponíveis."
                cor_box = "#F8D7DA"
            
            st.markdown(f"""
            <div style="background-color: {cor_box}; padding: 1rem; border-radius: 5px; height: 100%;">
                <p>{interpretacao}</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Insights
        st.markdown("""
        <div class="insight-box">
        <h3>📊 O que os dados mostram?</h3>
        <p><strong>Desenvolvimento humano além do PIB:</strong> O crescimento econômico (medido pelo PIB per capita) 
        está associado à redução da mortalidade infantil, mas não é o único fator. Investimentos em saúde, 
        saneamento e educação materna são fundamentais.</p>
        
        <p><strong>Mortalidade Infantil como indicador:</strong> A taxa de mortalidade infantil é um dos 
        principais indicadores de desenvolvimento humano de uma região, pois reflete qualidade do sistema de 
        saúde, nutrição, saneamento básico e condições socioeconômicas.</p>
        
        <p><strong>Meta ODS:</strong> O Brasil se comprometeu a reduzir a mortalidade infantil para 
        <strong>no máximo 8,5 mortes por mil nascidos vivos até 2030</strong> (ODS 3.2).</p>
        
        <p><strong>Alinhamento com ODS:</strong> 
        <strong>ODS 3 (Saúde e bem-estar)</strong> e 
        <strong>ODS 1 (Erradicação da pobreza)</strong>.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Contexto adicional
        with st.expander("ℹ️ Entenda a Mortalidade Infantil"):
            st.markdown("""
            **O que é?**  
            A taxa de mortalidade infantil indica o número de crianças que morrem antes de completar 1 ano 
            de vida a cada mil nascidos vivos.
            
            **Por que é importante?**  
            - Reflete a qualidade dos serviços de saúde materno-infantil
            - Indica condições de saneamento básico
            - Mostra o acesso a nutrição adequada
            - É sensível a melhorias nas condições socioeconômicas
            
            **Principais causas:**  
            - Causas perinatais (relacionadas à gravidez e parto)
            - Infecções respiratórias
            - Doenças diarreicas (relacionadas ao saneamento)
            - Desnutrição
            - Malformações congênitas
            """)
        
        # Tabela de dados
        with st.expander("📋 Ver dados completos"):
            st.dataframe(df_filtrado.style.format({
                'pib_per_capita': 'R$ {:,.2f}',
                'taxa_por_mil_nascidos': '{:.1f}'
            }), use_container_width=True)
    
    else:
        st.error("⚠️ Não foi possível carregar os dados. Verifique a conexão ou dados de fallback.")

except Exception as e:
    st.error(f"❌ Erro ao processar dados: {e}")
    st.info("💡 Dica: Certifique-se de que os arquivos de dados estão na pasta 'data/'")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666;">
    <small>Fontes: IBGE/SIDRA (PIB per capita) | DataSUS (Mortalidade Infantil)</small>
</div>
""", unsafe_allow_html=True)
