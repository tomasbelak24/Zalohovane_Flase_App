import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pandas as pd
from pathlib import Path

class CSV_PROCESSOR:

    file_path, save_path = None, None
    log = ''

    def __init__(self, title, process_method):
        self.window = tk.Tk()
        self.window.title(title)
        self.process_method = process_method

        upload_button = tk.Button(self.window, text="Upload CSV", command=self.upload_csv)
        upload_button.pack()

        self.selected_delimiter = tk.StringVar()
        delimiter_label = tk.Label(self.window, text="Delimiter:")
        delimiter_label.pack()
        self.delimiter_entry = ttk.Combobox(self.window, textvariable=self.selected_delimiter, state = 'readonly')
        self.delimiter_entry['values'] = ('  ,','  ;', '  \\t', '  Space')

        self.delimiter_entry.pack()
        self.delimiter_entry.current(1)

        self.process_button = tk.Button(self.window, text='Process CSV', command=self.process_csv_file)
        self.process_button.pack()

        self.save_button = tk.Button(self.window, text='Download CSV', command=self.save_file)
        self.save_button.pack()

        # Create a status label
        self.status_label = tk.Label(self.window, text="")
        self.status_label.pack()

        self.set_default_state()

    
    def set_default_state(self):
        self.process_button.config(state='disabled')
        self.save_button.config(state='disabled')
        self.file_processed = False

    
    def update_log(self, log_text):
        self.log += f'...{log_text}\n'
        self.status_label.config(text=self.log)

    
    def clear_log(self):
        self.log = ''

    
    def upload_csv(self):
        self.clear_log()
        self.file_path = filedialog.askopenfilename(title="Select CSV File", filetypes=[("CSV files", "*.csv")])
        if self.file_path:
            file_name = Path(self.file_path).name
            self.update_log(f'Successfully uploaded file {file_name}')
            self.enable_processing()

    
    def enable_processing(self):
        self.process_button.config(state='active')

    
    def process_csv_file(self):
        file_path = self.file_path
        delimiter = self.delimiter_entry.get().strip()
        print(delimiter)
    
        if file_path:
            try:
                self.df = pd.read_csv(file_path, delimiter=delimiter)
            
                self.process_method(self.df) # processing over here
                self.file_processed = True

                self.save_button.config(state='active')
                self.update_log(f'Successfully processed file')
            except Exception as e:
                self.update_log(f'Error when processing file: {str(e)}')
            

    def save_file(self):
        save_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if save_path:
            try:
                self.df.to_csv(save_path, index=False)
                self.update_log(f'File saved as: {save_path}')
                self.file_processed = False
                self.save_button.config(state='disabled')
            except Exception as e:
                self.update_log(f'Error when saving file: {str(e)}')
            self.set_default_state()
