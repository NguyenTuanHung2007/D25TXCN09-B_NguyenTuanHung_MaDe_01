student_list = [
    {
        'id': 'SV001',
        'ten': 'Nguyen Van A',
        'diem_toan': 8.5,
        'diem_ly': 7.0,
        'diem_hoa': 9.0,
        'diem_tb': 8.17,
        'xep_loai': 'Gioi'
    }
]

def calculate_average(math, physics, chemistry):
    return round((math + physics + chemistry) / 3, 2)

def get_classification(average):
    if average < 5.0:
        return 'Yeu'
    elif average < 7.0:
        return 'TB'
    elif average < 8.0:
        return 'Kha'
    else:
        return 'Gioi'

def display_students(data):
    if not data:
        print('Danh sach trong')
        return
    print('-' * 85)
    print(f'{'ID':<10} | {'Ho Ten':<20} | {'Toan':<5} | {'Ly':<5} | {'Hoa':<5} | {'DTB':<5} | {'Xep loai'}')
    print('-' * 85)
    for s in data:
        print(f'{s['id']:<10} | {s['ten']:<20} | {s['diem_toan']:<5} | {s['diem_ly']:<5} | {s['diem_hoa']:<5} | {s['diem_tb']:<5} | {s['xep_loai']}')
    print('-' * 85)

def add_student():
    while True:
        student_id = input('Nhap Ma SV: ')
        exists = False
        for s in student_list:
            if s['id'] == student_id:
                exists = True
                break
        if exists:
            print('Ma SV da ton tai')
        else:
            break
            
    name = input('Nhap Ho Ten: ')
    
    def input_score(label):
        while True:
            try:
                val = float(input(f'Nhap diem {label} (0-10): '))
                if 0 <= val <= 10:
                    return val
                print('Diem phai trong khoang 0-10')
            except ValueError:
                print('Vui long nhap so')

    math = input_score('Toan')
    phys = input_score('Ly')
    chem = input_score('Hoa')
    
    avg = calculate_average(math, phys, chem)
    rank = get_classification(avg)
    
    new_student = {
        'id': student_id,
        'ten': name,
        'diem_toan': math,
        'diem_ly': phys,
        'diem_hoa': chem,
        'diem_tb': avg,
        'xep_loai': rank
    }
    student_list.append(new_student)
    print('Them thanh cong')

def update_student():
    student_id = input('Nhap Ma SV can sua: ')
    for s in student_list:
        if s['id'] == student_id:
            print(f'Sua thong tin cho: {s['ten']}')
            s['diem_toan'] = float(input('Nhap diem Toan moi: '))
            s['diem_ly'] = float(input('Nhap diem Ly moi: '))
            s['diem_hoa'] = float(input('Nhap diem Hoa moi: '))
            s['diem_tb'] = calculate_average(s['diem_toan'], s['diem_ly'], s['diem_hoa'])
            s['xep_loai'] = get_classification(s['diem_tb'])
            print('Cap nhat thanh cong')
            return
    print('Khong tim thay sinh vien')

def delete_student():
    student_id = input('Nhap Ma SV can xoa: ')
    for i in range(len(student_list)):
        if student_list[i]['id'] == student_id:
            confirm = input(f'Xac nhan xoa {student_list[i]['ten']} (y/n): ')
            if confirm.lower() == 'y':
                student_list.pop(i)
                print('Da xoa')
            return
    print('Khong tim thay sinh vien')

def search_student():
    keyword = input('Nhap tu khoa: ').lower()
    results = [s for s in student_list if keyword in s['id'].lower() or keyword in s['ten'].lower()]
    display_students(results)

def sort_students():
    print('1. Diem TB giam dan')
    print('2. Ten tang dan')
    mode = input('Chon: ')
    if mode == '1':
        student_list.sort(key=lambda x: x['diem_tb'], reverse=True)
    elif mode == '2':
        student_list.sort(key=lambda x: x['ten'].split()[-1])
    print('Da sap xep')

def show_stats():
    summary = {'Gioi': 0, 'Kha': 0, 'TB': 0, 'Yeu': 0}
    for s in student_list:
        summary[s['xep_loai']] += 1
    print('Thong ke:')
    for k, v in summary.items():
        print(f'{k}: {v}')

def show_limit_scores():
    if not student_list:
        return
    highest = max(student_list, key=lambda x: x['diem_tb'])
    lowest = min(student_list, key=lambda x: x['diem_tb'])
    print(f'Cao nhat: {highest['ten']} ({highest['diem_tb']})')
    print(f'Thap nhat: {lowest['ten']} ({lowest['diem_tb']})')

def run_menu():
    while True:
        print('\nMENU QUAN LY')
        print('1. Hien thi danh sach sinh vien')
        print('2. Them sinh vien')
        print('3. Cap nhat sinh vien')
        print('4. Xoa sinh vien')
        print('5. Tim kiem sinh vien')
        print('6. Sap xep')
        print('7. Thong ke')
        print('8. Diem cao nhat va thap nhat')
        print('0. Thoat')
        
        cmd = input('Chon: ')
        if cmd == '1': 
            display_students(student_list)
        elif cmd == '2': 
            add_student()
        elif cmd == '3': 
            update_student()
        elif cmd == '4': 
            delete_student()
        elif cmd == '5': 
            search_student()
        elif cmd == '6': 
            sort_students()
        elif cmd == '7': 
            show_stats()
        elif cmd == '8': 
            show_limit_scores()
        elif cmd == '0':
            print('Tam biet')
            break
        else:
            print('Khong hop le')

if __name__ == '__main__':
    run_menu()