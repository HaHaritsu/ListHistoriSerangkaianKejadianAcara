print("| [[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]] |")
print("| Harits_(2509116048)_SistemInformasiB |")
print("| ListHistoriSerangkaianKejadian/Acara |")
print("| [[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]] |")
print("\n")


histori = [
    {"tahun": 2020, "data": ["Art Jog", "Java Jazz", "Pacu Jalur"]},
    {"tahun": 2021, "data": ["COVID-19", "Idemitsu Asian Talent Cup"]},
    {"tahun": 2022, "data": ["KTT G20", "WBSK"]}
]

mod_menu = ["Tutup Program", "Histori Acara", "Tambah Acara", "Ubah Acara", "Hapus Acara"]
menu_user = ["Tutup Program", "Histori Acara"]

akun = [
    {"username": "admin", "password": "admin", "role": "admin"},
    {"username": "test", "password": "1234", "role": "admin"},
    {"username": "user", "password": "user1", "role": "user"}
]


def login():
    try:
        while True:
            print("=================")
            print("|     Login     |")
            print("=================")
            username = input("Username: ")
            password = input("Password: ")
            
            user = next((u for u in akun if u["username"] == username), None)
            
            if not user:
                print("Username tidak ditemukan")
                continue
        
            if password == user["password"]:
                print("==================")
                print("| Login berhasil |")
                print("==================")
                print(f"Role anda: {user['role']}")
                print("\n\n")
                return user["role"]
            else:
                print("==================")
                print("| Login gagal |")
                print("==================")
        return None
    
    except EOFError:
        print("Input tidak valid: (^Z)")
        exit()
    except KeyboardInterrupt:
        print("\nProgram dihentikan paksa")
        exit()
    except Exception as e:
        print(f"Unknown Error {e}")
        return None


def view():
    try:
        print("---List Histori Acara---")
        for i, h in enumerate(histori):
            print(f"[{i}] ({h['tahun']}) {', '.join(h['data'])}")
    except EOFError:
        print("Input tidak valid: (^Z)")
        exit()
    except KeyboardInterrupt:
        print("\nProgram dihentikan paksa")
        exit()
    except Exception as e:
        print(f"Unknown Error {e}")


def add():
    try:
        print("Pilih tahun yang tersedia:")
        for i, h in enumerate(histori):
            print(f"[{i}] {h['tahun']}")
        
        opsi1 = input("Masukkan nomor tahun: ")
        if opsi1.isdigit() and int(opsi1) in range(len(histori)):
            opsi1 = int(opsi1)
            tambah = input("Masukkan acara baru (pisahkan dengan koma jika lebih dari 1): ")
            daftar = [x.strip() for x in tambah.split(",") if x.strip()]
            histori[opsi1]["data"].extend(daftar)
            print("Acara ditambahkan!")
        else:
            print("Input harus berupa angka")
    except EOFError:
        print("Input tidak valid: (^Z)")
        exit()
    except KeyboardInterrupt:
        print("\nProgram dihentikan paksa")
        exit()
    except Exception as e:
        print(f"Unknown Error {e}")


def update():
    try:
        print("Pilih tahun yang tersedia:")
        for i, h in enumerate(histori):
            print(f"[{i}] {h['tahun']}")
            
        opsi2 = input("Masukkan nomor tahun: ")
        if opsi2.isdigit() and int(opsi2) in range(len(histori)):
            opsi2 = int(opsi2)
                    
            # ShowEventOnExactYear
            print(f"--- Daftar Acara Tahun {histori[opsi2]['tahun']} ---")
            for j, acara in enumerate(histori[opsi2]["data"]):
                print(f"[{j}] {acara}")
                    
            # ChangingTheEvent
            opsi21 = input("Masukkan nomor acara yang ingin diubah: ")
            if opsi21.isdigit() and int(opsi21) in range(len(histori[opsi2]["data"])):  
                opsi21 = int(opsi21)
                ubah = input("Masukkan nama acara baru: ").strip()
                if ubah:
                    histori[opsi2]["data"][opsi21] = ubah
                    print("Acara berhasil diubah!")
                else:
                    print("Input kosong tidak valid")
            else:
                print("Input harus berupa angka")
        else:
            print("Input harus berupa angka")
    except EOFError:
        print("Input tidak valid: (^Z)")
        exit()
    except KeyboardInterrupt:
        print("\nProgram dihentikan paksa")
        exit()
    except Exception as e:
        print(f"Unknown Error {e}")
        

def remove():
    try:
        print("Pilih tahun yang tersedia:")
        for i, h in enumerate(histori):
            print(f"[{i}] {h['tahun']}")

        opsi3 = input("Masukkan nomor tahun: ")
        if opsi3.isdigit() and int(opsi3) in range(len(histori)):
            opsi3 = int(opsi3)

            # ShowEventOnExactYear
            print(f"--- Daftar Acara Tahun {histori[opsi3]['tahun']} ---")
            for j, acara in enumerate(histori[opsi3]["data"]):
                print(f"[{j}] {acara}")

            # DeletingTheEvent
            hapus = input("Masukkan nomor acara yang ingin dihapus: ")
            if hapus.isdigit() and int(hapus) in range(len(histori[opsi3]["data"])):  
                hapus = int(hapus)
                terhapus = histori[opsi3]["data"].pop(hapus)
                print(f"Acara '{terhapus}' terhapus")
            else:
                print("Input harus berupa angka")
        else:
            print("Input harus berupa angka")
    except EOFError:
        print("Input tidak valid: (^Z)")
        exit()
    except KeyboardInterrupt:
        print("\nProgram dihentikan paksa")
        exit()
    except Exception as e:
        print(f"Unknown Error {e}")


role = login()
if role:
    try:
        while True:
            #menutest
            if role == "user":
                current = menu_user
            else:
                current = mod_menu

            print("===Main Menu===")
            for i, item in enumerate(current):
                print(f"[{i}] {item}")

            opsi = input("\n>>> ")

            if not opsi.isdigit():
                print("Input harus berupa angka")
                continue

            opsi = int(opsi)

            if opsi == 0:
                print("Program Selesai >w<")
                break
            elif opsi == 1:
                view()
            elif role != "user":  #onlyadmin
                if opsi == 2:
                    add()
                elif opsi == 3:
                    update()
                elif opsi == 4:
                    remove()
                else:
                    print("Menu tidak tersedia")
            else:
                print("Menu tidak tersedia")

    except EOFError:
        print("Input tidak valid: (^Z)")
    except KeyboardInterrupt:
        print("\nProgram dihentikan paksa")
    except Exception as e:
        print(f"Unknown Error {e}")
