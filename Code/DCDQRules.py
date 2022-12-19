from pyhocon import ConfigFactory
import pandas as pd
from Code import Objetos as ob
import pygsheets

gc = pygsheets.authorize(service_file='credentials/credential.json')


columns = ob.columns
dataframeInfo = [ob.PHYSICAL_PATH, ob.FILE_TYPE, ob.EXTRA_OPTIONS, ob.SCHEMA_PATH, ob.DATA_DATE, ob.SUBSET, ob.SAMPLE,
                 ob.UUAA, ob.OBJECT_PHYSICAL_PATH, ob.PHYSICAL_NAME_OBJECT, ob.FREQUENCY_RULE_EXECUTION]
ruleInfo = [ob.CRITICAL, ob.REFUSALS, ob.ACCEPTANCE_MIN, ob.MIN_THRESHOLD, ob.TARGET_THRESHOLD,
            ob.DRILLDOWN, ob.AGGREGATION, ob.COLUMN, ob.COLUMNS, ob.CONDITION, ob.COMPARISON, ob.DATA_SOURCE_ID_RULE,
            ob.DATA_VALUES, ob.DATA_VALUES_COLUMN, ob.DATA_VALUES_CONDITION, ob.FORMAT, ob.KEY_COLUMNS, ob.LOWER_BOUND,
            ob.UPPER_BOUND, ob.PHYSICAL_FIELD_VALUE, ob.PHYSICAL_FIELD_CATALOG_VALUES, ob.VARIATION_ALLOWED, ob.SUBSET_RULE,
            ob.BALANCE_ACCEPTANCE_MIN, ob.BALANCE_IDS, ob.RATINGS, ob.NOTCHES, ob.NOTCHES_COLUMN,
            ob.NOTCHES_COLUMN_VALUES]


def DCQRRulesGen(lista: list, spreedsheet :str):
    sh = gc.open_by_key(spreedsheet)
    wks = sh.worksheet_by_title("DC-DQ-Rules")
    dcqr_rules = pd.DataFrame([], columns=columns)

    for i in range(len(lista)):
        conf = ConfigFactory.parse_string(lista[i])
        for j in range(len(conf["hammurabi.rules"])):
            newRule = [ob.PHYSICAL_NAME_OBJECT.decide(conf)]
            for dato in dataframeInfo:
                newRule.append(dato.decide(conf))

            newRule.append(ob.RULE_CLASS.decide(conf["hammurabi.rules"][j]))

            for data in ruleInfo:
                newRule.append(data.decide(conf["hammurabi.rules"][j]))

            df = pd.DataFrame([newRule], columns=columns)

            dcqr_rules = pd.concat([dcqr_rules, df])

    wks.set_dataframe(dcqr_rules,(5,1),copy_head=False)
    print("DCQRRulesGen")
    print("https://docs.google.com/spreadsheets/d/"+spreedsheet)
    print()
    # dcqr_rules.to_csv('C:/Users/w10/Documents/Repositorios/DC-DQ-Rules/' + nameout,index=False)

