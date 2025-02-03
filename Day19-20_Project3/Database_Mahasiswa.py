# Database Mahasiswa Project with Python
# Day 19 - 20 KelasBagus
# Code by Nadhif Rif'at Rasendriya

class databaseMahasiswa:
    def __init__(self, nama_file, nim_file):
        self.nama_file = nama_file
        self.nim_file = nim_file

        open(self.nama_file, 'a').close()
        open(self.nim_file, 'a').close()

    def add_student(self, nama, nim):
        with open(self.nim_file, 'r') as nim_file:
            nim_list = [line.strip() for line in nim_file.readlines()]

        if nim in nim_list:
            print(f"Error: Mahasiswa dengan NIM {nim} sudah ada!\n")
            return 
        
        with open(self.nama_file, 'a') as nama_file, open(self.nim_file, 'a') as nim_file:
            nama_file.write(nama + "\n")
            nim_file.write(nim + "\n")

        print(f"Mahasiswa {nama} (NIM: {nim}) sudah ditambah!\n")

    def show_all_students(self):
        with open(self.nama_file, 'r') as nama_file, open(self.nim_file, 'r') as nim_file:
            nama_list, nim_list = nama_file.readlines(), nim_file.readlines()

        if not nama_list or not nim_list or len(nama_list) != len(nim_list):
            print('Data tidak lengkap atau tidak ada!')
            return
        
        print('List of Students:\n')
        print(f"{'No.':<5}{'Nama':<20}{'NIM':<15}")
        print("-" * 40)
        
        [print(f"{i + 1:<5}{nama.strip():<20}{nim.strip():<15}") for i, (nama, nim) in enumerate(zip(nama_list, nim_list))]

    def delete_student(self, nim):
        students = self.student_to_dictionary()
        new_students = [student for student in students if student["NIM"] != nim]

        if len(new_students) < len(students):
            self._save_students(new_students)
            print(" ")
            print(f"Mahasiswa dengan NIM {nim} berhasil dihapus!")
        else:
            print("Student with the specified NIM not found.")

    def student_to_dictionary(self):
        with open(self.nama_file, 'r') as nama_file, open(self.nim_file, 'r') as nim_file:
            return [{"Nama": nama.strip(), "NIM": nim.strip()} for nama, nim in zip(nama_file.readlines(), nim_file.readlines())]

    def search_student_by_nim(self, nim):
        students = self.student_to_dictionary()
        student = next((s for s in students if s["NIM"] == nim), None)
        if student:
            print(f"Student Found: Nama: {student['Nama']}, NIM: {student['NIM']}")
            return student
        print("Student with the specified NIM not found.")
        return None

    def _save_students(self, students):
        with open(self.nama_file, 'w') as nama_file, open(self.nim_file, 'w') as nim_file:
            [nama_file.write(student["Nama"] + "\n") for student in students]
            [nim_file.write(student["NIM"] + "\n") for student in students]

    def update_student(self, old_nim, new_nama=None, new_nim=None):
        students = self.student_to_dictionary()
        for student in students:
            if student["NIM"] == old_nim:
                if new_nama:
                    student["Nama"] = new_nama
                if new_nim:
                    student["NIM"] = new_nim
                self._save_students(students)
                print("Student updated successfully!")
                return
        print("Student with the specified NIM not found.")

# CRUD Mahasiswa

# Eksekusi Program
db = databaseMahasiswa(r'Day19-20_Project3\nama.txt', r'Day19-20_Project3\nim.txt')
db.show_all_students()

db.add_student('Nadhif', '235150201111074') # Tambah 1 mahasiswa ke data
db.add_student('Nadhif2', '245150211116418')
db.add_student('Nadhif3', '245150201116588')
db.show_all_students() # Show mahasiswa yang sudah ditambahkan

db.delete_student('245150201116588') # Hapus mahasiswa pada suatu nim
db.show_all_students() # Show ulang hasil akhir
