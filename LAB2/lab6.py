from collections import OrderedDict
color_dict = {'red':'#FF0000',
              'green':'#008000',
              'black':'#000000',
              'white':'#FFFFFF'}



dict1 = OrderedDict(sorted(color_dict.items()))
print(dict1)
