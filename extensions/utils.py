from . import jalali
from django.utils import timezone
def converter_number_to_persian(mystr):
    num={
    "1":"1",
    "2":"2",
    "":"",
    "":"",
    "":"",
    "":"",
    "":"",
    }

def jalali_converter(time):
    time=timezone.localtime(time)
    time_to_str="{},{},{}".format(time.year,time.month,time.day)
    jmonth=["فروردین","اردیبهشت","خرداد","تیر","مرداد","شهریور","مهر","آبان","آذر","دی","بهمن","اسفند"]
    output_to_tuple=jalali.Gregorian(time_to_str).persian_tuple()
    output_to_string=jalali.Gregorian(time_to_str).persian_string()

    time_to_list=list(output_to_tuple)
    # for index,month in enumerate(jmonth):
    #     if time_to_list[1]==index+1:
    #         time_to_list[1]=month
    #         break
# ماه از 1 شروع میشود اما
# jmanth
# از0 شروع میشود
    output_to_nmonth_saat="{} {} {}، ساعت {}:{}".format(
    time_to_list[2],jmonth[time_to_list[1]-1],time_to_list[0],time.hour,time.minute
    )

    return output_to_nmonth_saat
