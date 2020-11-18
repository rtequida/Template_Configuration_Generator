from tkinter import *
import os.path
import winsound
import random

# Background color and entry field width
COLOR = "gray5"
width = "130"
DisBack = "gray30"
DEF_TEXT = "gray45"
# Variable used to keep track of positioning

# Purpose: Create form
def L2():
    global filename_field
    global filepath_field
    global hostname_field
    global data_num_field
    global data_name_field
    global data_IP_field
    global voice_num_field
    global voice_name_field
    global port_channel_field
    global channel
    global add_field
    global allowed_field
    global interface1_field
    global interface2_field
    global access_field
    global chann_num_field
    global chann_desc_field
    global chann_allowed_field
    global uplink_desc_field
    global snmp_loc_field
    global snmp_poc_field
    global default_IP_field
    global n

    root = Tk()
    # Making the background an image. Uncomment line 43 thru 46 to enable.
    # To change image add .ppm file to file with script in it and put that
    # filename with extension within the paranthesis of the next line.
    #img = PhotoImage(file = "Supporting Files\\Images\\Matrix.ppm")
    #background_label = Label(root, image = img)
    #background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    root.configure(background = COLOR)
    root.title("Config Template")
    # Size of entire form.
    root.geometry("575x860")
    # Creating all labels that appear on the form.
    form = Label(root, text = "Form", bg = COLOR, fg = "white")
    form.grid(row = 0, column = 1, pady = 5)
    n = 1
    createLabel("Filename", n, 0, root)
    createLabel("File Path", n, 0, root)
    createLabel("Hostname", n, 0, root)
    createLabel("Data Vlan", n, 1, root)
    createLabel("Vlan #", n, 0, root)
    createLabel("Vlan Name", n, 0, root)
    createLabel("Vlan IP", n, 0, root)
    createLabel("Voice Vlan", n, 1, root)
    createLabel("Vlan #", n, 0, root)
    createLabel("Vlan Name", n, 0, root)
    createLabel("Port Channel", n, 1, root)
    createLabel("#", n, 0, root)
    createLabel("Description", n, 0, root)
    createLabel("Allowed Vlans", n, 0, root)
    createLabel("Uplinks", n, 1, root)
    createLabel("Interfaces", n, 0, root)
    createLabel("Description", n, 0, root)
    createLabel("Port Channel #", n, 0, root)
    createLabel("Allowed Vlans", n, 0, root)
    createLabel("Access Ports", n, 1, root)
    createLabel("Type and Range", n, 0, root)
    createLabel("Default Gateway", n, 1, root)
    createLabel("IP", n, 0, root)
    createLabel("SNMP", n, 1, root)
    createLabel("Location", n, 0, root)
    createLabel("Contact", n, 0, root)
    createLabel("Additional Commands", n, 0, root)

    # Name of the new file to be created.
    filename_field = Entry(root)
    # Path of the location to place the new config file.
    filepath_field = Entry(root, fg = DEF_TEXT)
    # Insert example text and use lambda functions to delete text when clicking
    # in box and add it back if blank when clicking off box.
    filepath_field.insert(0, "C:\\Users\\...")
    filepath_field.bind("<FocusIn>", lambda event: on_focusin(0,\
        filepath_field))
    filepath_field.bind("<FocusOut>", lambda event: on_focusout(0,\
        filepath_field))
    # Hostname of switch
    hostname_field = Entry(root)
    # Data Vlan number
    data_num_field = Entry(root)
    # Inserting default data vlan number of 2
    data_num_field.insert(0, "2")
    # Data Vlan name
    data_name_field = Entry(root)
    # Inserting default data vlan name of DATA_VLAN
    data_name_field.insert(0, "DATA_VLAN")
    # Data Vlan IP address
    data_IP_field = Entry(root, fg = DEF_TEXT)
    # Insert example text and use lambda functions to delete text when clicking
    # in box and add it back if blank when clicking off box.
    data_IP_field.insert(0, "X.X.X.X X.X.X.X")
    data_IP_field.bind("<FocusIn>", lambda event: on_focusin(2,\
        data_IP_field))
    data_IP_field.bind("<FocusOut>", lambda event: on_focusout(2,\
        data_IP_field))
    # Voice Vlan number
    voice_num_field = Entry(root)
    # Inserting default data vlan number of 3
    voice_num_field.insert(0, "3")
    # Voice Vlan name
    voice_name_field = Entry(root)
    # Inserting default data vlan name of VOICE_VLAN
    voice_name_field.insert(0, "VOICE_VLAN")
    # Port channel number for trunked ports
    chann_num_field = Entry(root)
    chann_desc_field = Entry(root)
    chann_allowed_field = Entry(root, fg = DEF_TEXT)
    chann_allowed_field.insert(0, "2,3,...")
    chann_allowed_field.bind("<FocusIn>", lambda event: on_focusin(3,\
        chann_allowed_field))
    chann_allowed_field.bind("<FocusOut>", lambda event: on_focusout(3,\
        chann_allowed_field))
    uplink_desc_field = Entry(root)
    port_channel_field = Entry(root)
    # Create disabled entries and use lambda functions to delete text when
    # clicking in box and add it back if blank when clicking off box.
    # allowed_field is the entry for the vlans allowed across the trunked links
    allowed_field = Entry(root, fg = DEF_TEXT)
    allowed_field.insert(0, "2,3,...")
    allowed_field.bind("<FocusIn>", lambda event: on_focusin(3,\
        allowed_field))
    allowed_field.bind("<FocusOut>", lambda event: on_focusout(3,\
        allowed_field))
    access_field = Entry(root, fg = DEF_TEXT)
    access_field.insert(0, "Gi 0/1 - 48")
    access_field.bind("<FocusIn>", lambda event: on_focusin(6, access_field))
    access_field.bind("<FocusOut>", lambda event: on_focusout(6, access_field))
    default_IP_field = Entry(root, fg = DEF_TEXT)
    default_IP_field.insert(0, "X.X.X.X")
    default_IP_field.bind("<FocusIn>", lambda event: on_focusin(1, default_IP_field))
    default_IP_field.bind("<FocusOut>", lambda event: on_focusout(1, default_IP_field))
    snmp_loc_field = Entry(root)
    snmp_loc_field.insert(0, "Full Street Address, Tucson, AZ Zip")
    snmp_poc_field = Entry(root)
    snmp_poc_field.insert(0, "Comm Room Specific Info, Rm #, etc.," +\
        " Property Tag: (Asset Tag Info)")
    # Text field for additional commands which will be added at the end of the
    # config file
    add_field = Text(root, width = 15, height = 10)

    interface_frame = Frame(root, bg = COLOR)
    interface1_field = Entry(interface_frame, width = 30, fg = DEF_TEXT)
    interface1_field.insert(0, "Gi1/1/1")
    interface1_field.bind("<FocusIn>", lambda event: on_focusin(4,\
        interface1_field))
    interface1_field.bind("<FocusOut>", lambda event: on_focusout(4,\
        interface1_field))
    interface1_field.pack(side = LEFT, padx = 8)
    interface2_field = Entry(interface_frame, width = 30, fg = DEF_TEXT)
    interface2_field.insert(0, "Gi2/2/2")
    interface2_field.bind("<FocusIn>", lambda event: on_focusin(5,\
        interface2_field))
    interface2_field.bind("<FocusOut>", lambda event: on_focusout(5,\
        interface2_field))
    interface2_field.pack(side = LEFT, padx = 8)

    # Adding all entry fields to the form
    row_num = 1
    filename_field.grid(row = row_num, column = 1, ipadx = width)
    row_num += 1
    filepath_field.grid(row = row_num, column = 1, ipadx = width)
    row_num += 1
    hostname_field.grid(row = row_num, column = 1, ipadx = width)
    row_num += 2
    data_num_field.grid(row = row_num, column = 1, ipadx = width, pady = (5,1))
    row_num += 1
    data_name_field.grid(row = row_num, column = 1, ipadx = width)
    row_num += 1
    data_IP_field.grid(row = row_num, column = 1, ipadx = width, pady = (1,5))
    row_num += 2
    voice_num_field.grid(row = row_num, column = 1, ipadx = width,\
        pady = (5,1))
    row_num += 1
    voice_name_field.grid(row = row_num, column = 1, ipadx = width,\
        pady = (1,5))
    row_num += 2
    chann_num_field.grid(row = row_num, column = 1, ipadx = width)
    row_num += 1
    chann_desc_field.grid(row = row_num, column = 1, ipadx = width)
    row_num += 1
    chann_allowed_field.grid(row = row_num, column = 1, ipadx = width,\
        pady = (1,10))
    row_num += 2
    interface_frame.grid(row = row_num,  column = 1, pady = (5,1))
    row_num += 1
    uplink_desc_field.grid(row = row_num, column = 1, ipadx = width)
    row_num += 1
    port_channel_field.grid(row = row_num, column = 1, ipadx = width)
    row_num += 1
    allowed_field.grid(row = row_num, column = 1, ipadx = width)
    row_num += 2
    access_field.grid(row = row_num, column = 1, ipadx = width, pady = (5,5))
    row_num += 2
    default_IP_field.grid(row = row_num, column = 1, ipadx = width,\
        pady = (5,5))
    row_num += 2
    snmp_loc_field.grid(row = row_num, column = 1, ipadx = width, pady = (5,1))
    row_num += 1
    snmp_poc_field.grid(row = row_num, column = 1, ipadx = width, pady = (1,5))
    row_num += 1
    add_field.grid(row = row_num, column = 1, ipadx = width, pady = (10,5))
    row_num += 1

    # Creating submit button and adding to form
    l3submit = Button(root, text = "Submit", command = process)
    l3submit.grid(row = row_num, column = 1, pady = (10,0))

    root.mainloop()

