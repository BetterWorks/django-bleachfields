from jsonfield import JSONField

from .bleachfield import BleachField


class BleachJSONField(BleachField, JSONField):

    def pre_save(self, model_instance, add):
        new_value = getattr(model_instance, self.attname)
        clean_value = self._bleach_walk(new_value)
        setattr(model_instance, self.attname, clean_value)
        return clean_value

    def _bleach_walk(self, node):
        cleaned = node
        if isinstance(node, basestring):
            cleaned = self.clean_text(node)
        elif isinstance(node, dict):
            cleaned = {}
            for key, value in node.iteritems():
                cleaned[self._bleach_walk(key)] = self._bleach_walk(value)
        elif isinstance(node, list):
            cleaned = [self._bleach_walk(element) for element in node]

        return cleaned
