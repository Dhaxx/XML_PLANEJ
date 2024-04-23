import xml.etree.ElementTree as ET
import interface as inter
import conexao as cnx

cur_dest = cnx.conexao_destino.cursor()
tree = ET.parse('cad_ppa.xml')
root = tree.getroot()

programas = root.findall('.//{http://www.tce.sp.gov.br/audesp/xml/planejamento}Programa')

for programa in programas:
    numero = programa.find('{http://www.tce.sp.gov.br/audesp/xml/planejamento}NumeroPrograma').text
    objetivo = programa.find('{http://www.tce.sp.gov.br/audesp/xml/planejamento}ObjetivoPrograma').text
    classif = programa.find('{http://www.tce.sp.gov.br/audesp/xml/planejamento}ClassificacaoPrograma').text
    justif = programa.find('{http://www.tce.sp.gov.br/audesp/xml/planejamento}JustificativaPrograma').text

    try:
        for ods in programa.findall('{http://www.tce.sp.gov.br/audesp/xml/planejamento}Ods'):
            codigo_ods = ods.find('{http://www.tce.sp.gov.br/audesp/xml/planejamento}CodigoODS').text 
            for meta in ods.findall('{http://www.tce.sp.gov.br/audesp/xml/planejamento}Metas'):
                for codigo_meta in meta.findall('{http://www.tce.sp.gov.br/audesp/xml/planejamento}CodigoMeta'):
                    cur_dest.execute(f'Insert into ppa_progods (codprog, codods, codmetaods) values ({int(numero)},{codigo_ods},{codigo_meta.text})')
    except Exception as e:
        print(str(e))

    cur_dest.execute(f"update tabprograma set objetivo = '{objetivo}', classif = '{classif}' where programa = {numero}")
    cur_dest.execute(f"update ppa_programa set justif = '{justif}' where codprog = {int(numero)}") # Validar pela fk_tabprograma
inter.commit()