# Purpose: Run when submit button is pressed. Grab values from all fields and
# append them to config file. Creates new config file in desired location.
def process():
    global data_num
    global voice_num
    # Add name of file and extension to end of sounds to add more sounds.
    sounds = ["Yeah.wav", "Price.wav", "TADAAH.wav", "Batman.wav", "Shut.wav"]
    # Chooses random sound from sounds to play when submit button is pressed.
    x = random.randint(0, len(sounds) - 1)
    sound = os.path.join(sys.path[0], "Sounds\\" + sounds[x])
    winsound.PlaySound(sound, winsound.SND_ASYNC)
    # Grabbing all entry field inputs
    filename = filename_field.get()
    save_path = filepath_field.get()
    # Adds '\' to end of path if user forgets to
    if not save_path.endswith("\\"):
        save_path += "\\"
    hostname = hostname_field.get()
    data_num = data_num_field.get()
    data_name = data_name_field.get()
    data_IP = data_IP_field.get()
    voice_num = voice_num_field.get()
    voice_name = voice_name_field.get()
    chann_num = chann_num_field.get()
    chann_desc = chann_desc_field.get()
    chann_allowed = chann_allowed_field.get()
    interface1 = interface1_field.get()
    interface2 = interface2_field.get()
    uplink_desc = uplink_desc_field.get()
    port_channel = port_channel_field.get()
    allowed = allowed_field.get()
    access = access_field.get()
    default_IP = default_IP_field.get()
    snmp_loc = snmp_loc_field.get()
    snmp_poc = snmp_poc_field.get()
    additional_commands = add_field.get("1.0", END)
    # Reading in config template and attempting to open it. Closes program if
    # it can't be found.
    file_old = os.path.join(sys.path[0],\
        "L2 Text Files\\COT Basic L2 Access Switch Template.txt")
    try:
        file_old = open(file_old)
    except FileNotFoundError:
        print ("ERROR: could not open file " + file_old)
        exit (1)
    # Generating a new file for output. Checks that a file of the same name
    # doesn't already exist and appends an incrememting number to the end of
    # the filename if it does already exist.
    completeName = os.path.join(save_path, filename + ".txt")
    i = 1
    temp = completeName
    while os.path.isfile(temp):
        temp = completeName[0:-4] + str(i) + ".txt"
        i += 1
    completeName = temp
    # Creates the new config file.
    file_new = open(completeName, "w+")
    # Reads through each file in the config template and replaces parameters
    # with user given values.
    for line in file_old.readlines():
        if "@hostname@" in line:
            line = line.replace("@hostname@", hostname)
        if "@data_num@" in line:
            line = line.replace("@data_num@", data_num)
        if "@data_name@" in line:
            line = line.replace("@data_name@", data_name)
        if "@data_IP@" in line:
            line = line.replace("@data_IP@", data_IP)
        if "@voice_num@" in line:
            line = line.replace("@voice_num@", voice_num)
        if "@voice_name@" in line:
            line = line.replace("@voice_name@", voice_name)
        if "@chann_num@" in line:
            line = line.replace("@chann_num@", chann_num)
        if "@chann_desc@" in line:
            line = line.replace("@chann_desc@", chann_desc)
        if "@chann_allowed@" in line:
            line = line.replace("@chann_allowed@", chann_allowed)
        if "@interface1@" in line:
            line = line.replace("@interface1@", interface1)
        if "@interface2@" in line:
            line = line.replace("@interface2@", interface2)
        if "@uplink_desc@" in line:
            line = line.replace("@uplink_desc@", uplink_desc)
        if "@port_channel@" in line:
            line = line.replace("@port_channel@", port_channel)
        if "@allowed@" in line:
            line = line.replace("@allowed@", allowed)
        if "@access@" in line:
            line = line.replace("@access@", access)
        if "@default_IP@" in line:
            line = line.replace("@default_IP@", default_IP)
        if "@snmp_loc@" in line:
            line = line.replace("@snmp_loc@", snmp_loc)
        if "@snmp_poc@" in line:
            line = line.replace("@snmp_poc@", snmp_poc)
        if "@additional_commands@" in line:
            line = line.replace("@additional_commands@", additional_commands)
        # Writing to new config file.
        file_new.write(line)
    file_old.close()
    file_new.close()

