import tkinter as tk
import ttkbootstrap as ttk
import customtkinter as ctk


class App(ttk.Window):
	def __init__(self):
		super().__init__(self , themename = "darkly")
		
		self.columnconfigure(0, weight = 1, uniform= "a")
		self.rowconfigure((0,1,2,3),weight=1, uniform="a")
		self.geometry("400x400")
		self.minsize(400,400)
		
		self.height_int = tk.IntVar(value=184)
		self.weight_var = tk.DoubleVar(value=50.0)
		self.bmi_text = tk.StringVar()
		self.height_text = tk.StringVar(value = self.height_int.get()/100)
		self.metric_bool = tk.BooleanVar(value = True)
		self.update_bmi()
		
		self.height_int.trace("w", self.update_bmi)
		self.weight_var.trace("w", self.update_bmi)
		#self.metric_bool.trace("w", self.change_unit)
		
		
		ResultLabel(self, self.bmi_text)
		InputFrame(self, self.weight_var, self.metric_bool)
		self.height_input = HeightInput(self, self.height_int, self.height_text, self.metric_bool)
		UnitSwitcher(self, self.metric_bool)
		
		self.mainloop()
		
	def update_bmi(self, *args):
		height_meter = self.height_int.get() / 100
		weight = self.weight_var.get()
		bmi = round(weight / (height_meter**2), 2)
		
		self.bmi_text.set(bmi)
		
class ResultLabel(ttk.Label):
	def __init__(self , parent, result):
		super().__init__(master = parent, textvariable = result,anchor = "center", font=("Calibri", 45, "bold"), bootstyle="success")
		self.grid(row = 0, column = 0, rowspan =2, sticky = "nsew")

class InputFrame(tk.Frame):
	def __init__(self , parent,  weight_value, metric_bool):
		super().__init__(master=parent )
		
		self.rowconfigure(0, weight=1)
		self.columnconfigure(0, weight=1)
		self.columnconfigure(1, weight=1)
		self.columnconfigure(2, weight=1)
		self.columnconfigure(3, weight=1)
		self.columnconfigure(4, weight=1)
		
		self.grid(row = 2, column =0, sticky ="nsew")
		self.weight = weight_value
		self.metric_bool = metric_bool
		
		# creating Widgets
		self.label = ttk.Label(self , text = f"{self.weight.get()}kg", anchor="center", font=("arial",20),)
		self.label.grid(row =0, column =2)
		
		minus_btn = ttk.Button(self , text = "-", bootstyle="success-outline",command=lambda: self.update_weight(-1))
		minus_btn.grid(row=0, column =0, sticky="ns", pady=20)
		small_minus_btn = ttk.Button(self , text = "-", bootstyle="success-outline",command=lambda:self.update_weight(-0.1))
		small_minus_btn.grid(row=0, column =1)
		plus_btn = ttk.Button(self , text = "+", bootstyle="success-outline", command=lambda: self.update_weight(1))
		plus_btn.grid(row=0, column =4, sticky="ns", pady=20)
		small_plus_btn = ttk.Button(self , text = "+", bootstyle="success-outline",command=lambda: self.update_weight(0.1))
		small_plus_btn.grid(row=0, column =3)
	
	def update_weight(self , value):
		if self.metric_bool.get():
			self.weight.set(round(self.weight.get() + value, 1))
			self.label.configure(text = f"{self.weight.get()}kg")
		else:
			pass

class HeightInput(tk.Frame):
	def __init__(self , parent,  height, height_text,  metric_bool):
		super().__init__(master=parent)
		self.grid(row=3, column =0, sticky ="nsew", padx=20)
		
		self.height = height
		self.metric_bool = metric_bool
		
		slider = ttk.Scale(self, bootstyle="success",from_=100, to= 250, variable=height, command=self.update_label)
		slider.pack(fill = "x", padx = 15, side="left", expand=True)
		self.output_label = ttk.Label(self , text=f"{height_text.get()}m", font=("arial",15))
		self.output_label.pack(side="left", padx=20, fill="x")
		
	def update_label(self , *args):
		if self.metric_bool.get():
			self.output_label.config(text =f"{self.height.get()/100:.2f}m")
		else:
			pass

class UnitSwitcher(ttk.Button):
	def __init__(self, parent, metric_bool):
		super().__init__(parent, text = "metric", bootstyle="success-outline")
		self.metric_bool = metric_bool
		self.place(relx=.88, rely=.06, anchor= "center")

if __name__ == "__main__":
	App()