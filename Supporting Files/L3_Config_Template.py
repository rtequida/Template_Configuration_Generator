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
def L3():
    global filename_field
    global filepath_field
    global hostname_field
    global loopback_field
    global data_num_field
    global data_name_field
    global data_IP_field
    global voice_num_field
    global voice_name_field
    global trunk_val
    global route_val
    global port_channel_field
    global route_IP_field1
    global route_IP_field2
    global channel
    global route_IP1
    global route_IP2
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
    root.geometry("575x910")
    # Creating all labels that appear on the form.
    form = Label(root, text = "Form", bg = COLOR, fg = "white")
    form.grid(row = 0, column = 1, pady = 5)
    n = 1
    createLabel("Filename", n, 0, root)
    createLabel("File Path", n, 0, root)
    createLabel("Hostname", n, 0, root)
    createLabel("Loopback IP", n, 0, root)
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
    n += 1
    createLabel("Interfaces", n, 0, root)
    createLabel("Description", n, 0, root)
    createLabel("Port Channel #", n, 0, root)
    createLabel("Allowed Vlans", n, 0, root)
    createLabel("Routed IP Port 1", n, 0, root)
    createLabel("Routed IP Port 2", n, 0, root)
    createLabel("Access Ports", n, 1, root)
    createLabel("Type and Range", n, 0, root)
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
    # Loopback IP address
    loopback_field = Entry(root, fg = DEF_TEXT)
    # Insert example text and use lambda functions to delete text when clicking
    # in box and add it back if blank when clicking off box.
    loopback_field.insert(0, "X.X.X.X")
    loopback_field.bind("<FocusIn>", lambda event: on_focusin(1,\
        loopback_field))
    loopback_field.bind("<FocusOut>", lambda event: on_focusout(1,\
        loopback_field))
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
    port_channel_field = Entry(root, disabledbackground = DisBack, state =\
        DISABLED)
    # Create disabled entries and use lambda functions to delete text when
    # clicking in box and add it back if blank when clicking off box.
    # allowed_field is the entry for the vlans allowed across the trunked links
    allowed_field = Entry(root, disabledbackground = DisBack, state =\
        DISABLED)
    allowed_field.bind("<FocusIn>", lambda event: on_focusin(3,\
        allowed_field))
    allowed_field.bind("<FocusOut>", lambda event: on_focusout(3,\
        allowed_field))
    # IP of the first routed link
    route_IP_field1 = Entry(root, disabledbackground = DisBack, state =\
        DISABLED)
    route_IP_field1.bind("<FocusIn>", lambda event: on_focusin(2,\
        route_IP_field1))
    route_IP_field1.bind("<FocusOut>", lambda event: on_focusout(2,\
        route_IP_field1))
    # IP of the second routed link
    route_IP_field2 = Entry(root, disabledbackground = DisBack, state =\
        DISABLED)
    route_IP_field2.bind("<FocusIn>", lambda event: on_focusin(2,\
        route_IP_field2))
    route_IP_field2.bind("<FocusOut>", lambda event: on_focusout(2,\
        route_IP_field2))
    access_field = Entry(root, fg = DEF_TEXT)
    access_field.insert(0, "Gi 0/1 - 48")
    access_field.bind("<FocusIn>", lambda event: on_focusin(6, access_field))
    access_field.bind("<FocusOut>", lambda event: on_focusout(6, access_field))
    snmp_loc_field = Entry(root)
    snmp_loc_field.insert(0, "Full Street Address, Tucson, AZ Zip")
    snmp_poc_field = Entry(root)
    snmp_poc_field.insert(0, "Comm Room Specific Info, Rm #, etc.," +\
        " Property Tag: (Asset Tag Info)")
    # Text field for additional commands which will be added at the end of the
    # config file
    add_field = Text(root, width = 15, height = 10)

    # New frame to store checkboxes and checkbox labels
    check_frame = Frame(root, bg = COLOR)
    trunk = Label(check_frame, text = "Trunked: ", bg = COLOR, fg = "white")
    trunk.pack(side = LEFT)
    # Boolean variable to keep track of checkbox status
    trunk_val = BooleanVar()
    trunk_check = Checkbutton(check_frame, bg = COLOR, var = trunk_val,\
        command = lambda: trunkClick(trunk_check, route_check))
    trunk_check.pack(side = LEFT)
    route = Label(check_frame, text = "Routed: ", bg = COLOR, fg = "white")
    route.pack(side = LEFT)
    # Boolean variable to keep track of checkbox status
    route_val = BooleanVar()
    route_check = Checkbutton(check_frame, bg = COLOR, var = route_val,\
        command = lambda: routeClick(trunk_check, route_check))
    route_check.pack(side = LEFT)

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
    row_num += 1
    loopback_field.grid(row = row_num, column = 1, ipadx = width,\
        pady = (1,5))
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
    check_frame.grid(row = row_num, column = 1, pady = (1,5))
    row_num += 1
    interface_frame.grid(row = row_num, column = 1)
    row_num += 1
    uplink_desc_field.grid(row = row_num, column = 1, ipadx = width)
    row_num += 1
    port_channel_field.grid(row = row_num, column = 1, ipadx = width)
    row_num += 1
    allowed_field.grid(row = row_num, column = 1, ipadx = width)
    row_num += 1
    route_IP_field1.grid(row = row_num, column = 1, ipadx = width)
    row_num += 1
    route_IP_field2.grid(row = row_num, column = 1, ipadx = width, pady = (1,5))
    row_num += 2
    access_field.grid(row = row_num, column = 1, ipadx = width, pady = (5,5))
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
    loopback = loopback_field.get()
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
    access = access_field.get()
    snmp_loc = snmp_loc_field.get()
    snmp_poc = snmp_poc_field.get()
    additional_commands = add_field.get("1.0", END)
    # Generates uplink port commands based on which checkbox was checked
    uplink_port = getPort()
    # Reading in config template and attempting to open it. Closes program if
    # it can't be found.
    file_old = os.path.join(sys.path[0],\
        "L3 Text Files\\COT Basic L3 Access Switch Template.txt")
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
        if "@loopback@" in line:
            line = line.replace("@loopback@", loopback)
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
        if "@uplink_port@" in line:
            line = line.replace("@uplink_port@", uplink_port)
        if "@interface1@" in line:
            line = line.replace("@interface1@", interface1)
        if "@interface2@" in line:
            line = line.replace("@interface2@", interface2)
        if "@access@" in line:
            line = line.replace("@access@", access)
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

