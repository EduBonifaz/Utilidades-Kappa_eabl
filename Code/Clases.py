from pyhocon.exceptions import ConfigMissingException
import pyhocon


def clear(string: str):
    limpio = string.replace("[", "").replace("(", "").replace("'", "").replace(")", "").replace("]", "")
    return limpio


def replacequotes(string: str):
    limpio = string.replace("\'", "\"")
    return limpio


class Dato:

    def __init__(self, path):
        self.path = path
        self.name = path.split(".")[-1]

    def decide(self, conf):
        try:
            value = conf.get_string(self.path)
        except ConfigMissingException:
            value = None
        if value is None:
            return ""
        else:
            if isinstance(conf[self.path], str):
                return replacequotes(value)
            elif isinstance(conf[self.path], int):
                return replacequotes(value)
            elif isinstance(conf[self.path], float):
                return replacequotes(value)
            elif isinstance(conf[self.path], bool):
                return replacequotes(value)
            elif isinstance(conf[self.path], list):
                out = ""
                for i in range(len(conf[self.path])):
                    if type(conf[self.path][i]) is pyhocon.config_tree.ConfigTree:
                        pridat='{\n'
                        for k,d in conf[self.path][i].items():
                            pridat+=f'{k}="{d}"\n'
                        pridat+='}\n'
                        print(pridat)
                        out = out + ",\"" + pridat + "\""
                    else:
                        out = out + ",\"" + conf[self.path][i] + "\""
                return replacequotes(out[1:])
            elif isinstance(conf[self.path], pyhocon.config_tree.ConfigTree):
                listaNames = ["applyConversions", "options", "castMode", "charset", "metadataType", "position", "length", "path", "paths", "schema", "type"]
                out = "{\n" + " }"
                for i in range(len(listaNames)):
                    if Dato(self.path+"."+listaNames[i]).decide(conf) != '':
                        out = out[0:-1] + Dato(self.path+"."+listaNames[i]).name + " = " + Dato(self.path+"."+listaNames[i]).decide(conf) + "\n }"
                    else:
                        out = out
                return replacequotes(out)
