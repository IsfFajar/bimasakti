import tkinter as tk
from tkinter import scrolledtext
import openai
import tkinter.messagebox as mbox

openai.api_key = "your-API_key"
model_engine = 'text-davinci-003'

def generate_text():
    prompt = prompt_entry.get()
    if 'exit' in prompt or 'quit' in prompt:
        root.destroy()
    else:
        completion = openai.Completion.create(engine = model_engine, 
                                          prompt = prompt, 
                                          max_tokens = 1024, 
                                          n = 1, 
                                          stop = None, 
                                          temperature = 0.5)
    response = completion.choices[0].text
    output_text.delete('1.0',tk.END)
    output_text.insert(tk.END, response)

# create program for 'clear' button
def clear_text():
    prompt_entry.delete(0, tk.END)
    output_text.delete('1.0', tk.END)

# create program for 'copy' button
def copy_text():
    text = output_text.get('1.0', tk.END)
    root.clipboard_clear()
    root.clipboard_append(text)
    mbox.showinfo('Copied', 'Generated text has been copied to clipboard!')

# create main window
root = tk.Tk()
root.title('OpenAI Text Generation')

# create frame inside the window
frame = tk.Frame(root)
frame.pack()

# create the input prompt label and entry field inside a label frame
enter_prompt_frame = tk.LabelFrame(frame, text='Enter prompt')
enter_prompt_frame.grid(row=0, column=0, sticky="news", padx=20, pady=10)

prompt_label = tk.Label(enter_prompt_frame, text = 'Insert question:')
prompt_label.grid(row=0, column=0, padx=5, pady=5)
prompt_entry = tk.Entry(enter_prompt_frame, width =70)
prompt_entry.grid(row=0, column=1, padx=5, pady=5)

# create the generate button
generate_button = tk.Button(enter_prompt_frame, text='Generate', command=generate_text)
generate_button.grid(row=1, column=1, padx=5, pady=5, sticky='E')

# create the clear button
clear_button = tk.Button(enter_prompt_frame, text='Clear', command=clear_text)
clear_button.grid(row=1, column=0, padx=5, pady=5, sticky='W')

# create the output label and text field inside a label frame
Generate_text_frame = tk.LabelFrame(frame, text="Generated text")
Generate_text_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

output_label = tk.Label(Generate_text_frame, text='Output:')
output_label.grid(row=2, column=0, padx=5, pady=5)

# create the output scolledtext
output_text = scrolledtext.ScrolledText(Generate_text_frame, height=50, 
                                        width=90, wrap= 'none')
output_text.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

# create copy button
copy_button = tk.Button(Generate_text_frame, text='Copy Text', command=copy_text)
copy_button.grid(row=3, column=1, padx=5, pady=5, sticky='E')

# start the main event loop
root.mainloop()
