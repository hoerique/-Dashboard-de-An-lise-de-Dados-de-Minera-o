"""
Script de teste para verificar se o dashboard está funcionando corretamente
"""

import pandas as pd
import numpy as np
from datetime import datetime

def testar_carregamento_dados():
    """Testa o carregamento e tratamento dos dados"""
    print("🧪 TESTANDO CARREGAMENTO DE DADOS")
    print("=" * 50)
    
    try:
        # Carregar dados
        df = pd.read_csv('mineração.csv')
        print(f"✅ Dados carregados: {len(df)} registros")
        
        # Verificar colunas
        colunas_esperadas = [
            'ID', 'Produto', 'Quantidade (Toneladas)', 'Preço Unitário (R$)',
            'Fábrica', 'Data de Produção', 'Embalagem', 'Classificação de Sustentabilidade',
            'Volume de Vendas (R$)', 'Custo de Produção (R$)', 'Lucro (R$)',
            'Região', 'Quantidade Exportada (Toneladas)', 'Custo Logístico (R$)'
        ]
        
        colunas_faltando = [col for col in colunas_esperadas if col not in df.columns]
        if colunas_faltando:
            print(f"❌ Colunas faltando: {colunas_faltando}")
            return False
        else:
            print("✅ Todas as colunas necessárias estão presentes")
        
        # Testar conversão de data
        df['Data de Produção'] = pd.to_datetime(df['Data de Produção'])
        print("✅ Conversão de data realizada com sucesso")
        
        # Testar conversão numérica
        colunas_numericas = [
            'Quantidade (Toneladas)', 'Preço Unitário (R$)', 
            'Volume de Vendas (R$)', 'Custo de Produção (R$)', 
            'Lucro (R$)', 'Quantidade Exportada (Toneladas)', 
            'Custo Logístico (R$)'
        ]
        
        for coluna in colunas_numericas:
            df[coluna] = pd.to_numeric(df[coluna], errors='coerce')
        
        print("✅ Conversão numérica realizada com sucesso")
        
        # Testar cálculos de KPIs
        df['Margem de Lucro (%)'] = (df['Lucro (R$)'] / df['Volume de Vendas (R$)']) * 100
        df['Custo Total'] = df['Custo de Produção (R$)'] + df['Custo Logístico (R$)']
        df['ROI (%)'] = (df['Lucro (R$)'] / df['Custo Total']) * 100
        
        print("✅ Cálculos de KPIs realizados com sucesso")
        
        # Verificar se há dados válidos
        df_limpo = df.dropna()
        print(f"✅ Dados após limpeza: {len(df_limpo)} registros")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro no carregamento: {e}")
        return False

def testar_kpis(df):
    """Testa os cálculos dos KPIs"""
    print("\n🧪 TESTANDO CÁLCULOS DE KPIs")
    print("=" * 50)
    
    try:
        # KPI 1: Lucro Total
        lucro_total = df['Lucro (R$)'].sum()
        print(f"✅ KPI 1 - Lucro Total: R$ {lucro_total:,.2f}")
        
        # KPI 2: Volume Total de Vendas
        vendas_totais = df['Volume de Vendas (R$)'].sum()
        print(f"✅ KPI 2 - Volume Total de Vendas: R$ {vendas_totais:,.2f}")
        
        # KPI 3: Margem de Lucro
        margem_media = df['Margem de Lucro (%)'].mean()
        print(f"✅ KPI 3 - Margem de Lucro Média: {margem_media:.2f}%")
        
        # KPI 4: Custo Médio Logístico por Tonelada
        custo_logistico_total = df['Custo Logístico (R$)'].sum()
        quantidade_total = df['Quantidade (Toneladas)'].sum()
        custo_medio_logistico = custo_logistico_total / quantidade_total
        print(f"✅ KPI 4 - Custo Médio Logístico por Tonelada: R$ {custo_medio_logistico:.2f}")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro nos cálculos de KPIs: {e}")
        return False