# Purpose: Create labels and places them on the form.
# args: title is the text of the label, row is the row the label is placed on,
# col is the column the label is palced on, root is the root of the form itself.
def createLabel(title, row, col, root):
    global n
    new_label = Label(root, text = title, bg = COLOR, fg = "white")
    new_label.grid(row = row, column = col)
    n += 1

# Purpose: clears defaul text when user clicks on field.
# args: n indicates the position to use for text_list, entry is the entry field
# being clicked on
def on_focusin(n, entry):
    text_list = ["C:\\Users\\...", "X.X.X.X", "X.X.X.X X.X.X.X", "2,3,...",\
        "Gi1/1/1", "Gi2/2/2", "Gi 0/1 - 48"]
    if text_list[n] == entry.get():
        entry.delete(0, END)
        entry.config(fg = "black")

# Purpose: Adds default text back to field if field is left blank when clicking
# away from field.
# args: n indicates the position to use for text_list, entry is the entry field
# being clicked on
def on_focusout(n, entry):
    text_list = ["C:\\Users\\...", "X.X.X.X", "X.X.X.X X.X.X.X", "2,3,...",\
        "Gi1/1/1", "Gi2/2/2", "Gi 0/1 - 48"]
    if entry.get() == "":
        entry.config(fg = "gray45")
        entry.insert(0, text_list[n])
