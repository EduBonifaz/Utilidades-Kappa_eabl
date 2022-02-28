from Code.DCDQRules import DCQRRulesGen
from Code.RCRules import RCRulesGen

path = ['Resource/staging.conf', 'Resource/raw.conf', 'Resource/master.conf']

spreedsheetRC = "1L_OE39sNXl4XYON9ZkJonG1prgVj-MHP--E8wpMQQc"
RCRulesGen(path, spreedsheetRC)

spreedsheetDCQR = "17KQ-3JoVDJyBrLevMSKelefRR7sQhqxUoIPKkTybF8"
DCQRRulesGen(path, spreedsheetDCQR)

