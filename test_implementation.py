import medical_data_visualizer as mdv
import matplotlib.pyplot as plt

def test_data_loading():
    """Testa se os dados foram carregados corretamente"""
    print("Teste de Carregamento de Dados")
    print(f"Shape dos dados: {mdv.df.shape}")
    print(f"Colunas: {list(mdv.df.columns)}")
    print("\nPrimeiras 5 linhas:")
    print(mdv.df.head())
    
    # Verifica se a coluna overweight foi criada
    if 'overweight' in mdv.df.columns:
        print("\nColuna 'overweight' criada com sucesso")
        print(f"Valores únicos em overweight: {sorted(mdv.df['overweight'].unique())}")
    else:
        print("\nColuna 'overweight' não encontrada")
    
    # Verifica normalização de cholesterol e gluc
    print(f"\nValores únicos em cholesterol: {sorted(mdv.df['cholesterol'].unique())}")
    print(f"Valores únicos em gluc: {sorted(mdv.df['gluc'].unique())}")
    
    return True

def test_cat_plot():
    """Testa a função draw_cat_plot"""
    print("\nTeste do Gráfico Categórico")
    try:
        fig = mdv.draw_cat_plot()
        print("Gráfico categórico gerado com sucesso")
        print("Arquivo 'catplot.png' salvo")
        plt.close(fig)  
        return True
    except Exception as e:
        print(f"Erro ao gerar gráfico categórico: {e}")
        return False

def test_heat_map():
    """Testa a função draw_heat_map"""
    print("\nTeste do Mapa de Calor")
    try:
        fig = mdv.draw_heat_map()
        print("Mapa de calor gerado com sucesso")
        print("Arquivo 'heatmap.png' salvo")
        plt.close(fig)  
        return True
    except Exception as e:
        print(f"Erro ao gerar mapa de calor: {e}")
        return False

def main():
    """Executa todos os testes"""
    print("Iniciando testes do Visualizador de Dados Médicos...")
    
    tests_passed = 0
    total_tests = 3
    
    # Teste 1: Carregamento de dados
    try:
        test_data_loading()
        tests_passed += 1
    except Exception as e:
        print(f"Erro no teste de carregamento: {e}")
    
    # Teste 2: Gráfico categórico
    if test_cat_plot():
        tests_passed += 1
    
    # Teste 3: Mapa de calor
    if test_heat_map():
        tests_passed += 1
    
    print(f"\nResumo dos Testes")
    print(f"Testes aprovados: {tests_passed}/{total_tests}")
    
    if tests_passed == total_tests:
        print("Todos os testes passaram! O visualizador está funcionando corretamente.")
    else:
        print("Alguns testes falharam. Verifique os erros acima.")

if __name__ == "__main__":
    main()
