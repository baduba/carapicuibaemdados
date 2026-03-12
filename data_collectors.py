"""
Módulo para coleta de dados de APIs públicas
"""
import requests
import pandas as pd
from typing import Optional
import os

CODIGO_IBGE_CARAPICUIBA = "3510609"

class DataCollector:
    """Classe para coletar dados de APIs públicas"""
    
    @staticmethod
    def get_pib_per_capita() -> Optional[pd.DataFrame]:
        """Coleta PIB per capita de Carapicuíba do IBGE"""
        try:
            url = f"https://servicodados.ibge.gov.br/api/v3/agregados/5938/periodos/2010|2011|2012|2013|2014|2015|2016|2017|2018|2019|2020|2021/variaveis/37?localidades=N6[{CODIGO_IBGE_CARAPICUIBA}]"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            # Processar dados do IBGE
            years = []
            values = []
            
            if data and len(data) > 0:
                resultados = data[0].get('resultados', [])
                if resultados:
                    series = resultados[0].get('series', [])
                    if series:
                        serie_data = series[0].get('serie', {})
                        for year, value in serie_data.items():
                            if value and value != '...':
                                years.append(int(year))
                                values.append(float(value))
            
            if years and values:
                return pd.DataFrame({'ano': years, 'pib_per_capita': values})
            return None
            
        except Exception as e:
            print(f"Erro ao coletar PIB per capita: {e}")
            return None
    
    @staticmethod
    def get_populacao() -> Optional[pd.DataFrame]:
        """Coleta população de Carapicuíba do IBGE"""
        try:
            url = f"https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2010|2011|2012|2013|2014|2015|2016|2017|2018|2019|2020|2021|2022/variaveis/9324?localidades=N6[{CODIGO_IBGE_CARAPICUIBA}]"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            years = []
            values = []
            
            if data and len(data) > 0:
                resultados = data[0].get('resultados', [])
                if resultados:
                    series = resultados[0].get('series', [])
                    if series:
                        serie_data = series[0].get('serie', {})
                        for year, value in serie_data.items():
                            if value and value != '...':
                                years.append(int(year))
                                values.append(int(float(value)))
            
            if years and values:
                return pd.DataFrame({'ano': years, 'populacao': values})
            return None
            
        except Exception as e:
            print(f"Erro ao coletar população: {e}")
            return None
    
    @staticmethod
    def load_fallback_data(filename: str) -> pd.DataFrame:
        """Carrega dados de fallback de arquivo CSV"""
        try:
            filepath = os.path.join('data', filename)
            if os.path.exists(filepath):
                return pd.read_csv(filepath)
            else:
                print(f"Arquivo de fallback não encontrado: {filepath}")
                return pd.DataFrame()
        except Exception as e:
            print(f"Erro ao carregar dados de fallback: {e}")
            return pd.DataFrame()
    
    @staticmethod
    def get_saneamento_data() -> pd.DataFrame:
        """
        Obtém dados de saneamento (investimento)
        Por enquanto usa dados mockados, estrutura pronta para API real
        """
        # Tentar carregar de API real ou fallback
        return DataCollector.load_fallback_data('saneamento.csv')
    
    @staticmethod
    def get_saude_data() -> pd.DataFrame:
        """
        Obtém dados de saúde (internações por doenças hídricas)
        Por enquanto usa dados mockados, estrutura pronta para API real
        """
        return DataCollector.load_fallback_data('saude_internacoes.csv')
    
    @staticmethod
    def get_educacao_gastos() -> pd.DataFrame:
        """
        Obtém dados de gastos com educação
        Por enquanto usa dados mockados, estrutura pronta para Portal Transparência
        """
        return DataCollector.load_fallback_data('educacao_gastos.csv')
    
    @staticmethod
    def get_ideb_data() -> pd.DataFrame:
        """
        Obtém dados do IDEB
        Por enquanto usa dados mockados, estrutura pronta para API INEP
        """
        return DataCollector.load_fallback_data('ideb.csv')
    
    @staticmethod
    def get_mortalidade_infantil() -> pd.DataFrame:
        """
        Obtém dados de mortalidade infantil
        Por enquanto usa dados mockados, estrutura pronta para DataSUS
        """
        return DataCollector.load_fallback_data('mortalidade_infantil.csv')
    
    @staticmethod
    def get_ubs_data() -> pd.DataFrame:
        """
        Obtém dados de UBS por região
        Por enquanto usa dados mockados, estrutura pronta para CNES/DataSUS
        """
        return DataCollector.load_fallback_data('ubs_regiao.csv')
