result = 0
last_missed = 0


def probable_attendance(prev_attendance, cur_attendance, missed_attendance, no_of_days, attendance, missed_flag):
    global result
    global last_missed

    if missed_attendance >= 4:
        missed_flag = True
        return

    if no_of_days == attendance:
        attendance_str = prev_attendance + cur_attendance
        if missed_flag:
            return
        if cur_attendance == 'A':
            last_missed += 1
        result += 1
        return

    probable_attendance(prev_attendance=prev_attendance+cur_attendance, cur_attendance="P",
                              missed_attendance=0, no_of_days=no_of_days+1, attendance=attendance, missed_flag=missed_flag)
    probable_attendance(prev_attendance=prev_attendance+cur_attendance, cur_attendance="A",
                              missed_attendance=missed_attendance+1, no_of_days=no_of_days+1, attendance=attendance, missed_flag=missed_flag)
    return str(last_missed)+'/'+str(result)

print(probable_attendance("", "", 0, 0, 5, False))
