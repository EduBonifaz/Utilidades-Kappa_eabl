from Code.DCDQRules import DCQRRulesGen
from Code.RCRules import RCRulesGen


path = [
    'Resource/staging.conf',
    'Resource/raw.conf',
    'Resource/master.conf'
]

spreedsheetRC = ""
RCRulesGen(path, spreedsheetRC)

spreedsheetDCQR = ""
DCQRRulesGen(path, spreedsheetDCQR)

