#import os
#from os.path import join
#import zipfile
#
#for root, dirs, files in os.walk('C:\\Users\\Ian\\ianmshelton.com\\test'):
#    for name in files:
#        file_name = '{}\\{}'.format(root, name)
#        print(file_name)
#        folder_name = name.replace('.zip', '')
#        print(folder_name)
#        z = zipfile.ZipFile(file_name).extractall('C:\\Users\\Ian\\ianmshelton.com\\dest\\{}'.format(folder_name))
#
#for root, dirs, files in os.walk('C:\\Users\\Ian\\ianmshelton.com\\dest'):
#    for name in files:
#        if(name=='image1.emf'):
#            x = os.path.abspath(os.path.join(root, os.pardir))
#            x = os.path.abspath(os.path.join(x, os.pardir))
#            x = x.rsplit('\\',1)[1]
#            x = '{}.emf'.format(x)
#            os.rename(join(root, name), join(root, x))
#            print(x)


from PIL import Image

Image.open('C:\\Users\\Ian\\ianmshelton.com\\test.emf').save('C:\\Users\\Ian\\ianmshelton.com\\test_o.pdf')
