from tkinter import*
import random

root=Tk()
root.title('Pasword Genrator')
root.geometry('500x500')

label=Label(root)

array_3d=[[[1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ],["Tomoe Sharin","Tomoe Sharin"],["gan","gan","gan","gan","gan","gan","gan","gan" ]]]
print(array_3d[0][2][3])


def password():
    random_number1=random.randint(0,5)
    random_number2=random.randint(0,1)
    random_number3=random.randint(0,7)
    
    letter1=str(array_3d[0][0][random_number1])
    letter2=(array_3d[0][1][random_number2])
    letter3=(array_3d[0][2][random_number3])   
    label["text"]=letter1+""+letter2+""+letter3
    
btn=Button(root,text="GENERATE PASSWORD",command=password)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)


label.place(relx=0.5,rely=0.4,anchor=CENTER)

root.mainloop()