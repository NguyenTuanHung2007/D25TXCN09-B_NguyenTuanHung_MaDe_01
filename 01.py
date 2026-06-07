import json
import os

FILE_PATH = 'data.json'
student_list = []

def load_data():
    global student_list
    if os.path.exists(FILE_PATH):
        try:
            with open(FILE_PATH, 'r', encoding='utf-8') as f:
                student_list = json.load(f)
        except:
            student_list = []
    else:
        student_list = []

def save_data():
    with open(FILE_PATH, 'w', encoding='utf-8') as f:
        json.dump(student_list, f, indent=4, ensure_ascii=False)

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

def display_students():
    load_data()
    if not student_list:
        print('Danh sach trong')
        return
    print('-' * 95)
    print(f"{'Ma SV':<10} | {'Ho Ten':<20} | {'Toan':<6} | {'Ly':<6} | {'Hoa':<6} | {'TB':<6} | {'Xep Loai'}")
    print('-' * 95)
    for s in student_list:
        print(f"{s['id']:<10} | {s['ten']:<20} | {s['diem_toan']:<6} | {s['diem_ly']:<6} | {s['diem_hoa']:<6} | {s['diem_tb']:<6} | {s['xep_loai']}")
    print('-' * 95)

def input_score(label):
    while True:
        try:
            val = float(input(f'Nhap diem {label} (0-10): '))
            if 0 <= val <= 10:
                return val
            print('Diem phai trong khoang 0-10')
        except ValueError:
            print('Vui long nhap so')

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
    save_data()
    print('Them thanh cong')

def update_student():
    student_id = input('Nhap Ma SV can sua: ')
    for s in student_list:
        if s['id'] == student_id:
            print(f"Dang sua sinh vien: {s['ten']}")
            s['diem_toan'] = input_score('Toan moi')
            s['diem_ly'] = input_score('Ly moi')
            s['diem_hoa'] = input_score('Hoa moi')
            s['diem_tb'] = calculate_average(s['diem_toan'], s['diem_ly'], s['diem_hoa'])
            s['xep_loai'] = get_classification(s['diem_tb'])
            save_data()
            print('Cap nhat thanh cong')
            return
    print('Khong tim thay sinh vien')

def delete_student():
    student_id = input('Nhap Ma SV can xoa: ')
    for i in range(len(student_list)):
        if student_list[i]['id'] == student_id:
            confirm = input(f"Ban co chac muon xoa {student_list[i]['ten']}? (y/n): ")
            if confirm.lower() == 'y':
                student_list.pop(i)
                save_data()
                print('Da xoa')
            return
    print('Khong tim thay sinh vien')

def search_student():
    keyword = input('Nhap ten hoac Ma SV can tim: ').lower()
    results = [s for s in student_list if keyword in s['id'].lower() or keyword in s['ten'].lower()]
    if not results:
        print('Khong tim thay ket qua')
    else:
        print('-' * 95)
        print(f"{'Ma SV':<10} | {'Ho Ten':<20} | {'Toan':<6} | {'Ly':<6} | {'Hoa':<6} | {'TB':<6} | {'Xep Loai'}")
        print('-' * 95)
        for s in results:
            print(f"{s['id']:<10} | {s['ten']:<20} | {s['diem_toan']:<6} | {s['diem_ly']:<6} | {s['diem_hoa']:<6} | {s['diem_tb']:<6} | {s['xep_loai']}")
        print('-' * 95)

def sort_students():
    print('1. Diem TB giam dan')
    print('2. Ten tang dan (A-Z)')
    choice = input('Chon kieu sap xep: ')
    if choice == '1':
        student_list.sort(key=lambda x: x['diem_tb'], reverse=True)
        print('Da sap xep theo diem TB giam dan')
    elif choice == '2':
        student_list.sort(key=lambda x: x['ten'])
        print('Da sap xep theo ten A-Z')
    else:
        print('Lua chon khong hop le')

def show_stats():
    stats = {'Gioi': 0, 'Kha': 0, 'TB': 0, 'Yeu': 0}
    for s in student_list:
        if s['xep_loai'] in stats:
            stats[s['xep_loai']] += 1
    print('Thong ke xep loai:')
    for k, v in stats.items():
        print(f'{k}: {v}')

def show_min_max():
    if not student_list:
        print('Danh sach trong')
        return
    max_score = max(student_list, key=lambda x: x['diem_tb'])['diem_tb']
    min_score = min(student_list, key=lambda x: x['diem_tb'])['diem_tb']
    
    print(f'Sinh vien co diem TB cao nhat ({max_score}):')
    for s in student_list:
        if s['diem_tb'] == max_score:
            print(f"- {s['ten']} (Ma: {s['id']})")
            
    print(f'Sinh vien co diem TB thap nhat ({min_score}):')
    for s in student_list:
        if s['diem_tb'] == min_score:
            print(f"- {s['ten']} (Ma: {s['id']})")

def run_menu():
    load_data()
    while True:
        print('\n--- HE THONG QUAN LY SINH VIEN ---')
        print('1. Hien thi danh sach sinh vien')
        print('2. Them moi sinh vien')
        print('3. Cap nhat thong tin sinh vien')
        print('4. Xoa sinh vien')
        print('5. Tim kiem sinh vien')
        print('6. Sap xep danh sach')
        print('7. Thong ke diem TB')
        print('8. Sinh vien co diem TB cao nhat / thap nhat')
        print('9. Thoat')
        
        choice = input('Chon chuc nang (1-9): ')
        
        if choice == '1':
            display_students()
        elif choice == '2':
            add_student()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            search_student()
        elif choice == '6':
            sort_students()
        elif choice == '7':
            show_stats()
        elif choice == '8':
            show_min_max()
        elif choice == '9':
            print('Ket thuc chuong trinh')
            break
        else:
            print('Lua chon khong hop le')

if __name__ == '__main__':
    run_menu()