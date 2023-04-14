import customtkinter as ctk

class GUI:
    def __init__(self, master):
        self.master = master
        self.directory_var = ctk.StringVar()
        
        # ウィンドウを作成
        self.window = ctk.Frame(self.master)
        self.window.pack(fill=ctk.BOTH, expand=True)

        # サイドバーを作成
        self.sidebar = ctk.Frame(self.window, width=200, background="white")
        self.sidebar.pack(side=ctk.LEFT, fill=ctk.Y)

        # メイン画面を作成
        self.main_frame = ctk.Frame(self.window)
        self.main_frame.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True)

        # ディレクトリ選択ボタンを作成
        self.directory_button = ctk.Button(self.sidebar, text="Select Directory")
        self.directory_button.pack(pady=10)

        # ディレクトリ選択テキストボックスを作成
        self.directory_entry = ctk.Entry(self.sidebar, textvariable=self.directory_var)
        self.directory_entry.pack(pady=10)

        # submitボタンを作成
        self.submit_button = ctk.Button(self.sidebar, text="Submit")
        self.submit_button.pack(pady=10)

        # テキスト表示エリアを作成
        self.text_area = ctk.Text(self.sidebar, height=20, width=30)
        self.text_area.pack(pady=10)

        # 画像表示エリアを作成
        self.image_area = ctk.Label(self.main_frame, background="white")
        self.image_area.pack(side=ctk.TOP, fill=ctk.BOTH, expand=True)

        # グラフ表示エリアを作成
        self.graph_area = ctk.Frame(self.main_frame, background="white")
        self.graph_area.pack(side=ctk.BOTTOM, fill=ctk.BOTH, expand=True)

#test
def test_gui():                    
    root = ctk.CTk()
    gui = GUI(root)
    root.mainloop()

if __name__ == "__main__":
    test_gui()

#test
