import configparser
import os

#handle configuration file
class ConfHandler():

    dicSections = {}
    
    def __init__(self,file_full_path):

        if not os.path.exists(file_full_path):
            raise Exception('path not correct: {0}'.format(file_full_path))
        
        config = configparser.ConfigParser()
        config.read(file_full_path)
        
##        if os.getcwd()[os.getcwd().rindex('\\')+1:]=='lib':
##            config.read('../'+path+file)    
##        else:
##            config.read(path+file)
        
        for s in config.sections():
            dicParams = {}
            for p in config[s]:
                dicParams[p] = config[s][p]
            self.dicSections[s] = dicParams

    def get(self,section,param):
        return self.dicSections[section][param]

    def get_section(self,section):
        return self.dicSections[section]
        

if __name__ == "__main__":
    conf = ConfHandler('../conf/test.ini')
    print(conf.get('test_section','test_key'))
    dic = conf.get_section('test_section')
    print(dic)
    

    
