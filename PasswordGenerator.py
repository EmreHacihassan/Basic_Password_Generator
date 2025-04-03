import random
import string
import pyperclip
import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog, ttk


# 📌 Şifre Üretme Fonksiyonu
def generate_password(length=12, use_special_chars=True):
    """Belirtilen uzunlukta ve özel karakter içeren rastgele bir şifre üretir."""
    try:
        length = int(length)  # Spinbox'tan gelen değeri tam sayıya çevir
        if length < 6:
            messagebox.showwarning("Uyarı", "Şifre uzunluğu en az 6 olmalıdır!")
            return ""
    except ValueError:
        messagebox.showerror("Hata", "Geçersiz uzunluk girdisi!")
        return ""

    characters = string.ascii_letters + string.digits
    if use_special_chars:
        characters += string.punctuation  # Özel karakterleri ekle

    if length > len(characters):
        messagebox.showerror("Hata", "Şifre uzunluğu çok büyük! Lütfen daha küçük bir değer girin.")
        return ""

    return ''.join(random.sample(characters, length))


# 📌 Şifreyi Panoya Kopyalama
def copy_to_clipboard(password):
    """Şifreyi panoya kopyalar ve kullanıcıya bilgi verir."""
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Başarı", "Şifre panoya kopyalandı!")


# 📌 Şifreyi Dosyaya Kaydetme
def save_password_to_file(password):
    """Şifreyi kullanıcının seçtiği bir dosyaya kaydeder."""
    if not password:
        messagebox.showwarning("Uyarı", "Kaydedilecek bir şifre yok!")
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All Files", "*.*")],
        title="Şifreyi Kaydet"
    )

    if file_path:
        with open(file_path, "a") as file:
            file.write(password + "\n")
        messagebox.showinfo("Başarı", f"Şifre başarıyla kaydedildi!\n{file_path}")


# 📌 Arayüzü Oluşturma
def create_gui():
    """Şifre üretici için grafiksel kullanıcı arayüzü (GUI) oluşturur."""
    root = tk.Tk()
    root.title("🔐 Gelişmiş Şifre Üretici")
    root.geometry("400x300")
    root.resizable(False, False)

    # Tema Stili
    style = ttk.Style()
    style.theme_use("clam")

    # Şifre uzunluğu etiketi
    length_label = ttk.Label(root, text="Şifre Uzunluğu:", font=("Arial", 12))
    length_label.pack(pady=5)

    # Uzunluk Spinbox
    length_spinbox = ttk.Spinbox(root, from_=6, to=50, width=5)
    length_spinbox.pack(pady=5)
    length_spinbox.set(12)  # Varsayılan 12 karakter

    # Özel karakter kullanım seçeneği
    use_special_chars_var = tk.BooleanVar(value=True)
    use_special_chars_checkbox = ttk.Checkbutton(root, text="Özel Karakter Kullan", variable=use_special_chars_var)
    use_special_chars_checkbox.pack(pady=5)

    # Sonuç göstermek için Entry kutusu (Salt okunur)
    password_entry = ttk.Entry(root, font=("Arial", 12), justify="center", state="readonly", width=30)
    password_entry.pack(pady=5)

    # Şifre üret butonu
    def generate_and_display():
        password = generate_password(length_spinbox.get(), use_special_chars_var.get())
        if password:
            password_entry.config(state="normal")
            password_entry.delete(0, tk.END)
            password_entry.insert(0, password)
            password_entry.config(state="readonly")

    generate_button = ttk.Button(root, text="🔄 Şifre Üret", command=generate_and_display)
    generate_button.pack(pady=5)

    # Panoya kopyalama butonu
    copy_button = ttk.Button(root, text="📋 Panoya Kopyala", command=lambda: copy_to_clipboard(password_entry.get()))
    copy_button.pack(pady=5)

    # Dosyaya kaydetme butonu
    save_button = ttk.Button(root, text="💾 Dosyaya Kaydet", command=lambda: save_password_to_file(password_entry.get()))
    save_button.pack(pady=5)

    root.mainloop()


# 🚀 Programı Çalıştır
if __name__ == "__main__":
    create_gui()







