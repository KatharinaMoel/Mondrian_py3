"""
read adult dataset
"""

# !/usr/bin/env python
# coding=utf-8

# Read data and read tree fuctions for INFORMS data
# attributes ['age', 'workclass', 'final_weight', 'education', 'education_num',
# 'matrital_status', 'occupation', 'relationship', 'race', 'sex', 'capital_gain',
# 'capital_loss', 'hours_per_week', 'native_country', 'class']
# QID ['age', 'workcalss', 'education', 'matrital_status', 'race', 'sex', 'native_country']
# SA ['occupation']

from utils.utility import cmp_str
from utils import yaml_tools

config = yaml_tools.Config(file = 'data/adult_plot2.yaml')
ATT_name = config.attribute_names
QI_INDEX = config.qi_indices
IS_CAT = config.is_cat 
SA_INDEX = config.sa_index

__DEBUG = False


def read_data():
    """
    read microda for *.txt and return read data

    # Note that Mondrian can only handle numeric attribute
    # So, categorical attributes should be transformed to numberic attributes
    # before anonymization. For example, Male and Female shold be transformed
    # to 0, 1 during pre-processing. Then, after anonymization, 0 and 1 should
    # be transformed to Male and Female.
    """
    QI_num = len(QI_INDEX)
    data = []
    # order categorical attributes in intuitive order
    # here, we use the appear number
    intuitive_dict = []
    intuitive_order = []
    intuitive_number = []
    for i in range(QI_num):
        intuitive_dict.append(dict())
        intuitive_number.append(0)
        intuitive_order.append(list())
    data_file = open('data/adult_klein.data', 'rU')
    for line in data_file:
        line = line.strip()
        # remove empty and incomplete lines
        # only 30162 records will be kept
        if len(line) == 0 or '?' in line:
            continue
        # remove double spaces
        line = line.replace(' ', '')
        temp = line.split(',')
        ltemp = []
        for i in range(QI_num):
            index = QI_INDEX[i]
            if IS_CAT[i]:
                try:
                    ltemp.append(intuitive_dict[i][temp[index]])
                except KeyError:
                    intuitive_dict[i][temp[index]] = intuitive_number[i]
                    ltemp.append(intuitive_number[i])
                    intuitive_number[i] += 1
                    intuitive_order[i].append(temp[index])
            else:
                ltemp.append(int(temp[index]))
        ltemp.append(temp[SA_INDEX])
        data.append(ltemp)
    return data, intuitive_order
