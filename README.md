# 📊 Dashboard de Análise de Dados de Mineração

Este projeto oferece uma análise completa e visualização interativa dos dados de mineração, incluindo tratamento de dados, análises estatísticas e dashboard interativo.

## 🚀 Funcionalidades

### Dashboard Interativo (Streamlit)
- **Visualizações dinâmicas** com gráficos interativos
- **Filtros avançados** por produto, região, ano e sustentabilidade
- **Métricas em tempo real** com comparações
- **Análise de correlação** entre variáveis
- **Download de dados tratados**

### Análise Estatística Detalhada
- **Tratamento de dados** automático
- **Remoção de outliers** usando método IQR
- **Análise temporal** (ano, mês, trimestre)
- **Análise por categorias** (produto, região, sustentabilidade)
- **Identificação de padrões** e tendências
- **Geração de relatórios** em Excel

## 📋 Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

## 🛠️ Instalação

1. **Clone ou baixe o projeto**
2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

## 🎯 Como Usar

### Dashboard Interativo
```bash
streamlit run app.py
```
O dashboard será aberto automaticamente no seu navegador.

### Análise Estatística Detalhada
```bash
python analise_dados.py
```
Este comando irá:
- Carregar e tratar os dados
- Realizar análises estatísticas
- Gerar relatórios em CSV e Excel
- Exibir resultados no terminal

## 📊 Estrutura dos Dados

O arquivo `mineração.csv` contém as seguintes colunas:

| Coluna | Descrição | Tipo |
|--------|-----------|------|
| ID | Identificador único | Inteiro |
| Produto | Tipo de produto mineral | Texto |
| Quantidade (Toneladas) | Quantidade produzida | Numérico |
| Preço Unitário (R$) | Preço por unidade | Monetário |
| Fábrica | Local de produção | Texto |
| Data de Produção | Data da produção | Data/Hora |
| Embalagem | Tipo de embalagem | Texto |
| Classificação de Sustentabilidade | Nível A, B, C ou D | Texto |
| Volume de Vendas (R$) | Valor total vendido | Monetário |
| Custo de Produção (R$) | Custo de fabricação | Monetário |
| Lucro (R$) | Lucro obtido | Monetário |
| Região | Região geográfica | Texto |
| Quantidade Exportada (Toneladas) | Quantidade exportada | Numérico |
| Custo Logístico (R$) | Custo de transporte | Monetário |

## 🔧 Tratamento de Dados

### Etapas Automáticas:
1. **Conversão de tipos de dados**
   - Datas convertidas para datetime
   - Valores monetários convertidos para float
   
2. **Criação de variáveis derivadas**
   - Ano, Mês, Trimestre extraídos da data
   - Margem de Lucro (%) calculada
   - Custo Total (Produção + Logística)
   - ROI (%) calculado
   
3. **Limpeza de dados**
   - Remoção de valores nulos
   - Remoção de outliers extremos (método IQR)
   
4. **Análises realizadas**
   - Estatísticas descritivas
   - Análise de correlação
   - Análise temporal
   - Análise por categorias

## 📈 Visualizações Disponíveis

### Dashboard:
- **Gráficos de barras** - Volume de vendas por produto
- **Gráficos de pizza** - Distribuição do lucro por região
- **Gráficos de linha** - Evolução temporal de vendas e lucros
- **Matriz de correlação** - Relações entre variáveis numéricas
- **Gráficos de sustentabilidade** - Análise por classificação

### Relatórios:
- **Estatísticas descritivas** completas
- **Análises por categoria** detalhadas
- **Tendências temporais** identificadas
- **Padrões e insights** descobertos

## 📁 Arquivos do Projeto

```
app-de previsão/
├── app.py                 # Dashboard Streamlit principal
├── analise_dados.py       # Script de análise estatística
├── mineração.csv          # Dados originais
├── requirements.txt       # Dependências do projeto
└── README.md             # Este arquivo
```

## 🎨 Personalização

### Adicionar Novos Filtros:
Edite o arquivo `app.py` na seção de filtros da sidebar.

### Modificar Visualizações:
As visualizações usam Plotly Express e podem ser facilmente customizadas.

### Adicionar Novas Análises:
Edite o arquivo `analise_dados.py` para incluir novas análises estatísticas.

## 📊 Exemplos de Insights

Com base na análise dos dados, você pode descobrir:

- **Produtos mais lucrativos** por região
- **Tendências sazonais** na produção
- **Correlações** entre custos e lucros
- **Impacto da sustentabilidade** na rentabilidade
- **Padrões temporais** de vendas

## 🤝 Contribuição

Para contribuir com o projeto:

1. Faça um fork do repositório
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 📞 Suporte

Para dúvidas ou problemas:
- Abra uma issue no repositório
- Entre em contato através do email do projeto

---

**Desenvolvido com ❤️ para análise de dados de mineração** 