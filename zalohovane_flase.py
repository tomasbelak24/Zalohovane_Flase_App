from csv_processor import CSV_PROCESSOR
from processing_methods import ZalohovaneFlaseProcessing

if __name__ == '__main__':

    App = CSV_PROCESSOR(title = 'DRS Flase', process_method=ZalohovaneFlaseProcessing)
    # Start the GUI application
    App.window.mainloop()