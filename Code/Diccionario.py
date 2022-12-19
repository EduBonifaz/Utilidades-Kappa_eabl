TipoRegla = {"com.datio.hammurabi.rules.availability.DateRangeFileRule": "1.1-Comprobar que el archivo se haya recibido en la fecha y hora acordadas",
                   "com.datio.hammurabi.rules.availability.DateValidationRule": "1.2-Actualización del valor de los datos en la fecha requerida",
                   "com.datio.hammurabi.rules.completeness.CompletenessRule": "2.1-Completitud registros",
                   "com.datio.hammurabi.rules.completeness.BasicPerimeterCompletenessRule": "2.2-Completitud requerida del perímetro entre STAGING y RAW [solo Datio]",
                   "com.datio.hammurabi.rules.completeness.ConditionalPerimeterCompletenessRule": "2.3-Completitud del perímetro requerido entre RAW y MASTER [solo Datio]",
                   "com.datio.hammurabi.rules.completeness.MetadataCompletenessRule": "2.4-Completitud requerida del perímetro entre el origen y staging [solo Datio]",
                   "com.datio.hammurabi.rules.validity.NotNullValidationRule": "3.1-Comprobación del valor de datos nulo (NULL o vacío)",
                   "com.datio.hammurabi.rules.validity.FormatValidationRule": "3.2-Comprobando el formato del campo",
                   "com.datio.hammurabi.rules.validity.StaticForbiddenValuesRule": "3.3-Comprobación de valores ilegales",
                   "com.datio.hammurabi.rules.validity.NumericRangeRule": "3.4-Verificación del valor de los datos dentro del rango esperado",
                   "com.datio.hammurabi.rules.validity.StringRangeRule": "3.4-Verificación del valor de los datos dentro del rango esperado",
                   "com.datio.hammurabi.rules.validity.DateRangeRule": "3.4-Verificación del valor de los datos dentro del rango esperado",
                   "com.datio.hammurabi.rules.validity.StaticCatalogRule": "3.5-Comprobación del valor de datos en el catálogo",
                   "com.datio.hammurabi.rules.validity.DynamicCatalogRule": "3.5-Comprobación del valor de datos en el catálogo",
                   "com.datio.hammurabi.rules.consistence.DuplicateRule":"4.2-Duplicación de registros para los mismos datos",
                   "com.datio.hammurabi.rules.consistence.ValueConciliationRule":"4.3-Conciliación contable/Integridad Referencial",
                   "com.datio.hammurabi.rules.integrity.ValueComparisonRule": "5.2-Comparación entre diferentes valores de datos relacionados entre sí (los campos están en diferentes objetos)",
                   "com.datio.hammurabi.rules.integrity.SameValueComparisonRule": "5.3-Comparación entre diferentes valores de datos relacionados entre sí (los campos están en el mismo objeto)",
                   "com.datio.hammurabi.rules.accuracy.StaticGatheringRule": "6.1-Concentración de valores de los mismos datos en un catálogo",
                   "com.datio.hammurabi.rules.accuracy.DynamicGatheringRule": "6.1-Concentración de valores de los mismos datos en un catálogo",
                   "com.datio.hammurabi.rules.accuracy.ValueSensitivityThresholdRule": "6.2-Comprobación de la sensibilidad del valor de un dato a un umbral",
                   "com.datio.hammurabi.rules.accuracy.ValueVariationRule": "6.4-Comparación del valor de los mismos datos entre períodos",
                   "com.datio.hammurabi.rules.accuracy.VolumetricTrendRule": "6.9-Tendencia de volumetría",
                   "com.datio.hammurabi.rules.accuracy.DynamicRatingVariationRule":"6.10-Comprobar que la tendencia (evolución) del valor de un mismo dato en el tiempo es aceptable con la variación referida a un catálogo",
                   "com.datio.hammurabi.rules.accuracy.StaticRatingVariationRule": "6.10-Comprobar que la tendencia (evolución) del valor de un mismo dato en el tiempo es aceptable con la variación referida a un catálogo",
                   "com.datio.hammurabi.rules.accuracy.HerfindahlRule": "6.11-Comparación del valor de un mismo dato entre periodos con la máxima variación referida a un catálogo dinámico."}

DescipcionRegla = {"1.1-Comprobar que el archivo se haya recibido en la fecha y hora acordadas": "Escribir descripción",
                   "1.2-Actualización del valor de los datos en la fecha requerida": "Escribir descripción",
                   "2.1-Completitud registros": "Evaluar que el archivo no este vacío",
                   "2.2-Completitud requerida del perímetro entre STAGING y RAW [solo Datio]": "Evaluar que el total de registros en Raw es igual al de Staging",
                   "2.3-Completitud del perímetro requerido entre RAW y MASTER [solo Datio]": "Evaluar que el total de registros en Master es igual al de Raw",
                   "2.4-Completitud requerida del perímetro entre el origen y staging [solo Datio]": "Evaluar que el total de registros en Staging es igual al de origen.",
                   "3.1-Comprobación del valor de datos nulo (NULL o vacío)": "Evaluar nulidad en campo",
                   "3.2-Comprobando el formato del campo": "Escribir que formato evalua",
                   "3.3-Comprobación de valores ilegales": "Escribir descripción",
                   "3.4-Verificación del valor de los datos dentro del rango esperado": "Escribir descripción",
                   "3.5-Comprobación del valor de datos en el catálogo": "Escribir descripción",
                   "4.2-Duplicación de registros para los mismos datos": "Evaluar duplicidad en campos",
                   "4.3-Conciliación contable/Integridad Referencial": "Escribir descripción",
                   "5.2-Comparación entre diferentes valores de datos relacionados entre sí (los campos están en diferentes objetos)": "Escribir descripción",
                   "5.3-Comparación entre diferentes valores de datos relacionados entre sí (los campos están en el mismo objeto)": "Escribir descripción",
                   "6.1-Concentración de valores de los mismos datos en un catálogo": "Escribir descripción",
                   "6.2-Comprobación de la sensibilidad del valor de un dato a un umbral": "Escribir descripción",
                   "6.4-Comparación del valor de los mismos datos entre períodos": "Escribir descripción",
                   "6.9-Tendencia de volumetría": "Escribir descripción",
                   "6.10-Comprobar que la tendencia (evolución) del valor de un mismo dato en el tiempo es aceptable con la variación referida a un catálogo": "Escribir descripción",
                   "6.11-Comparación del valor de un mismo dato entre periodos con la máxima variación referida a un catálogo dinámico.": "Escribir descripción"}

def MVPRules(name :str):
    aux = name.split("-")[0]
    if aux in {"2.1", "2.2", "2.3", "2.4", "3.1", "3.2", "4.2"}:
        value = "MVP"
    else:
        value = "Fuera de MVP"
    return value

Interesado = {"MVP" : "Data Hub", "Fuera de MVP" : "Product Owner"}

PrincipioCalidad = {"1": "1. Availability",
             "2": "2. Completeness",
             "3": "3. Validity",
             "4": "4. Consistence",
             "5": "5. Integrity",
             "6": "6. Accuracy"}

def NombreCampo(field:str):
    if field == "":
        value = "No aplica, regla a nivel objeto"
    else:
        value = field
    return value