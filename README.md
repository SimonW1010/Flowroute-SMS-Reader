# Flowroute-SMS-Reader
Meant to be used in conjunction with [Flowroute SMS export](https://github.com/SimonW1010/Flowroute-SMS-Export). This script takes the raw SMS Flowroute Excel file created and converts it into a simple to read neat Excel sheet for easy billing or analysis.

# Imports
```
import wx
import csv
import os
import tqdm
```

# Flowroute Installation (Skip if already done with SMS Export)
Go to [Flowroute Github](https://github.com/flowroute/flowroute-sdk-v3-python) and download as a zip 
>
Extract zip contents 
>
Open Windows terminal (Windows + R type: cmd)
>
type ```cd C:\Users\ Location of extracted file```
>
Once you're in the proper directory type ```pip3 install -r requirements.txt```
>
Copy and paste the flowroutenumbersandmessaging folder into you're C:\Users\your user\AppData\Local\Programs\Python\Python39\Lib\site-packages directory

# Access Key / Secret Key (Same as with SMS Export)
For line 6 you're going to need your flowroute API keys these are found here
>
Login Into Flowroute > Prefrences > API Control
>
![Screenshot 2021-11-28 155648](https://user-images.githubusercontent.com/93505099/143791617-219d24e4-5e96-4dca-a4d4-6d250a49274a.png)
>NOTE: The blue arrows point to location the red arrows point to where the API accesss keys are located

# Using the GUI 
![Screenshot 2021-11-30 130319](https://user-images.githubusercontent.com/93505099/144128168-781a5466-50dd-4034-8ed3-036538caee96.png)
>
Simply Browse for location of raw SMS Export file (red arrow) or type the path into the bar
>
Then click "create" (Blue Arrow) and BAM a new file will be placed in the same directory as the file you selected