# Purpose: Determines which entry fields to enable and disables if the trunked
# checkbox is clicked.
# args: trunk_check and route_check are the checkboxes.
def trunkClick(trunk_check, route_check):
    # What to do if checked.
    if trunk_val.get():
        # Set routed checkbox to unchecked.
        route_val.set(False)
        # Disable and clear routed fields
        route_IP_field1.delete(0, END)
        route_IP_field1.config(state = DISABLED)
        route_IP_field2.delete(0, END)
        route_IP_field2.config(state = DISABLED)
        # Enable trunked fields and add default values if any.
        port_channel_field.config(state = NORMAL)
        allowed_field.config(state = NORMAL, fg = DEF_TEXT)
        if allowed_field.get() == "":
            allowed_field.insert(0, "2,3,...")
    # What to do if unchecked.
    else:
        port_channel_field.config(state = DISABLED)
        allowed_field.delete(0, END)
        allowed_field.config(state = DISABLED)

# Purpose: Determines which entry fields to enable and disables if the routed
# checkbox is clicked.
# args: trunk_check and route_check are the checkboxes.
def routeClick(trunk_check, route_check):
    # What to do if chekced.
    if route_val.get():
        # Set trunked checkbox to unchecked.
        trunk_val.set(False)
        # Disable and clear trunked fields
        port_channel_field.delete(0, END)
        port_channel_field.config(state = DISABLED)
        allowed_field.delete(0, END)
        allowed_field.config(state = DISABLED)
        # Enable routed fields and add default values if any.
        route_IP_field1.config(state = NORMAL, fg = DEF_TEXT)
        route_IP_field2.config(state = NORMAL, fg = DEF_TEXT)
        if route_IP_field1.get() == "":
            route_IP_field1.insert(0, "X.X.X.X X.X.X.X")
        if route_IP_field2.get() == "":
            route_IP_field2.insert(0, "X.X.X.X X.X.X.X")
    # What do to if unchecked.
    else:
        route_IP_field1.delete(0, END)
        route_IP_field1.config(state = DISABLED)
        route_IP_field2.delete(0, END)
        route_IP_field2.config(state = DISABLED)

# Purpose: Open text files with desired port type and append and modify each
# line to commands
# Return: commands which is the text of the uplink port configs
def getPort():
    file = None
    commands = ""
    uplink_desc = uplink_desc_field.get()
    # Gets trunk port config if trunked checkbox is checked.
    if trunk_val.get():
        channel = port_channel_field.get()
        allowed = allowed_field.get()
        file = os.path.join(sys.path[0], "L3 Text Files\\Trunk Port.txt")
        try:
            file = open(file)
        except FileNotFoundError:
            print ("ERROR: could not open file " + file)
            exit (1)
    # Gets routed port config if routed checkbox is checked.
    elif route_val.get():
        route_IP1 = route_IP_field1.get()
        route_IP2 = route_IP_field2.get()
        file = os.path.join(sys.path[0], "L3 Text Files\\Route Port.txt")
        try:
            file = open(file)
        except FileNotFoundError:
            print ("ERROR: could not open file " + file)
            exit (1)
    # Reads in each line of the selected file and replaces parameters with user
    # given values.
    if file != None:
        for line in file:
            if "@uplink_desc@" in line:
                line = line.replace("@uplink_desc@", uplink_desc)
            if "@route_IP1@" in line:
                line = line.replace("@route_IP1@", route_IP1)
            if "@route_IP2@" in line:
                line = line.replace("@route_IP2@", route_IP2)
            if "@channel@" in line:
                line = line.replace("@channel@", channel)
            if "@allowed@" in line:
                line = line.replace("@allowed@", allowed)
            commands += line
        file.close()
    return commands
