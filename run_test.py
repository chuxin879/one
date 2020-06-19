from datetime import datetime
from unittest import TestLoader
import os

from lib.HTMLTestRunner import HTMLTestRunner



def run():
    case_suite = TestLoader().discover("./test")
    report_name = os.path.join("./report" , datetime.now().strftime("%Y%m%d%H%M%S") + ".html")
    with open(report_name, "wb") as fp:
        runner = HTMLTestRunner(stream=fp, verbosity=2, title=datetime.now().strftime("%Y%m%d%H%M%S"), tester="dongdong.guo")
        runner.run(case_suite)
    

if __name__ == "__main__":

    run()
    
     
    
    