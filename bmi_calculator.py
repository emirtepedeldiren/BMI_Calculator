from tkinter import *

bmi_window = Tk()
bmi_window.title("BMI Calculator")
bmi_window.minsize(width=400 , height=300)
bmi_window.config(padx=30 , pady=30 )

def calculate_bmi():

    w_input = weight_entry.get()
    h_input = height_entry.get()
    if w_input == "" or h_input == "" :
        m_label.config(text="Please enter value!" , fg="#4B1599")
        return
    try:
        w = float(w_input)
        h = float(h_input)

        sh = h/100
        nh = sh**2
        c_bmi = w/nh
        n_bmi = int(c_bmi*10)/10 #Kusürat_atıldıktan_sonraki bmi

        if n_bmi <= 18.5 :
            m_label.config(text=f"Your BMI is {n_bmi}. You are underweight. " , fg="Blue")

        elif 18.5 < n_bmi <= 24.9 :
            m_label.config(text=f"Your BMI is {n_bmi}. You are healthy :)" , fg="Green")

        elif 25 <= n_bmi <= 29.9 :
            m_label.config(text=f"Your BMI is {n_bmi}. You are overweight." , fg="Orange")
        elif 30 <= n_bmi <= 39.9 :
            m_label.config(text=f"Your BMI is {n_bmi}. You are obese!" , fg="Red")
        else:
            m_label.config(text=f"Your BMI is {n_bmi}. You are extremely obese !!" , fg="darkred")

    except ValueError:
        m_label.config(text="Enter a valid number!")


# UI SETTİNGS

#weight_settings
w_label = Label(text="Enter your weight(kg):" , font=("Arial" , 10 , "normal"))
w_label.pack()

weight_entry = Entry(bmi_window , width=15)
weight_entry.pack(pady=5)

#height_settings
h_label = Label(text="Enter your height(cm):" , font=("Arial" , 10 , "normal"))
h_label.pack(pady=(10,0))

height_entry = Entry(bmi_window , width=15)
height_entry.pack(pady=5)

#Calculate_button
c_button = Button(text="Calculate" , command=calculate_bmi)
c_button.pack(pady=20)

#message_label
m_label = Label(text="" , font =("Arial" , 11 , "bold"))
m_label.pack()


bmi_window.mainloop()


