import tkinter as tk
from tkinter import ttk, messagebox

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python GUI App Base")
        self.root.geometry("400x300")

        # メインフレームの作成（余白設定）
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # ラベルの作成
        self.label = ttk.Label(self.main_frame, text="名前を入力してください:", font=("Arial", 10))
        self.label.pack(pady=5)

        # 入力ボックスの作成
        self.entry = ttk.Entry(self.main_frame, width=30)
        self.entry.pack(pady=5)

        # ボタンの作成
        self.button = ttk.Button(self.main_frame, text="実行", command=self.on_click)
        self.button.pack(pady=20)

    def on_click(self):
        name = self.entry.get()
        if name:
            messagebox.showinfo("メッセージ", f"こんにちは、{name}さん！")
        else:
            messagebox.showwarning("注意", "名前を入力してください。")

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
    