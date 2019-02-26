import re

def update():

    with open('webpage/static/css/index_raw.css', 'r', encoding='UTF-8') as f1:
        css_raw = f1.read()
        timetable_td_size_1 = re.findall('  --td-size-1:(.*?);', css_raw)[0]
        timetable_td_size_2 = re.findall('  --td-size-2:(.*?);', css_raw)[0]
        timetable_gap_size = re.findall('  --gap-size:(.*?);', css_raw)[0]
        print(timetable_td_size_1, timetable_td_size_2)
        with open('webpage/static/css/index.css', 'w', encoding='UTF-8') as f2:
            f2.write(css_raw.replace('var(--td-size-1)', timetable_td_size_1).replace('var(--td-size-2)', timetable_td_size_2).replace('var(--gap-size)', timetable_gap_size))