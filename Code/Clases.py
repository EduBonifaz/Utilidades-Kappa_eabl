from pyhocon.exceptions import ConfigMissingException
import re


def clear(string: str):
    limpio = string.replace("[", "").replace("(", "").replace("'", "").replace(")", "").replace("]", "")
    return limpio


def replacequotes(string: str):
    limpio = string.replace("\'", "\"")
    return limpio


class Dato:

    def __init__(self, path):
        self.path = path

    def decide(self, conf):
        try:
            value = conf.get_string(self.path)
        except ConfigMissingException:
            value = ''
        return replacequotes(value)


class DatoList(Dato):

    def decide(self, conf):
        try:
            value = conf.get_list(self.path)
        except ConfigMissingException:
            value = ''
        out = ""
        for i in range(len(value)):
            out = out + ",\"" + value[i] + "\""
        return replacequotes(out[1:])


class DatoConfig(Dato):
    def decide(self, conf):
        try:
            value = conf.get_string(self.path)
        except ConfigMissingException:
            value = ''
        if value != '':
            value = re.search("\[.+\]", value)[0]
            value = value.split(",")
            out = "{\n" + " }"
            for i in range(int(len(value) / 2)):
                out = out[0:-1] + clear(value[2 * i]) + "=" + clear(value[2 * i + 1]) + "\n}"
            return replacequotes(out)
        else:
            return replacequotes(value)


class DatoConfig2(DatoConfig):
    def decide(self, conf):
        try:
            value = conf.get_string(self.path)
        except ConfigMissingException:
            value = ''
        if value != '':
            out = "{\n" \
                  + "path : " + conf.get_string(self.path + ".paths")[1:-2] \
                  + "\nschema : {\n     path : " + conf.get_string(self.path + ".schema.path")[1:] + "\" \n }" \
                  + "\ntype : " + conf.get_string(self.path + ".type") \
                  + "\n}"
            return replacequotes(out)
        else:
            return replacequotes(value)