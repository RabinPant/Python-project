# Program By Rabin Pant


#This Program calculates the
#Body mass index of a person
#The result is display in a label
#on the main window

import tkinter
import tkinter.messagebox

class BodyMassIndex:
    def __init__(self):
        
        #Create the main window.
        self.main_window = tkinter.Tk()
        
        #create frames
        self.input_height_frame = tkinter.Frame(self.main_window)
        self.input_weight_frame = tkinter.Frame(self.main_window)
        self.result_frame = tkinter.Frame(self.main_window)
        self.message_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)
        
        
        #Create the widget for the input frame one
        self.input_height_label = tkinter.Label(self.input_height_frame,\
                                          text='Enter your height in inches:')
        self.input_height_label.pack()
        self.input_height_entry = tkinter.Entry(self.input_height_frame,\
                                          width = 30)
        self.input_height_entry.pack()
        
        
        
        #Create the widget for the input frame two
        self.input_weight_label = tkinter.Label(self.input_weight_frame,\
                                          text='Enter your weight in pounds:')
        self.input_weight_label.pack()
        
        self.input_weight_entry = tkinter.Entry(self.input_weight_frame,\
                                          width = 30)
        self.input_weight_entry.pack()
        
        #creating the widget for the result
        self.result_label = tkinter.Label(self.result_frame,\
                                          text = 'Result BMI:')
        
        #updating calculate value evertime the value gets changed in real time
        # Making more dynamic
        self.calculated = tkinter.StringVar() 
        self.calculated_value = tkinter.Message(self.result_frame,\
                                          textvariable=self.calculated)
        ###background change and color
        self.calculated_value.config(width='100',bg='white',font=(20))
        self.result_label.pack(side='left')
        self.calculated_value.pack(side='left')
        
        #creating the message widget for the message box
        
        self.message_label = tkinter.Label(self.message_frame,\
                                          text = '')
        #updating message evertime the value gets changed in real time
        self.message_deliver = tkinter.StringVar() 
        
        ###background change and color
        self.message_deliver_message = tkinter.Message(self.message_frame,\
                                          textvariable=self.message_deliver)
        self.message_deliver_message.config(bg='white',width=120,font=('times',12,'italic'))
        
        self.message_label.pack(side='left')
        self.message_deliver_message.pack(side='left')
        
        #create and pack the button widgets.
        #two button one for
        #getting result
        #one for killing the window
        self.result_button =tkinter.Button(self.button_frame,\
                                           text='CalculateBMI',\
                                           command = self.calculate)
        self.quit_button = tkinter.Button(self.button_frame,\
                                          text = 'QUIT',\
                                          command =self.main_window.destroy)
        self.result_button.pack(side="left")
        self.quit_button.pack(side = "left")
        
        #pack the frames.
        
        self.input_height_frame.pack()
        self.input_weight_frame.pack()
        self.result_frame.pack()
        self.message_frame.pack()
        self.button_frame.pack()
        
        #start the main loop
        tkinter.mainloop()
    
   # The calculate method is the call back fucntion for
   #result_button widget
   
    def calculate(self):
       
       #Input for the height and weight
        self.height = float(self.input_height_entry.get())
        self.weight = float(self.input_weight_entry.get())
        
        #calculate the BMI
        self.BMI = (self.weight*703)/(self.height*self.height)
       
       #passing calculated BMI
        self.calculated.set(format(self.BMI,".2f"))
       
       #corresponding message for calculated BMI
        if(self.BMI<18.5):
            self.message_deliver.set("UNDERWEIGHT")
        elif(self.BMI>=18.5 and self.BMI<25):
            self.message_deliver.set('NORMAL')
        elif(self.BMI>=25 and self.BMI<30):
            self.message_deliver.set('OVERWEIGHT')
        elif(self.BMI>=30):
            self.message_deliver.set('OBESE')
#main function            
def main():
    
    #instance or object of the class BodyMassIndex
    calulated_bmi = BodyMassIndex()

#calling main function    
main()
