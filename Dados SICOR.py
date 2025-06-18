# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 13:38:13 2024

@author: joao.machado
"""

# PACOTES 

import polars as pl

"""

Dados desagregados do SICOR

1. ESCOLHER O ARQUIVO PARA ALGUM ANO 

2. SELECIONAR AS VARIÁVEIS PARA ESSE ANO 

3. USAR AS OUTRAS TABELAS COM OS CÓDIGOS PARA PEGAR PRODUTO E VARIEDADE

4. AGREGAR PARA DIMINUIR UM POUCO A BASE

"""



#### definindo os anos ####

anos = [2024]

path = r".."

#### importando tabelas auxiliares ####

empreendimentos = pl.read_csv(path + r'\Empreendimento.csv', 
                              encoding = 'latin1') # produtos e variedades

empreendimentos = empreendimentos.select(['FINALIDADE','ATIVIDADE','MODALIDADE','PRODUTO','VARIEDADE','#CODIGO'])

empreendimentos = empreendimentos.rename({'#CODIGO':'CD_EMPREENDIMENTO'})

print(empreendimentos)

fontes = pl.read_csv(path + r'\FonteRecursos.csv', encoding = 'latin1')

fontes = fontes.rename({'#CODIGO':'CD_FONTE_RECURSO'})

fontes = fontes.select(['CD_FONTE_RECURSO', 'DESCRICAO'])

print(fontes)

valores = pl.read_csv(r"..SICOR_LIBERACAO_RECURSOS.csv", separator = ';')

print(valores)

programas = pl.read_csv(path + r'\Programa.csv', encoding = 'latin1')

programas = programas.rename({'#CODIGO':'CD_PROGRAMA',
                              'DESCRICAO':'DESCRICAO_PROGRAMA'})

programas = programas.select(['CD_PROGRAMA','DESCRICAO_PROGRAMA'])

print(programas)

subprogramas = pl.read_csv(path + r'\Subprogramas.csv', encoding = 'latin1', separator = ';')

subprogramas = subprogramas.rename({'#CODIGO_SUBPROGRAMA':'CD_SUBPROGRAMA',
                                    'CODIGO_PROGRAMA':'CD_PROGRAMA'})

subprogramas = subprogramas.select(['CD_SUBPROGRAMA','DESCRICAO_SUBPROGRAMA','CD_PROGRAMA'])

subprogramas.columns

agro = pl.read_csv(path + r'\TipoAgropecuaria.csv', encoding = 'latin1')

agro= agro.rename({'#CODIGO':'CD_TIPO_AGRICULTURA',
                   'DESCRICAO':'DESCRICAO_AGRO'})

cultivo = pl.read_csv(path + r'\TipoCultivo.csv', encoding = 'latin1')

cultivo = cultivo.rename({'#CODIGO':'CD_TIPO_CULTIVO',
                          'DESCRICAO':'DESCRICAO_CULTIVO'})

integr = pl.read_csv(path + r'\TipoIntegracao.csv', encoding = 'latin1')

integr = integr.rename({'#CODIGO':'CD_TIPO_INTGR_CONSOR',
                        'DESCRICAO':'DESCRICAO_INTEGRACAO'})

print(cultivo)

#### definindo os arquivos ####

# ano = 2013

for ano in anos: 
            
    arquivo = rf'..SICOR_OPERACAO_BASICA_ESTADO_{ano}\SICOR_OPERACAO_BASICA_ESTADO_{ano}.csv'
    
    df = pl.read_csv(arquivo, separator = ';',dtypes={'CD_CONTRATO_STN': pl.Utf8})
    
    #### pegando os valores e colocando na tabela das operações ####
    
    df = df.rename({'#REF_BACEN':'REF_BACEN'})
    
    df = df.join(valores, on = ['REF_BACEN','NU_ORDEM'], how = 'left')
    
    #### pegando os valores dos empreendimentos ####
    
    df = df.join(empreendimentos, on = 'CD_EMPREENDIMENTO', how = 'left')
    
    print(df)
    
    #### diminuindo as colunas ####
    
    # colunas_drop = ['CNPJ_IF',
    #                 'CD_INST_CREDITO',
    #                 'CD_CATEG_EMITENTE',
    #                 'CNPJ_AGENTE_INVEST',
    #                 'CD_TIPO_SEGURO',
    #                 'CD_TIPO_ENCARG_FINANC',
    #                 'CD_FASE_CICLO_PRODUCAO',
    #                 'CD_TIPO_GRAO_SEMENTE',
    #                 'VL_ALIQ_PROAGRO',
    #                 'VL_RECEITA_BRUTA_ESPERADA',
    #                 'VL_AREA_FINANC',
    #                 'DT_FIM_COLHEITA',
    #                 'DT_FIM_PLANTIO',
    #                 'DT_INIC_COLHEITA',
    #                 'DT_INIC_PLANTIO',
    #                 'CD_CONTRATO_STN',
    #                 'CD_CNPJ_CADASTRANTE',
    #                 'VL_AREA_INFORMADA',
    #                 'CD_CICLO_CULTIVAR',
    #                 'CD_TIPO_SOLO',
    #                 'PC_BONUS_CAR',
    #                 '#LIR_DT_LIBERACAO',
    #                 'LIR_VL_LIBERADO',
    #                 'CD_TIPO_IRRIGACAO',
    #                 'CD_REF_BACEN_INVESTIMENTO']
    
    
    
    # df = df.drop(colunas_drop)
    
    #### trocando códigos por valores que realmente interessam ####
    
    ### FONTES
    
    df = df.join(fontes, on = 'CD_FONTE_RECURSO', how = 'left')
    
    df = df.rename({'DESCRICAO':'DESCRICAO_FONTES'})
    
    ### PROGRAMAS
    
    df = df.join(programas, on = 'CD_PROGRAMA', how = 'left')
    
    ### SUBPROGRAMAS
    
    subs = [int(x) if x is not None else None for x in df['CD_SUBPROGRAMA']]
    
    df = df.with_columns([
        pl.Series('CD_SUBPROGRAMA',subs)
        ])
    
    df = df.join(subprogramas, on = ['CD_SUBPROGRAMA','CD_PROGRAMA'], how = 'left')
    
    ### TIPO DE AGRICULTURA
    
    df = df.join(agro, on = 'CD_TIPO_AGRICULTURA', how = 'left')
    
    ### TIPO DE CULTIVO
    
    df = df.join(cultivo, on = 'CD_TIPO_CULTIVO', how = 'left')
    
    ### TIPO DE INTEGRAÇÃO
    
    df = df.join(integr, on = 'CD_TIPO_INTGR_CONSOR', how = 'left')
    
    df.columns
    
    ### salvar xlsx
    
    dir(df)
    
    df.to_pandas().to_csv(rf'..DADOS_{ano}.csv', index = False)
    






