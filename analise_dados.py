"""
Script para análise detalhada dos dados de mineração
Este script realiza análises estatísticas avançadas e gera relatórios
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

def carregar_e_tratar_dados():
    """Carrega e trata os dados do CSV"""
    print("🔄 Carregando dados...")
    
    # Carregar dados
    df = pd.read_csv('mineração.csv')
    print(f"✅ Dados carregados: {len(df)} registros")
    
    # Converter colunas de data
    df['Data de Produção'] = pd.to_datetime(df['Data de Produção'])
    
    # Extrair informações da data
    df['Ano'] = df['Data de Produção'].dt.year
    df['Mês'] = df['Data de Produção'].dt.month
    df['Trimestre'] = df['Data de Produção'].dt.quarter
    df['Dia da Semana'] = df['Data de Produção'].dt.day_name()
    
    # Converter colunas numéricas
    colunas_numericas = [
        'Quantidade (Toneladas)', 'Preço Unitário (R$)', 
        'Volume de Vendas (R$)', 'Custo de Produção (R$)', 
        'Lucro (R$)', 'Quantidade Exportada (Toneladas)', 
        'Custo Logístico (R$)'
    ]
    
    for coluna in colunas_numericas:
        df[coluna] = pd.to_numeric(df[coluna], errors='coerce')
    
    # Calcular métricas adicionais
    df['Margem de Lucro (%)'] = (df['Lucro (R$)'] / df['Volume de Vendas (R$)']) * 100
    df['Custo Total'] = df['Custo de Produção (R$)'] + df['Custo Logístico (R$)']
    df['ROI (%)'] = (df['Lucro (R$)'] / df['Custo Total']) * 100
    df['Preço por Tonelada'] = df['Volume de Vendas (R$)'] / df['Quantidade (Toneladas)']
    
    # Limpar dados inconsistentes
    df_original = df.copy()
    df = df.dropna()
    print(f"🧹 Dados após remoção de nulos: {len(df)} registros")
    
    # Remover outliers extremos
    registros_antes = len(df)
    for coluna in colunas_numericas:
        Q1 = df[coluna].quantile(0.25)
        Q3 = df[coluna].quantile(0.75)
        IQR = Q3 - Q1
        limite_inferior = Q1 - 1.5 * IQR
        limite_superior = Q3 + 1.5 * IQR
        df = df[(df[coluna] >= limite_inferior) & (df[coluna] <= limite_superior)]
    
    print(f"📊 Dados após remoção de outliers: {len(df)} registros")
    print(f"🗑️ Registros removidos: {registros_antes - len(df)}")
    
    return df, df_original

def analise_estatistica(df):
    """Realiza análise estatística detalhada"""
    print("\n📈 ANÁLISE ESTATÍSTICA DETALHADA")
    print("=" * 50)
    
    # Estatísticas descritivas
    colunas_analise = [
        'Quantidade (Toneladas)', 'Preço Unitário (R$)', 
        'Volume de Vendas (R$)', 'Custo de Produção (R$)', 
        'Lucro (R$)', 'Margem de Lucro (%)', 'ROI (%)'
    ]
    
    print("\n📋 Estatísticas Descritivas:")
    print(df[colunas_analise].describe())
    
    # Análise por produto
    print("\n🏭 Análise por Produto:")
    analise_produto = df.groupby('Produto').agg({
        'Volume de Vendas (R$)': ['count', 'sum', 'mean'],
        'Lucro (R$)': ['sum', 'mean'],
        'Margem de Lucro (%)': 'mean',
        'ROI (%)': 'mean'
    }).round(2)
    print(analise_produto)
    
    # Análise por região
    print("\n🗺️ Análise por Região:")
    analise_regiao = df.groupby('Região').agg({
        'Volume de Vendas (R$)': ['count', 'sum', 'mean'],
        'Lucro (R$)': ['sum', 'mean'],
        'Margem de Lucro (%)': 'mean'
    }).round(2)
    print(analise_regiao)
    
    # Análise por sustentabilidade
    print("\n🌱 Análise por Classificação de Sustentabilidade:")
    analise_sust = df.groupby('Classificação de Sustentabilidade').agg({
        'Volume de Vendas (R$)': ['count', 'sum', 'mean'],
        'Lucro (R$)': ['sum', 'mean'],
        'Margem de Lucro (%)': 'mean'
    }).round(2)
    print(analise_sust)

def analise_temporal(df):
    """Análise temporal dos dados"""
    print("\n📅 ANÁLISE TEMPORAL")
    print("=" * 50)
    
    # Análise por ano
    print("\n📊 Análise por Ano:")
    analise_ano = df.groupby('Ano').agg({
        'Volume de Vendas (R$)': 'sum',
        'Lucro (R$)': 'sum',
        'Margem de Lucro (%)': 'mean',
        'Quantidade (Toneladas)': 'sum'
    }).round(2)
    print(analise_ano)
    
    # Análise por mês
    print("\n📅 Análise por Mês:")
    analise_mes = df.groupby('Mês').agg({
        'Volume de Vendas (R$)': 'sum',
        'Lucro (R$)': 'sum',
        'Margem de Lucro (%)': 'mean'
    }).round(2)
    print(analise_mes)
    
    # Análise por trimestre
    print("\n📊 Análise por Trimestre:")
    analise_trimestre = df.groupby('Trimestre').agg({
        'Volume de Vendas (R$)': 'sum',
        'Lucro (R$)': 'sum',
        'Margem de Lucro (%)': 'mean'
    }).round(2)
    print(analise_trimestre)

def analise_correlacao(df):
    """Análise de correlação entre variáveis"""
    print("\n🔗 ANÁLISE DE CORRELAÇÃO")
    print("=" * 50)
    
    colunas_correlacao = [
        'Quantidade (Toneladas)', 'Preço Unitário (R$)', 
        'Volume de Vendas (R$)', 'Custo de Produção (R$)', 
        'Lucro (R$)', 'Custo Logístico (R$)', 'Margem de Lucro (%)'
    ]
    
    correlacao = df[colunas_correlacao].corr()
    print("\nMatriz de Correlação:")
    print(correlacao.round(3))
    
    # Correlações mais fortes
    print("\n🔍 Correlações mais fortes (|r| > 0.5):")
    for i in range(len(correlacao.columns)):
        for j in range(i+1, len(correlacao.columns)):
            valor = correlacao.iloc[i, j]
            if abs(valor) > 0.5:
                print(f"{correlacao.columns[i]} ↔ {correlacao.columns[j]}: {valor:.3f}")

def identificar_padroes(df):
    """Identifica padrões interessantes nos dados"""
    print("\n🔍 IDENTIFICAÇÃO DE PADRÕES")
    print("=" * 50)
    
    # Top 5 produtos mais lucrativos
    print("\n🏆 Top 5 Produtos por Lucro Total:")
    top_lucro = df.groupby('Produto')['Lucro (R$)'].sum().sort_values(ascending=False).head()
    print(top_lucro)
    
    # Top 5 fábricas mais produtivas
    print("\n🏭 Top 5 Fábricas por Volume de Vendas:")
    top_fabricas = df.groupby('Fábrica')['Volume de Vendas (R$)'].sum().sort_values(ascending=False).head()
    print(top_fabricas)
    
    # Análise de sazonalidade
    print("\n📅 Análise de Sazonalidade (por mês):")
    sazonalidade = df.groupby('Mês')['Volume de Vendas (R$)'].mean().sort_index()
    print(sazonalidade)
    
    # Produtos com maior margem de lucro
    print("\n💰 Produtos com Maior Margem de Lucro:")
    margem_produtos = df.groupby('Produto')['Margem de Lucro (%)'].mean().sort_values(ascending=False)
    print(margem_produtos)

def gerar_relatorio(df):
    """Gera um relatório resumido"""
    print("\n📄 RELATÓRIO RESUMIDO")
    print("=" * 50)
    
    # Métricas gerais
    total_vendas = df['Volume de Vendas (R$)'].sum()
    total_lucro = df['Lucro (R$)'].sum()
    margem_geral = (total_lucro / total_vendas) * 100
    total_toneladas = df['Quantidade (Toneladas)'].sum()
    
    print(f"\n📊 MÉTRICAS GERAIS:")
    print(f"• Total de Vendas: R$ {total_vendas:,.2f}")
    print(f"• Total de Lucro: R$ {total_lucro:,.2f}")
    print(f"• Margem de Lucro Geral: {margem_geral:.2f}%")
    print(f"• Total de Toneladas: {total_toneladas:,.0f}")
    print(f"• Número de Registros: {len(df):,}")
    
    # Produto mais vendido
    produto_mais_vendido = df.groupby('Produto')['Volume de Vendas (R$)'].sum().idxmax()
    vendas_produto = df.groupby('Produto')['Volume de Vendas (R$)'].sum().max()
    print(f"\n🏆 PRODUTO MAIS VENDIDO:")
    print(f"• {produto_mais_vendido}: R$ {vendas_produto:,.2f}")
    
    # Região mais lucrativa
    regiao_mais_lucrativa = df.groupby('Região')['Lucro (R$)'].sum().idxmax()
    lucro_regiao = df.groupby('Região')['Lucro (R$)'].sum().max()
    print(f"\n🗺️ REGIÃO MAIS LUCRATIVA:")
    print(f"• {regiao_mais_lucrativa}: R$ {lucro_regiao:,.2f}")
    
    # Período de maior atividade
    periodo_mais_ativo = df.groupby('Ano')['Volume de Vendas (R$)'].sum().idxmax()
    vendas_periodo = df.groupby('Ano')['Volume de Vendas (R$)'].sum().max()
    print(f"\n📅 PERÍODO DE MAIOR ATIVIDADE:")
    print(f"• {periodo_mais_ativo}: R$ {vendas_periodo:,.2f}")

def salvar_dados_tratados(df):
    """Salva os dados tratados em diferentes formatos"""
    print("\n💾 SALVANDO DADOS TRATADOS")
    print("=" * 50)
    
    # Salvar CSV tratado
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    nome_arquivo = f"dados_mineracao_tratados_{timestamp}.csv"
    df.to_csv(nome_arquivo, index=False, encoding='utf-8-sig')
    print(f"✅ CSV salvo: {nome_arquivo}")
    
    # Salvar Excel com múltiplas abas
    nome_excel = f"relatorio_mineracao_{timestamp}.xlsx"
    with pd.ExcelWriter(nome_excel, engine='openpyxl') as writer:
        # Dados completos
        df.to_excel(writer, sheet_name='Dados_Completos', index=False)
        
        # Resumo por produto
        resumo_produto = df.groupby('Produto').agg({
            'Volume de Vendas (R$)': ['count', 'sum', 'mean'],
            'Lucro (R$)': ['sum', 'mean'],
            'Margem de Lucro (%)': 'mean'
        }).round(2)
        resumo_produto.to_excel(writer, sheet_name='Resumo_Produto')
        
        # Resumo por região
        resumo_regiao = df.groupby('Região').agg({
            'Volume de Vendas (R$)': ['count', 'sum', 'mean'],
            'Lucro (R$)': ['sum', 'mean'],
            'Margem de Lucro (%)': 'mean'
        }).round(2)
        resumo_regiao.to_excel(writer, sheet_name='Resumo_Regiao')
        
        # Resumo temporal
        resumo_temporal = df.groupby('Ano').agg({
            'Volume de Vendas (R$)': 'sum',
            'Lucro (R$)': 'sum',
            'Margem de Lucro (%)': 'mean'
        }).round(2)
        resumo_temporal.to_excel(writer, sheet_name='Resumo_Temporal')
    
    print(f"✅ Excel salvo: {nome_excel}")

def main():
    """Função principal"""
    print("🚀 INICIANDO ANÁLISE DE DADOS DE MINERAÇÃO")
    print("=" * 60)
    
    # Carregar dados
    df, df_original = carregar_e_tratar_dados()
    
    if df is not None and len(df) > 0:
        # Realizar análises
        analise_estatistica(df)
        analise_temporal(df)
        analise_correlacao(df)
        identificar_padroes(df)
        gerar_relatorio(df)
        salvar_dados_tratados(df)
        
        print("\n🎉 ANÁLISE CONCLUÍDA COM SUCESSO!")
        print("=" * 60)
        print("📁 Arquivos gerados:")
        print("   • dados_mineracao_tratados_[timestamp].csv")
        print("   • relatorio_mineracao_[timestamp].xlsx")
        print("\n📊 Para visualização interativa, execute: streamlit run app.py")
        
    else:
        print("❌ Erro: Não foi possível carregar ou processar os dados")

if __name__ == "__main__":
    main() 