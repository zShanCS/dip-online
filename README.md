Digital Image Processing Online

Install Requirements by using
      pip install -r requiremts.txt

put your "images" folder inside static folder

edit the get_neighbors method in main to return whatever neighbors you want.
The result list should contain list of string names of files (in png format) 
These images must be present in your new static/images folder

In root, open terminal and run
      uvicorn main:app --reload
to run the app in development mode.