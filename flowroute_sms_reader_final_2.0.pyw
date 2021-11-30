import wx
from flowroutenumbersandmessaging.flowroutenumbersandmessaging_client import FlowroutenumbersandmessagingClient
import csv
import tqdm
import wx.lib.filebrowsebutton
import os


client = FlowroutenumbersandmessagingClient('Access Key', 'Secret Key')
messages_controller = client.messages


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Flowroute sms raw reader')
        panel = wx.Panel(self)

        self.SetSize(wx.Size(350, 200))

        my_btn = wx.Button(panel, label='Create', pos=(230, 82))
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)

        self.browse = wx.lib.filebrowsebutton.FileBrowseButton(panel, labelText="Select a csv file:", fileMask="*.csv", pos=(25, 50))

        self.Show()

        wx.StaticText(panel, label="Which raw would you like to convert?", pos=(70, 5))

    def on_press(self, panel):
        browse1 = self.browse.GetValue()
        username = os.getlogin()

        if not browse1:
            wx.MessageBox("ERROR \n(Required field empty)")
        else:
            def main(browse1):

                clients = client_list(browse1)

                count_lines = 0

                w_file = open('C:/Users/' + username + '/Desktop/flowroute _raw_results.csv', 'w')
                w_file.write(
                    "Client,text_count_sms_longcode,text_count_mms_longcode,text_count_sms_toll_free,text_count_mms_toll_free,,text_count_sms_longcode,text_count_mms_longcode,text_count_sms_toll_free,text_count_mms_toll_free\n")

                for count in tqdm.trange(len(clients)):
                    count_lines += 1
                    total_amount_sms_longcode, total_amount_mms_longcode, total_amount_sms_toll_free, total_amount_mms_toll_free, text_count_sms_longcode, text_count_mms_longcode, text_count_sms_toll_free, text_count_mms_toll_free = spreadsheet(
                        browse1, clients[count])

                    if total_amount_sms_longcode == 0:
                        total_amount_sms_longcode = ""
                    if total_amount_mms_longcode == 0:
                        total_amount_mms_longcode = ""
                    if total_amount_sms_toll_free == 0:
                        total_amount_sms_toll_free = ""
                    if total_amount_mms_toll_free == 0:
                        total_amount_mms_toll_free = ""

                    if text_count_sms_longcode == 0:
                        text_count_sms_longcode = ""
                    if text_count_mms_longcode == 0:
                        text_count_mms_longcode = ""
                    if text_count_sms_toll_free == 0:
                        text_count_sms_toll_free = ""
                    if text_count_mms_toll_free == 0:
                        text_count_mms_toll_free = ""

                    line = clients[count] + "," + str(text_count_sms_longcode) + "," + str(
                        text_count_mms_longcode) + "," + str(text_count_sms_toll_free) + "," + str(
                        text_count_mms_toll_free) + ",," + str(total_amount_sms_longcode) + "," + str(
                        total_amount_mms_longcode) + "," + str(total_amount_sms_toll_free) + "," + str(
                        total_amount_mms_toll_free) + "\n"
                    w_file.write(line)
                    print("\n")

            def client_list(browse1):
                with open(browse1, "r") as file:
                    reader = csv.reader(file)

                    clients = []

                    for row in reader:
                        c = row[9]
                        if c not in clients:
                            clients += [c]

                    clients.sort()

                    if clients[0] in (None, ""):
                        del clients[0]

                    if "client" in clients:
                        clients.remove("client")

                    return clients

            def spreadsheet(browse1, client):

                with open(browse1, "r") as file:
                    reader = csv.reader(file)

                    total_amount_sms_longcode = 0
                    total_amount_mms_longcode = 0
                    total_amount_sms_toll_free = 0
                    total_amount_mms_toll_free = 0

                    text_count_sms_longcode = 0
                    text_count_mms_longcode = 0
                    text_count_sms_toll_free = 0
                    text_count_mms_toll_free = 0

                    for row in reader:

                        # -------------------------------------Client filter 1-----------------------------------------

                        if client == row[9] and "longcode" in row[4]:

                            if "true" in str(row[3]):
                                total_amount_mms_longcode += float(row[0])
                                text_count_mms_longcode += 1


                            elif "false" in str(row[3]):
                                total_amount_sms_longcode += float(row[0])
                                text_count_sms_longcode += 1

                        # ---------------------------------Client Filter 2------------------------------------------------
                        if client == row[9] and "toll-free" in row[4]:

                            if "true" in str(row[3]):
                                total_amount_mms_toll_free += float(row[0])
                                text_count_mms_toll_free += 1


                            elif "false" in str(row[3]):
                                total_amount_sms_toll_free += float(row[0])
                                text_count_sms_toll_free += 1

                    # ---------------------------------Client Filter 3------------------------------------------------

                    # ---------------------------------Client Filter 4------------------------------------------------

                    return float(total_amount_sms_longcode), float(total_amount_mms_longcode), float(
                        total_amount_sms_toll_free), float(
                        total_amount_mms_toll_free), text_count_sms_longcode, text_count_mms_longcode, text_count_sms_toll_free, text_count_mms_toll_free

            main(browse1)
            wx.MessageBox("File created on desktop")


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
