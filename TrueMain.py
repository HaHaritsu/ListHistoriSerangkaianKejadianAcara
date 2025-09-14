
print("-"*100)
print("Harits_(2509116048)_SistemInformasiB")
print("ListHistoriSerangkaianKejadian/Acara")
print("-"*100)


histori = [
    {"tahun": 2020, "data": ["Art Jog", "Java Jazz", "Pacu Jalur"]},
    {"tahun": 2021, "data": ["COVID-19", "Idemitsu Asian Talent Cup"]},
    {"tahun": 2022, "data": ["KTT G20", "WBSK"]}
]
menu = ["Histori Acara", "Tambah Acara", "Ubah Acara", "Hapus Acara"]

while True:
    print("===Main Menu===")
    for i, item in enumerate(menu):
        print(f"[{i}] {item}")
    print("[9] Tutup")
    
    opsi = input("\n>>> ")
    
    if opsi == "9":
        print("Program Selesai >w<")
        break
    
    elif opsi.isdigit() and int(opsi) in range(len(menu)):
        opsi = int(opsi)
        
        #SeeEvent
        if opsi == 0:
            print("---List Histori Acara---")
            for i, h in enumerate(histori):
                print(f"[{i}] ({h['tahun']}) {', '.join(h['data'])}")
        
        #AddEvevnt
        elif opsi == 1:
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
                print("unknown problem")
        
        #UpdateEvent
        elif opsi == 2:
            print("Pilih tahun yang tersedia:")
            for i, h in enumerate(histori):
                print(f"[{i}] {h['tahun']}")
            
            opsi2 = input("Masukkan nomor tahun: ")
            if opsi2.isdigit() and int(opsi2) in range(len(histori)):
                opsi2 = int(opsi2)
                
                #ShowEventOnExactYear
                print(f"--- Daftar Acara Tahun {histori[opsi2]['tahun']} ---")
                for j, acara in enumerate(histori[opsi2]["data"]):
                    print(f"[{j}] {acara}")
                
                #ChangingTheEvent
                opsi21 = input("Masukkan nomor acara yang ingin diubah: ")
                if opsi21.isdigit() and int(opsi21) in range(len(histori[opsi2]["data"])):
                    opsi21 = int(opsi21)
                    ubah = input("Masukkan nama acara baru: ").strip()
                    if ubah:
                        histori[opsi2]["data"][opsi21] = ubah
                        print("Acara berhasil diubah!")
                    else:
                        print("unknown problme")
                else:
                    print("unknown problem")
            else:
                print("unknown problem")
        
        #RemoveEvent
        elif opsi == 3:
            print("Pilih tahun yang tersedia:")
            for i, h in enumerate(histori):
                print(f"[{i}] {h['tahun']}")
            
            opsi3 = input("Masukkan nomor tahun: ")
            if opsi3.isdigit() and int(opsi3) in range(len(histori)):
                opsi3 = int(opsi3)
                
                #ShowEventOnExactYear
                print(f"--- Daftar Acara Tahun {histori[opsi3]['tahun']} ---")
                for j, acara in enumerate(histori[opsi3]["data"]):
                    print(f"[{j}] {acara}")
                
                #DeletingTheEvent
                hapus = input("Masukkan nomor acara yang ingin dihapus: ")
                if hapus.isdigit() and int(hapus) in range(len(histori[opsi3]["data"])):
                    hapus = int(hapus)
                    terhapus = histori[opsi3]["data"].pop(hapus)
                    print(f"Acara '{terhapus}' terhapus")
                else:
                    print("unknown problem")
            else:
                print("unknown problem")
        
        else:
            print("unknown problem")
    else:
        print("unknown problem")