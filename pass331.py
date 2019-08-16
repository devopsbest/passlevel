


from ectools.config import set_environment
from ectools.offline_class_helper import achieve_minimum_class_taken, HelperConfig

def passofflinelessons(id):
    student_id = id
    set_environment('uat')
    HelperConfig.LevelMustComplete = True
    HelperConfig.LevelEnrollDateShift = {'days': -30}
    HelperConfig.ClassTakenSince = {'days': -29}
    HelperConfig.ClassTakenUntil = {'days': -1}
    try:
        achieve_minimum_class_taken(student_id, f2f=3, workshop=3, apply_or_lc=1, online_pl=0, online_gl=0)
    except Exception as e:
        print(e)