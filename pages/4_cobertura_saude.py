"""
Painel 4 - Cobertura de Saúde (UBS vs. Densidade Populacional)
"""
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from data_collectors import DataCollector

st.set_page_config(
    page_title="Cobertura de Saúde",
    page_icon="🏥",
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
st.title("🏥 Cobertura de Saúde")

# Pergunta em destaque
st.markdown("""
<div class="question-box">
    Tem unidade de saúde onde tem gente?
</div>
""", unsafe_allow_html=True)

# Carregar dados
try:
    df_ubs = DataCollector.get_ubs_data()
    
    if not df_ubs.empty:
        # Calcular métricas
        df_ubs['pessoas_por_ubs'] = (df_ubs['populacao'] / df_ubs['ubs']).round(0)
        df_ubs['ubs_por_10mil_hab'] = (df_ubs['ubs'] / df_ubs['populacao'] * 10000).round(2)
        
        # Filtros na sidebar
        st.sidebar.markdown("### 🎚️ Filtros")
        
        regioes_selecionadas = st.sidebar.multiselect(
            "Regiões para análise",
            options=df_ubs['regiao'].tolist(),
            default=df_ubs['regiao'].tolist()
        )
        
        ordenar_por = st.sidebar.selectbox(
            "Ordenar por",
            ["População (maior)", "População (menor)", "Número de UBS (maior)", "Densidade (maior)", "Pessoas por UBS (maior)"]
        )
        
        # Filtrar dados
        df_filtrado = df_ubs[df_ubs['regiao'].isin(regioes_selecionadas)].copy()
        
        # Ordenar
        if ordenar_por == "População (maior)":
            df_filtrado = df_filtrado.sort_values('populacao', ascending=False)
        elif ordenar_por == "População (menor)":
            df_filtrado = df_filtrado.sort_values('populacao', ascending=True)
        elif ordenar_por == "Número de UBS (maior)":
            df_filtrado = df_filtrado.sort_values('ubs', ascending=False)
        elif ordenar_por == "Densidade (maior)":
            df_filtrado = df_filtrado.sort_values('densidade_hab_km2', ascending=False)
        else:  # Pessoas por UBS
            df_filtrado = df_filtrado.sort_values('pessoas_por_ubs', ascending=False)
        
        # Gráfico 1: Barras comparativas - UBS vs População
        st.markdown("### 📊 Distribuição de UBS por Região")
        
        fig1 = go.Figure()
        
        # Barras de população (escala secundária)
        fig1.add_trace(go.Bar(
            x=df_filtrado['regiao'],
            y=df_filtrado['populacao'],
            name='População',
            marker_color='#5B2D8E',
            yaxis='y2',
            opacity=0.6
        ))
        
        # Barras de UBS
        fig1.add_trace(go.Bar(
            x=df_filtrado['regiao'],
            y=df_filtrado['ubs'],
            name='Número de UBS',
            marker_color='#00C4B4',
            text=df_filtrado['ubs'],
            textposition='auto',
            yaxis='y1'
        ))
        
        fig1.update_layout(
            title='Número de UBS vs. População por Região',
            xaxis=dict(title='Região', tickangle=-45),
            yaxis=dict(
                title='Número de UBS',
                titlefont=dict(color='#00C4B4'),
                tickfont=dict(color='#00C4B4')
            ),
            yaxis2=dict(
                title='População',
                titlefont=dict(color='#5B2D8E'),
                tickfont=dict(color='#5B2D8E'),
                overlaying='y',
                side='right'
            ),
            hovermode='x unified',
            height=450,
            plot_bgcolor='white',
            showlegend=True
        )
        
        st.plotly_chart(fig1, use_container_width=True)
        
        # Gráfico 2: Scatter - Densidade vs Cobertura
        st.markdown("### 🎯 Densidade Populacional vs. Cobertura de UBS")
        
        fig2 = px.scatter(
            df_filtrado,
            x='densidade_hab_km2',
            y='ubs_por_10mil_hab',
            size='populacao',
            color='pessoas_por_ubs',
            hover_name='regiao',
            hover_data={
                'densidade_hab_km2': ':.0f',
                'ubs_por_10mil_hab': ':.2f',
                'populacao': ':,',
                'pessoas_por_ubs': ':.0f',
                'ubs': True
            },
            labels={
                'densidade_hab_km2': 'Densidade (hab/km²)',
                'ubs_por_10mil_hab': 'UBS por 10 mil habitantes',
                'pessoas_por_ubs': 'Pessoas por UBS',
                'populacao': 'População'
            },
            color_continuous_scale='RdYlGn_r',
            title='Relação entre Densidade Populacional e Cobertura de UBS'
        )
        
        fig2.update_layout(
            height=450,
            plot_bgcolor='white',
            showlegend=True
        )
        
        # Linha de referência (média nacional aproximada: 1 UBS por 10 mil hab)
        fig2.add_hline(y=1.0, line_dash="dash", line_color="gray", 
                       annotation_text="Referência aproximada (1 UBS/10mil hab)")
        
        st.plotly_chart(fig2, use_container_width=True)
        
        # Métricas gerais
        st.markdown("### 📈 Indicadores Gerais")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            total_ubs = df_filtrado['ubs'].sum()
            st.metric(
                "Total de UBS",
                total_ubs,
                delta=f"{len(df_filtrado)} regiões"
            )
        
        with col2:
            pop_total = df_filtrado['populacao'].sum()
            st.metric(
                "População Total",
                f"{pop_total:,}",
                delta="habitantes"
            )
        
        with col3:
            media_pessoas_ubs = df_filtrado['pessoas_por_ubs'].mean()
            st.metric(
                "Média de Pessoas por UBS",
                f"{media_pessoas_ubs:,.0f}",
                delta="hab/UBS"
            )
        
        with col4:
            cobertura_media = df_filtrado['ubs_por_10mil_hab'].mean()
            st.metric(
                "Cobertura Média",
                f"{cobertura_media:.2f}",
                delta="UBS/10mil hab"
            )
        
        # Tabela detalhada
        st.markdown("### 📋 Dados Detalhados por Região")
        
        # Criar uma cópia formatada para exibição
        df_display = df_filtrado[['regiao', 'ubs', 'populacao', 'densidade_hab_km2', 'pessoas_por_ubs', 'ubs_por_10mil_hab']].copy()
        df_display.columns = ['Região', 'UBS', 'População', 'Densidade (hab/km²)', 'Pessoas por UBS', 'UBS por 10mil hab']
        
        # Destacar regiões com cobertura abaixo/acima da média
        def highlight_cobertura(row):
            if row['UBS por 10mil hab'] < cobertura_media * 0.8:
                return ['background-color: #FFE5E5'] * len(row)  # Vermelho claro - cobertura baixa
            elif row['UBS por 10mil hab'] > cobertura_media * 1.2:
                return ['background-color: #E5FFE5'] * len(row)  # Verde claro - cobertura alta
            else:
                return [''] * len(row)
        
        st.dataframe(
            df_display.style.apply(highlight_cobertura, axis=1).format({
                'População': '{:,}',
                'Densidade (hab/km²)': '{:,.0f}',
                'Pessoas por UBS': '{:,.0f}',
                'UBS por 10mil hab': '{:.2f}'
            }),
            use_container_width=True,
            height=400
        )
        
        st.caption("🟢 Verde: cobertura acima da média | 🔴 Vermelho: cobertura abaixo da média")
        
        # Identificar regiões críticas
        st.markdown("### ⚠️ Regiões que Precisam de Atenção")
        
        # Regiões com maior população por UBS (pior cobertura)
        regioes_criticas = df_filtrado.nlargest(3, 'pessoas_por_ubs')
        
        col_a, col_b = st.columns(2)
        
        with col_a:
            st.markdown("**🔴 Menor cobertura (mais pessoas por UBS):**")
            for _, row in regioes_criticas.iterrows():
                st.markdown(f"- **{row['regiao']}**: {row['pessoas_por_ubs']:,.0f} pessoas/UBS ({row['ubs']} UBS para {row['populacao']:,} habitantes)")
        
        # Regiões com melhor cobertura
        regioes_boas = df_filtrado.nsmallest(3, 'pessoas_por_ubs')
        
        with col_b:
            st.markdown("**🟢 Melhor cobertura (menos pessoas por UBS):**")
            for _, row in regioes_boas.iterrows():
                st.markdown(f"- **{row['regiao']}**: {row['pessoas_por_ubs']:,.0f} pessoas/UBS ({row['ubs']} UBS para {row['populacao']:,} habitantes)")
        
        # Insights
        st.markdown("""
        <div class="insight-box">
        <h3>📊 O que os dados mostram?</h3>
        
        <p><strong>Distribuição desigual:</strong> Há variação significativa na cobertura de UBS entre as 
        diferentes regiões de Carapicuíba. Regiões mais densamente povoadas nem sempre têm proporcionalmente 
        mais unidades de saúde.</p>
        
        <p><strong>Parâmetro do Ministério da Saúde:</strong> O MS recomenda 1 UBS para cada 2.000 a 3.500 pessoas 
        (ESF - Estratégia Saúde da Família). Regiões com mais de 3.500 pessoas por UBS podem estar com cobertura insuficiente.</p>
        
        <p><strong>Densidade vs. Acesso:</strong> Alta densidade populacional deve ser acompanhada de maior número 
        de UBS para garantir acesso adequado aos serviços básicos de saúde.</p>
        
        <p><strong>Priorização de investimentos:</strong> Os dados permitem identificar quais regiões necessitam 
        com mais urgência de novas unidades de saúde.</p>
        
        <p><strong>Alinhamento com ODS:</strong> 
        <strong>ODS 3 (Saúde e bem-estar)</strong> - Meta 3.8: Cobertura universal de saúde e 
        <strong>ODS 11 (Cidades e comunidades sustentáveis)</strong> - Acesso a serviços básicos.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Informações adicionais
        with st.expander("ℹ️ Sobre as Unidades Básicas de Saúde (UBS)"):
            st.markdown("""
            **O que é uma UBS?**  
            As Unidades Básicas de Saúde são a porta de entrada do SUS. Oferecem atendimento em:
            - Consultas médicas
            - Vacinação
            - Pré-natal
            - Prevenção de doenças
            - Pequenos procedimentos
            - Dispensação de medicamentos básicos
            
            **Importância da proximidade:**  
            UBS devem estar próximas da população para garantir:
            - Acesso facilitado a serviços preventivos
            - Redução de custos com transporte
            - Maior adesão a tratamentos contínuos
            - Diagnóstico precoce de doenças
            
            **Estratégia Saúde da Família:**  
            Cada equipe de ESF deve cobrir entre 2.000 e 3.500 pessoas, visitando residências e 
            conhecendo a realidade de cada família.
            """)
    
    else:
        st.error("⚠️ Não foi possível carregar os dados. Verifique os dados de fallback.")

except Exception as e:
    st.error(f"❌ Erro ao processar dados: {e}")
    st.info("💡 Dica: Certifique-se de que o arquivo 'ubs_regiao.csv' está na pasta 'data/'")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666;">
    <small>Fontes: CNES/DataSUS (Cadastro Nacional de Estabelecimentos de Saúde) | IBGE (Dados demográficos)</small>
</div>
""", unsafe_allow_html=True)
