from pyhocon import ConfigFactory
import pandas as pd
from Code import Objetos as ob
import pygsheets
from Code import Diccionario as dc

gc = pygsheets.authorize(service_file='credentials/credential.json')

rcfields = [ob.COLUMN, ob.COLUMNS]
threshold = [ob.MIN_THRESHOLD, ob.TARGET_THRESHOLD, ob.ACCEPTANCE_MIN]
criticidad = [ob.CRITICAL, ob.REFUSALS]


def RCRulesGen(lista: list, spreedsheet :str):
    sh = gc.open_by_key(spreedsheet)
    wks = sh.worksheet_by_title("Plantilla de Ingesta")
    rc_rules_aux = pd.DataFrame([])
    RCvacio=pd.DataFrame([])
    RCvacio2 =pd.DataFrame([["","","","","","","","","","","","","",""]])
    for i in range(50):
        RCvacio = pd.concat([RCvacio,RCvacio2])

    wks.set_dataframe(RCvacio,(6,1),copy_head=False)

    for i in range(len(lista)):
        conf = ConfigFactory.parse_file(lista[i])

        for j in range(len(conf["hammurabi.rules"])):
            confAux = conf["hammurabi.rules"][j]
            tipoRegla = dc.TipoRegla[ob.RULE_CLASS.decide(confAux)]
            newRule = []

            newRule.append(dc.NombreCampo(ob.COLUMN.decide(confAux) + ob.COLUMNS.decide(confAux)))

            newRule.append(dc.DescipcionRegla[tipoRegla])

            newRule.append(dc.Interesado[dc.MVPRules(tipoRegla)])

            newRule.append(dc.MVPRules(tipoRegla))

            newRule.append(dc.NombreCampo(ob.COLUMN.decide(confAux) + ob.COLUMNS.decide(confAux)))

            newRule.append(dc.PrincipioCalidad[tipoRegla[0]])

            newRule.append(tipoRegla)

            for dato in threshold:
                newRule.append(dato.decide(confAux) + "%")

            for dato in criticidad:
                newRule.append(dato.decide(confAux).upper())

            newRule.append((conf.get_string("hammurabi.dataFrameInfo.objectPathName")).split("/")[2].title())

            newRule.append("")

            df = pd.DataFrame([newRule])

            rc_rules_aux = pd.concat([rc_rules_aux, df])

    wks.set_dataframe(rc_rules_aux,(6,1),copy_head=False)


