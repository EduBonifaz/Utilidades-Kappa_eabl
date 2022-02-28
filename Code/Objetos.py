from Code.Clases import DatoList, Dato, DatoConfig, DatoConfig2

PHYSICAL_PATH = DatoList("hammurabi.input.paths")

FILE_TYPE = Dato("hammurabi.input.type")

EXTRA_OPTIONS = DatoConfig("hammurabi.input.options")

SCHEMA_PATH = Dato("hammurabi.input.schema.path")

DATA_DATE = Dato("hammurabi.dataFrameInfo.cutoffDate")

SUBSET = Dato("hammurabi.dataFrameInfo.subset")

SAMPLE = Dato("hammurabi.dataFrameInfo.sample")

UUAA = Dato("hammurabi.dataFrameInfo.uuaa")

OBJECT_PHYSICAL_PATH = Dato("hammurabi.dataFrameInfo.objectPathName")

PHYSICAL_NAME_OBJECT = Dato("hammurabi.dataFrameInfo.physicalObjectName")

FREQUENCY_RULE_EXECUTION = Dato("hammurabi.dataFrameInfo.frequencyRuleExecution")

RULE_CLASS = Dato("class")

CRITICAL = Dato("config.isCritical")

REFUSALS = Dato("config.withRefusals")

ACCEPTANCE_MIN = Dato("config.acceptanceMin")

SUBSET_RULE = Dato("config.none")

MIN_THRESHOLD = Dato("config.minThreshold")

TARGET_THRESHOLD = Dato("config.targetThreshold")

DRILLDOWN = Dato("config.none")

AGGREGATION = Dato("config.none")

COLUMN = Dato("config.column")

COLUMNS = DatoList("config.columns")

CONDITION = Dato("config.condition")

COMPARISON = Dato("config.none")

DATA_SOURCE_ID_RULE = Dato("config.none")

DATA_VALUES = DatoConfig2("config.dataValues")

DATA_VALUES_COLUMN = Dato("config.none")

DATA_VALUES_CONDITION = Dato("config.none")

FORMAT = Dato("config.format")

KEY_COLUMNS = Dato("config.none")

LOWER_BOUND = Dato("config.none")

UPPER_BOUND = Dato("config.none")

PHYSICAL_FIELD_VALUE = Dato("config.value")

PHYSICAL_FIELD_CATALOG_VALUES = Dato("config.none")

VARIATION_ALLOWED = Dato("config.none")

BALANCE_ACCEPTANCE_MIN = Dato("config.none")

BALANCE_IDS = Dato("config.none")

RATINGS = Dato("config.none")

NOTCHES = Dato("config.none")

NOTCHES_COLUMN = Dato("config.none")

NOTCHES_COLUMN_VALUES = Dato("config.none")

columns = ["CONFIG NAME", "PHYSICAL PATH", "FILE TYPE", "EXTRA OPTIONS", "SCHEMA PATH", "DATA DATE", "SUBSET", "SAMPLE",
           "UUAA", "OBJECT PHYSICAL PATH", "PHYSICAL NAME OBJECT", "FREQUENCY RULE EXECUTION", "RULE CLASS", "CRITICAL",
           "REFUSALS", "ACCEPTANCE MIN", "MIN THRESHOLD", "TARGET THRESHOLD", "DRILLDOWN", "AGGREGATION",
           "COLUMN", "COLUMNS", "CONDITION", "COMPARISON", "DATA SOURCE ID RULE", "DATA VALUES", "DATA VALUES COLUMN",
           "DATA VALUES CONDITION", "FORMAT", "KEY COLUMNS", "LOWER BOUND", "UPPER BOUND", "PHYSICAL FIELD VALUE",
           "PHYSICAL FIELD CATALOG VALUES", "VARIATION ALLOWED", "SUBSET RULE", "BALANCE ACCEPTANCE MIN", "BALANCE IDS",
           "RATINGS",
           "NOTCHES", "NOTCHES COLUMN", "NOTCHES COLUMN VALUES"]



