import yaml
import os

class Config(object):
    def __init__(self, data = None, file = None):
        self.data = data
        if file:
            assert(not data), 'Config object need EITHER data stream OR file to read from, not both.'
            self.data = read_yaml(file)
        self.attribute_names, self.qi_indices, self.is_cat, self.sa_index = self.get_anonymize_config()

    def get_anonymize_config(self):
        data = self.data
        if not data:
            return None, None, None, None
        attribute_names = [ att['name'] for att in data['columns'] ]
        qi_indices = []
        is_cat = []
        sa_index = None
        for i in range(len(attribute_names)):
            is_qi = data['columns'][i]['is_qi']
            if is_qi:
                qi_indices.append(data['columns'][i]['index'])
                if data['columns'][i]['type'] == 'category':
                    is_cat.append( True )
                else:
                    is_cat.append(False)
                continue
            is_sensible = data['columns'][i]['is_sensible']
            if is_sensible:
                sa_index = data['columns'][i]['index']
        print('attribute names: \n\t %s\n' % attribute_names)
        print('qi_indices: \n\t %s\n' % qi_indices)
        print('is cat: \n\t %s\n' % is_cat)
        print('sa_index: \n\t %s\n' % sa_index)
        return attribute_names, qi_indices, is_cat, sa_index


def read_yaml(file):
    with open(file, 'r') as readfile:
        data = yaml.load(readfile)
    print(data)
    return data

def write_yaml(self, data, file=None):
    if not file:
        file = '.yaml'
    with open('output-' + file, 'w') as writefile:
        yaml.dump(data, writefile, default_flow_style=False)

if __name__ == '__main__':
    FILENAME = 'adult.yaml'
    file = FILENAME
    #data = read_yaml(file)
    #write_yaml(data, file)
    #get_anonymize_config(data)
    config = Config(file=file)