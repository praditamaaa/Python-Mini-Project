# Program untuk menambahkan To Do List

end = False
file = open("todo.txt", "a")

while (not end):

    id = str(input("\nMasukkan Id: "))
    todo = str(input("Masukkan kegiatan: "))
    jam = str(input("Masukkan jam: "))

    file.write(id + " ")
    file.write(todo + " ")
    file.write(jam + " ")
    file.write("\n")

    out = int(input("\nTambah lagi? Ketik 1 jika ya: "))
    end = True

    if out == 1:
        end = False

file.close()
   
