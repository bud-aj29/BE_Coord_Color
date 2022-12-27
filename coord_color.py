#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.colorchooser import askcolor
import assets.manifest_file, assets.folders_file, assets.hud_file, assets.bg_image_file, assets.pack_icon_file, assets.container_file
from assets import global_var

class GuiApp:
    def __init__(self, master=None):
        # build ui
        toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        self.img_dataassets_global_var = tk.PhotoImage(
            data=assets.global_var.gui_base64)
        toplevel1.configure(height=200, width=200)
        toplevel1.iconphoto(True, self.img_dataassets_global_var)
        toplevel1.title(global_var.pack_name)
        self.text_frame0 = ttk.Frame(toplevel1)
        self.text_frame0.configure(height=200, relief="ridge", width=200)
        self.text_label0 = ttk.Label(self.text_frame0)
        self.text_label0.configure(text='Text Color')
        self.text_label0.grid(
            column=0,
            columnspan=3,
            padx=5,
            pady=5,
            row=0,
            sticky="ew")
        self.text_label1 = ttk.Label(self.text_frame0)
        self.text_label1.configure(text='Hex')
        self.text_label1.grid(column=0, padx="5 0", pady=5, row=1, sticky="e")
        self.text_entry0 = ttk.Entry(self.text_frame0)
        self.text_entry0.grid(column=1, padx="0 5", pady=5, row=1, sticky="w")
        self.text_button0 = ttk.Button(self.text_frame0)
        self.text_button0.configure(text='pick')
        self.text_button0.grid(column=2, padx=5, pady=5, row=1, sticky="w")
        self.text_button0.configure(command=self.choose_text_color)
        self.text_frame0.grid(
            column=0,
            columnspan=3,
            padx=5,
            pady=5,
            row=0,
            sticky="ew")
        self.background_frame0 = ttk.Frame(toplevel1)
        self.background_frame0.configure(height=200, relief="ridge", width=200)
        self.background_label0 = ttk.Label(self.background_frame0)
        self.background_label0.configure(text='Background Color')
        self.background_label0.grid(
            column=0,
            columnspan=3,
            padx=5,
            pady=5,
            row=0,
            sticky="ew")
        self.background_label1 = ttk.Label(self.background_frame0)
        self.background_label1.configure(text='Hex')
        self.background_label1.grid(
            column=0, padx="5 0", pady=5, row=1, sticky="e")
        self.background_entry0 = ttk.Entry(self.background_frame0)
        self.background_entry0.grid(
            column=1, padx="0 5", pady=5, row=1, sticky="w")
        self.background_button0 = ttk.Button(self.background_frame0)
        self.background_button0.configure(text='pick')
        self.background_button0.grid(
            column=2, padx=5, pady=5, row=1, sticky="w")
        self.background_button0.configure(command=self.choose_background_color)
        self.background_scale0 = tk.Scale(self.background_frame0)
        self.alpha_var = tk.StringVar()
        self.background_scale0.configure(
            from_=0.0,
            label='Alpha (default=0.7)',
            orient="horizontal",
            relief="groove",
            resolution=0.1,
            to=1.0,
            variable=self.alpha_var)
        self.background_scale0.grid(
            column=0,
            columnspan=3,
            padx=5,
            pady=5,
            row=3,
            sticky="ew")
        self.background_frame0.grid(
            column=0,
            columnspan=3,
            padx=5,
            pady=5,
            row=1,
            sticky="ew")
        self.preview_frame0 = ttk.Frame(toplevel1)
        self.preview_frame0.configure(height=200, relief="ridge", width=200)
        self.preview_label0 = ttk.Label(self.preview_frame0)
        self.preview_label0.configure(text='Preview (color only)')
        self.preview_label0.grid(
            column=0,
            columnspan=3,
            padx=5,
            pady=5,
            row=0,
            sticky="ew")
        self.preview_label1 = ttk.Label(self.preview_frame0)
        self.preview_label1.configure(
            anchor="center",
            font="{Arial} 18 {}",
            text='Aa Bb Cc',
            width=17)
        self.preview_label1.grid(
            column=0,
            columnspan=3,
            padx="10 0",
            pady=5,
            row=1,
            sticky="ew")
        self.preview_frame0.grid(
            column=0,
            columnspan=3,
            padx=5,
            pady=5,
            row=2,
            sticky="ew")
        self.font_frame0 = ttk.Frame(toplevel1)
        self.font_frame0.configure(height=200, relief="ridge", width=200)
        self.font_label0 = ttk.Label(self.font_frame0)
        self.font_label0.configure(text='Font')
        self.font_label0.grid(
            column=0,
            columnspan=3,
            padx=5,
            pady=5,
            row=0,
            sticky="ew")
        self.font_label1 = ttk.Label(self.font_frame0)
        self.img_dataassets_global_var = tk.PhotoImage(
            data=assets.global_var.ui_fonts_base64)
        self.font_label1.configure(
            anchor="center",
            image=self.img_dataassets_global_var)
        self.font_label1.grid(
            column=0,
            columnspan=3,
            padx=50,
            pady=5,
            row=2,
            sticky="ew")
        self.font_radio0 = tk.Radiobutton(self.font_frame0)
        self.font_var = tk.StringVar(value='default')
        self.font_radio0.configure(value="default", variable=self.font_var)
        self.font_radio0.grid(column=0, row=1, sticky="e")
        self.font_radio1 = tk.Radiobutton(self.font_frame0)
        self.font_radio1.configure(value="smooth", variable=self.font_var)
        self.font_radio1.grid(column=1, row=1)
        self.font_radio2 = tk.Radiobutton(self.font_frame0)
        self.font_radio2.configure(
            value="MinecraftTen",
            variable=self.font_var)
        self.font_radio2.grid(column=2, row=1, sticky="w")
        self.font_frame0.grid(
            column=0,
            columnspan=3,
            padx=5,
            pady=5,
            row=3,
            sticky="ew")
        self.shadow_frame0 = ttk.Frame(toplevel1)
        self.shadow_frame0.configure(height=200, relief="ridge", width=200)
        self.shadow_label0 = ttk.Label(self.shadow_frame0)
        self.shadow_label0.configure(text='Shadow')
        self.shadow_label0.grid(
            column=0,
            columnspan=3,
            padx=5,
            pady=5,
            row=0,
            sticky="ew")
        self.shadow_check0 = tk.Checkbutton(self.shadow_frame0)
        self.shadow_var = tk.BooleanVar()
        self.shadow_check0.configure(text='On/Off', variable=self.shadow_var)
        self.shadow_check0.grid(
            column=0,
            columnspan=3,
            padx=5,
            pady="0 5",
            row=1,
            sticky="w")
        self.shadow_frame0.grid(
            column=0,
            columnspan=3,
            padx=5,
            pady=5,
            row=4,
            sticky="ew")
        self.create_frame0 = ttk.Frame(toplevel1)
        self.create_frame0.configure(height=200, relief="ridge", width=200)
        self.create_button0 = ttk.Button(self.create_frame0)
        self.create_button0.configure(text='Create Pack', width=35)
        self.create_button0.grid(
            column=0,
            columnspan=3,
            padx="12 0",
            pady=5,
            row=0,
            sticky="ew")
        self.create_button0.configure(command=self.create_pack)
        self.create_frame0.grid(
            column=0,
            columnspan=3,
            padx=5,
            pady=5,
            row=5,
            sticky="ew")

        # Main widget
        self.mainwindow = toplevel1

        #set default control states
        self.background_scale0.set(0.7)
        self.font_radio0.select()
        self.shadow_check0.select()

        #change on entry values
        def txt_on_entry(txt_var):
            txt_var_content= txt_var.get()
            self.preview_label1.configure(foreground=txt_var_content)
        def bg_on_entry(bg_var):
            bg_var_content= bg_var.get()
            self.preview_label1.configure(background=bg_var_content)
        txt_var = tk.StringVar()
        txt_var.trace("w", lambda name, index,mode, txt_var=txt_var: txt_on_entry(txt_var))
        self.text_entry0.configure(textvariable=txt_var)
        self.text_entry0.insert("0", "#ffffff")
        bg_var = tk.StringVar()
        bg_var.trace("w", lambda name, index,mode, bg_var=bg_var: bg_on_entry(bg_var))
        self.background_entry0.configure(textvariable=bg_var)
        self.background_entry0.insert("0", "#000000")

    def run(self):
        self.mainwindow.mainloop()

    def choose_text_color(self):
        txt_color = askcolor(title = "Text_Color")
        self.text_entry0.delete("0", "end")
        self.text_entry0.insert("0", txt_color[1])

    def choose_background_color(self):
        bg_color = askcolor(title = "Background_Color")
        self.background_entry0.delete("0", "end")
        self.background_entry0.insert("0", bg_color[1])

    def create_pack(self):
        assets.folders_file.folders_class.folders_method(self)
        assets.manifest_file.manifest_class.manifest_method(self)
        txt_out = self.text_entry0.get()
        alpha_out = self.background_scale0.get()
        font_out = self.font_var.get()
        shadow_out = self.shadow_var.get()
        assets.hud_file.hud_class.hud_method(txt_out,alpha_out,font_out,shadow_out)
        bg_out = self.background_entry0.get()
        assets.bg_image_file.bg_image_class.bg_image_method(bg_out)
        assets.pack_icon_file.pack_icon_class.pack_icon_method(bg_out,txt_out)
        assets.container_file.container_class.container_method(self)

if __name__ == "__main__":
    app = GuiApp()
    app.run()