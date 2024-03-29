# coding:utf-8
import logging,time,os.path

class Logger(object):
    def __init__(self,logger):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        rq = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        log_path = os.path.dirname(os.path.abspath('..')) + '/logs/'
        #print(log_path)
        log_name = log_path + rq + '.log'
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        logformat = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s')
        fh.setFormatter(logformat)
        ch.setFormatter(logformat)
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
    def getlogger(self):
        return self.logger

# if __name__ == '__main__':
#     logger = Logger('test')