import tkinter as tk
from tkinter import messagebox


# chatbot command list type definition
ws_g = ['Google', 'Google on', 'Google on']
question = ["Whats the postal code of your current residence?", "Do you have cough? (Y/N)", "Do you have colds? (Y/N)", "Do you have Diarrhea? (Y/N)", "Do you have sore throught? (Y/N)", "Are you experiencing MYALGIA or Body Aches? (Y/N)", "Do you have Headache? (Y/N)",
            "Do you have fever?(Temperature 37.8 C and above) (Y/N)", "Are you having difficulty in breathing? (Y/N)", "Are your experiencing Fatigue? (Y/N)", "Have you travelled recently during the past 14days? (Y/N)", "Do you have travel history to a COVID-19 INFECTED AREA? (Y/N)", "Do you have direct contact or is taking care of a positive COVID-19 PATIENT? (Y/N)"]
confirmation = ["yeah", "Yeah", "yes", "yes ", "Yes", "y", "Y", "ha", "Ha"]
deny = ["nope", "Nope", "no", "no ", "No", "N", "n", "na"]

base = tk.Tk()
input_message = tk.StringVar(base)
input_message.set("")
base.title('NoCO Bot')
base.geometry('750x600')


# Mainframe
frame1 = tk.Frame(height=60, width=70, bg="#A9D0F5")
frame2 = tk.Frame(height=400, width=70, bg="#A9D0F5")
frame3 = tk.Frame(height=80, width=70, bg="#A9D0F5")
frame1.pack(fill='x', side='top')
frame2.pack(fill='both', expand='YES')
frame3.pack(fill='x', side='bottom')


# Bot name label
bot_name = tk.Label(frame1, text='NoCo BOT', bg='#A9D0F5',
                    font=('Helvetica', 12), width=15, height=2)
bot_name.pack(side='left')


# Message box
message_window = tk.Text(frame2, bg='#CED8F6',
                         yscrollcommand='YES', font=('NanumGothic', 12))
message_window.insert('end', '\n NoCo :\t' +
                      'Hello there. I am NoCo bot. I will help you to find out the chances of you being corona infected.\n \t Would you like to proceed? \n')
message_window.insert('end', '\n NoCo :\t' +
                      'Whats your name?.\n')


message_window.config(state='disabled')
message_window.pack(side='top', expand='YES', fill='both')


input_entry = tk.Entry(frame3, width=10, bg='white',
                       textvariable=input_message, font=('NanumGothic', 12))
input_entry.pack(side='left', expand='YES', fill='both')

count = -1
points = 0
# Input / output part


def add_text(mw, st, imsg):
    # mw:message window/st:state/imsg:input message
    global count, points
    message_send_by_bot = ''
    message_send_by_human = imsg.get()

    if count == -1:
        message_send_by_human = '\n ME   :\t'+imsg.get()+'\n'
        count += 2
        message_send_by_bot = '\n NoCo   :\t' + question[0] + '\n'
        mw.config(state='normal')  # entery Status default
        mw.insert('end', message_send_by_human)  # Add user message
        mw.insert('end', message_send_by_bot)  # Add bot message
        imsg.set("")
        mw.see('end')
        mw.config(state='disabled')

    elif count == 1:
        message_send_by_human = '\n ME   :\t'+imsg.get()+'\n'
        message_send_by_bot = '\n NoCo   :\t' + question[count] + '\n'
        mw.config(state='normal')  # entery Status default
        mw.insert('end', message_send_by_human)  # Add user message
        mw.insert('end', message_send_by_bot)  # Add bot message
        imsg.set("")
        mw.see('end')
        mw.config(state='disabled')
        count += 1

    elif message_send_by_human in confirmation and count > 1 and count <= 12:
        if count <= 8:
            points += 1
        elif count >= 9 and count <= 10:
            points += 2
        elif count > 11 and count <= 13:
            points += 3
        message_send_by_human = '\n ME   :\t'+imsg.get()+'\n'
        message_send_by_bot = '\n NoCo   :\t' + question[count] + '\n'
        mw.config(state='normal')  # entery Status default
        mw.insert('end', message_send_by_human)  # Add user message
        mw.insert('end', message_send_by_bot)  # Add bot message
        imsg.set("")
        mw.see('end')
        mw.config(state='disabled')
        count += 1

    elif message_send_by_human in deny and count <= 12:
        message_send_by_human = '\n ME   :\t'+imsg.get()+'\n'
        message_send_by_bot = '\n NoCo   :\t' + question[count] + '\n'
        mw.config(state='normal')  # entery Status default
        mw.insert('end', message_send_by_human)  # Add user message
        mw.insert('end', message_send_by_bot)  # Add bot message
        imsg.set("")
        mw.see('end')
        mw.config(state='disabled')
        count += 1

    else:
        if points >= 0 and points <= 2:
            message_send_by_bot = '\n\n NoCo   :\t' + \
                'Almost no chances of infection' + '\n' + \
                "\tMaybe due to stress." + " Stay at home, take care!" + "\n"
        elif points >= 3 and points <= 5:
            message_send_by_bot = '\n NoCo   :\t' + \
                'Hydrate properly and proper hygiene. Observe and re-evaluate after 2 days' + \
                '\n' + "\tSelf isolate yourself."
        elif points >= 6 and points <= 12:
            message_send_by_bot = '\n NoCo   :\t' + \
                'Seek consultation with Doctor.' + '\n' + \
                "\tCompletely isolate yourself, even from your family!"
        elif points > 12 and points <= 24:
            message_send_by_bot = '\n NoCo   :\t' + \
                'CALL HOTLINE!' + '\n' + \
                "\tInform all people you have met to get checked if they show even the slightest symptoms!"
        mw.config(state='normal')
        mw.insert('end', message_send_by_human)
        mw.insert('end', message_send_by_bot)
        imsg.set("")
        mw.see('end')
        mw.config(state='disabled')


# Input button
send_button = tk.Button(frame3, text='input', width=10, height=2, relief='groove', bg='#81BEF7',
                        state='active', command=lambda: add_text(message_window, input_entry, input_message))
send_button.pack(side='right')
base.bind('<Return>', lambda x: add_text(
    message_window, input_entry, input_message))  # Use the Enter key

base.mainloop()