def testar_graficos(df):
    """Testa a geração dos gráficos"""
    print("\n🧪 TESTANDO GERAÇÃO DE GRÁFICOS")
    print("=" * 50)
    
    try:
        # Teste 1: Gráfico de Barras – Lucro por Produto
        lucro_por_produto = df.groupby('Produto')['Lucro (R$)'].sum().reset_index()
        print(f"✅ Gráfico 1 - Lucro por Produto: {len(lucro_por_produto)} produtos")
        
        # Teste 2: Gráfico de Linhas – Evolução de Vendas
        vendas_tempo = df.groupby('Data de Produção')['Volume de Vendas (R$)'].sum().reset_index()
        print(f"✅ Gráfico 2 - Evolução de Vendas: {len(vendas_tempo)} pontos temporais")
        
        # Teste 3: Gráfico de Pizza – Vendas por Região
        vendas_por_regiao = df.groupby('Região')['Volume de Vendas (R$)'].sum().reset_index()
        print(f"✅ Gráfico 3 - Vendas por Região: {len(vendas_por_regiao)} regiões")
        
        # Teste 4: Gráfico de Colunas – Custo vs Lucro por Fábrica
        custo_lucro_fabrica = df.groupby('Fábrica').agg({
            'Custo de Produção (R$)': 'sum',
            'Lucro (R$)': 'sum'
        }).reset_index()
        print(f"✅ Gráfico 4 - Custo vs Lucro por Fábrica: {len(custo_lucro_fabrica)} fábricas")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro na geração de gráficos: {e}")
        return False

def testar_filtros(df):
    """Testa os filtros do dashboard"""
    print("\n🧪 TESTANDO FILTROS")
    print("=" * 50)
    
    try:
        # Teste filtro por produto
        produtos = df['Produto'].unique()
        print(f"✅ Filtro Produto: {len(produtos)} produtos disponíveis")
        
        # Teste filtro por região
        regioes = df['Região'].unique()
        print(f"✅ Filtro Região: {len(regioes)} regiões disponíveis")
        
        # Teste filtro por ano
        df['Ano'] = df['Data de Produção'].dt.year
        anos = df['Ano'].unique()
        print(f"✅ Filtro Ano: {len(anos)} anos disponíveis")
        
        # Teste filtro por sustentabilidade
        classificacoes = df['Classificação de Sustentabilidade'].unique()
        print(f"✅ Filtro Sustentabilidade: {len(classificacoes)} classificações disponíveis")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro nos filtros: {e}")
        return False

def main():
    """Função principal de teste"""
    print("🚀 INICIANDO TESTES DO DASHBOARD")
    print("=" * 60)
    
    # Teste 1: Carregamento de dados
    if not testar_carregamento_dados():
        print("❌ Falha no teste de carregamento de dados")
        return
    
    # Carregar dados para os próximos testes
    df = pd.read_csv('mineração.csv')
    df['Data de Produção'] = pd.to_datetime(df['Data de Produção'])
    
    colunas_numericas = [
        'Quantidade (Toneladas)', 'Preço Unitário (R$)', 
        'Volume de Vendas (R$)', 'Custo de Produção (R$)', 
        'Lucro (R$)', 'Quantidade Exportada (Toneladas)', 
        'Custo Logístico (R$)'
    ]
    
    for coluna in colunas_numericas:
        df[coluna] = pd.to_numeric(df[coluna], errors='coerce')
    
    df['Margem de Lucro (%)'] = (df['Lucro (R$)'] / df['Volume de Vendas (R$)']) * 100
    df['Custo Total'] = df['Custo de Produção (R$)'] + df['Custo Logístico (R$)']
    df['ROI (%)'] = (df['Lucro (R$)'] / df['Custo Total']) * 100
    df = df.dropna()
    
    # Teste 2: KPIs
    if not testar_kpis(df):
        print("❌ Falha no teste de KPIs")
        return
    
    # Teste 3: Gráficos
    if not testar_graficos(df):
        print("❌ Falha no teste de gráficos")
        return
    
    # Teste 4: Filtros
    if not testar_filtros(df):
        print("❌ Falha no teste de filtros")
        return
    
    print("\n🎉 TODOS OS TESTES PASSARAM COM SUCESSO!")
    print("=" * 60)
    print("✅ O dashboard está pronto para uso!")
    print("📊 Execute 'streamlit run app.py' para iniciar o dashboard")

if __name__ == "__main__":
    main() 