import os
import csv
from PyPDF2 import PdfReader

ATIVOS_DIR = "./ativos"
RESULT_DIR = './CSVs' 

def convert_pdfs():
    if not os.path.exists(RESULT_DIR):
        os.makedirs(RESULT_DIR)
    
    if not os.path.exists(ATIVOS_DIR):
        print("ERRO: Por favor, provenha uma pasta com o nome 'ativos', contendo os PDFs a serem convertidos.")

    pdf_list = os.listdir(ATIVOS_DIR)
    break_words = {
        'datetime_atualizacao': 'Atualizado em',
        'dados_companhia': 'Dados da Companhia',
        'nome_pregao': 'Nome de Pregão:',
        'cod_negociacao': 'Códigos de Negociação:',
        'cnpj': 'CNPJ:',
        'atv_principal': 'Atividade Principal:',
        'class_setorial': 'Classi\x00cação Setorial:',
        'site': 'Site:',
        'contato': 'Contatos',
        'plantao_noticias': 'Plantão de Notícias delay de 15 min.',
        'mais_noticias': 'MAIS NOTÍCIAS',
        'dados_economicos': 'Dados Econômico-Financeiros - R$ - mil',
        'ver_dados': 'Ver dados no formato',
        'balanco_patrimonial': 'Balanço Patrimonial - Consolidado',
        'ativo_imobilizado': 'Ativo Imobilizado, Investimentos e Intangível',
        'ativo_total': 'Ativo Total',
        'patrimonio_liquido': 'Patrimônio Líquido',
        'patrimonio_liquido_controladora': 'Patrimônio Líquido Atribuído à Controladora',
        'demonstracao_resultado': 'Demonstração do Resultado - Consolidado',
        'receita_de_venda': 'Receita de Venda',
        'resultado_bruto': 'Resultado Bruto',
        'resultado_de_equivalencia': 'Resultado de Equivalência Patrimonial',
        'resultado_financeiro': 'Resultado Financeiro',
        'resultado_liquido_continuado': 'Resultado Líquido das Operações Continuadas',
        'lucro_prejuizo': 'Lucro (Prejuízo) do Período',
        'lucro_prejuizo_controladora': 'Lucro (Prejuízo) do Período Atribuído à Controladora',
        'demonstracao_fluxo_de_caixa': 'Demonstração do Fluxo de Caixa - Consolidado',
        'atividades_operacionais': 'Atividades Operacionais',
        'atividades_de_investimento': 'Atividades de Investimento',
        'atividade_de_financiamento': 'Atividades de Financiamento',
        'avariacao_cambial': 'Variação Cambial sobre Caixa e Equivalentes',
        'aumento_reducao': 'Aumento (Redução) de Caixa e Equivalentes',
        'posicao_acionaria': 'Posição Acionária*',
        'informacoes_posicao_acionaria_recebida_em': 'Informação recebida em',
        'acoes_em_circulacao_mercado': 'Ações em Circulação no Mercado',
        'composicao_capital_social': 'Composição do Capital Social'
    }
    data = list(break_words.keys())

    for pdf in pdf_list:
        reader = PdfReader(os.path.join(ATIVOS_DIR, pdf))
        
        number_of_pages = len(reader.pages)
        
        text = []
        pdf_dict = {}
        for n_page in range(0, number_of_pages):
            page = reader.pages[n_page]

            text.append(page.extract_text())
            
        text = ''.join(text)
            
        for i in range(0, len(data)):
            if (i == len(data)-1):
                pdf_dict[data[i]] = ''.join(text.split(break_words[data[i]])[1]).replace("\n", " ").strip()
                break

            try:
                pdf_dict[data[i]] = ''.join(text.split(break_words[data[i]])[1].split(break_words[data[i+1]])[0]).replace("\n", " ").strip()
            except:
                try:
                    pdf_dict[data[i]] = ''.join(text.split(break_words[data[i+1]])[1].split(break_words[data[i]])[0]).replace("\n", " ").strip()
                except:
                    pass

        with open(f'./{RESULT_DIR}/{pdf}.csv', 'w') as f:
            w = csv.DictWriter(f, pdf_dict.keys())
            w.writeheader()
            w.writerow(pdf_dict)
