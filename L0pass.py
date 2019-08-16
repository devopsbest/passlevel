from ectools.config import set_environment

from ectools.db_query import execute_query


class_types = [3134176, 3134194, 3134195, 3134196, 3134197, 3134198, 3134199, 3134200, 3134201, 3134202]
sql3 = '''
declare @student_id as int
set @student_id = {}


insert into oboe..booking
values
'''
sql4 = "({}, @student_id, '2', 1, 1, 0, getdate()-3, getdate()-3, '1', NULL)"

sql5 = "\ninsert into oboe..StudentCourseClass \nvalues \n"

bookingid='{\"bookingId\": 574639}'
sql6 = """ (@student_id, 30010699, 3, 507, 9030865, {}, '{}',0, getdate(), getdate())"""

lists = class_types[3:11]




def passofflineclasses(env,memberid, select_list):
    # student_id = 23989928
    student_id = memberid

    sql7 = ''
    sql8 = ''


    if len(select_list) > 1:
        for x in select_list:
            sql8 = sql8 + sql4.format(class_types[x]) + "," + "\n"
            sql7 = sql7 + sql6.format(class_types[x],bookingid) + "," + "\n"

        sql = sql3.format(student_id) + sql8[0:-2] + sql5 + sql7[0:-2]

    else:
        sql = sql3.format(student_id) + sql4.format(class_types[select_list[0]]) + sql5 + sql6.format(class_types[select_list[0]],bookingid)

    from ectools.logger import get_logger


    if env in ["mobilefirst","uat"]:

        set_environment('uat')
        get_logger(sql)
        print(sql)
        execute_query(sql)

    return sql





if __name__ == "__main__":
    passofflineclasses("uat",23989907,[2])





