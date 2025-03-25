#Nama : Neisha Qonita Nurul Izzah
#NIM : 242410101007

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Membagi array menjadi dua bagian
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)  # Rekursif untuk bagian kiri
        merge_sort(right_half)  # Rekursif untuk bagian kanan

        i = j = k = 0

        # Menggabungkan kembali dua bagian yang telah disorting
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Menambahkan elemen yang tersisa dari bagian kiri (jika ada)
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Menambahkan elemen yang tersisa dari bagian kanan (jika ada)
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Contoh penggunaan
data = [55, 32, 29, 17, 27, 14, 78]
merge_sort(data)
print("Data setelah diurutkan:", data)
