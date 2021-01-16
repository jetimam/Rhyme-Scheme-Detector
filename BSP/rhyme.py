import tkinter as tk
import PyPDF2
from tkinter import scrolledtext
import tkinter.font as TkFont
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
import main_gui

#Main frame
root = tk.Tk()
root.title('Rhyme Scheme Detector')
root.configure(bg='slate gray')

#Logo
logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo, borderwidth=0, highlightthickness=0)
logo_label.image = logo
logo_label.grid(columnspan=3,column=0,row=0)

#Instructions
instructions = tk.Label(root, text='Please choose which tool you wish to use after you have entered the text.', font='Arial', bg='slate gray', fg='black')
instructions.grid(columnspan=3, column=0, row=1, pady=5)

#Button Functionality
def rhyme_sorter():
    rhyme_sort = main_gui.rhyme_scheme(input_text.get(1.0, tk.END))

    output_text.config(state='normal')

    output_text.delete(1.0, tk.END)

    for key,value in rhyme_sort.items():
        result = key + ': ' + ', '.join(value) + '\n'
        output_text.insert(tk.INSERT, result)
    
    output_text.config(state='disabled')

def rhyme_dict():
    output_text.config(state='normal')

    if ' ' in input_text.get(1.0, tk.END):
        output_text.delete(1.0, tk.END)
        
        output_text.insert(tk.INSERT, 'Enter only one word if you wish to use the Rhyme Dictionary.')
    else:
          
        word = input_text.get(1.0, tk.END).split('\n')[0]

        rhymes_dict = main_gui.give_rhyme(word)

        output_text.delete(1.0, tk.END)

        for key,value in rhymes_dict.items():
            result = str(key) + ': ' + value + '\n'
            output_text.insert(tk.INSERT, result)
        
        output_text.config(state='disabled')

def open_file():
    file = askopenfile(parent=root, mode='rb', title='Choose a file', filetype=[('Pdf file', '*.pdf')])
    
    if file:
        pdf_read = PyPDF2.PdfFileReader(file)
        page_count = pdf_read.getNumPages()

        for i in range(page_count):
            page = pdf_read.getPage(i)
            content = page.getContents()
            input_text.delete(1.0, tk.END)
            input_text.insert(1.0, content)

#Buttons
text1 = tk.StringVar()
text2 = tk.StringVar()
text3 = tk.StringVar()
rhymeSort_button = tk.Button(root, textvariable=text1, height=1, width=19, command=rhyme_sorter, font=('Arial', '10'))
rhymeGive_button = tk.Button(root, textvariable=text2, height=1, width=16, command=rhyme_dict, font=('Arial', '10'))
openFile_button = tk.Button(root, textvariable=text3, height=1, width=10, command=open_file, font=('Arial', '10'))
text1.set('Rhyme Scheme Sorter')
text2.set('Rhyme Dictionary')
text3.set('Open PDF')
rhymeSort_button.grid(columnspan=3, column=0, row=2, pady=5)
rhymeGive_button.grid(columnspan=3, column=0, row=3)
openFile_button.grid(columnspan=2, column=2, row=2)


#Input Box
input_text = scrolledtext.ScrolledText(root, height=20, width=45, wrap='word', font=('Arial', '10'))
input_text.grid(column=0, row=4, padx=15, pady=15)

#Output Box
output_text = scrolledtext.ScrolledText(root, height=20, width=45, wrap='word', font=('Arial', '10'))
output_text.config(state='disabled')
output_text.grid(column=2, row=4, padx=15, pady=15)

root.mainloop()