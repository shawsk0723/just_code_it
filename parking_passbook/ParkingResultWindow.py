"""
Module name
- ParkingPassbookApp

Author
- 코드장인
- https://blog.naver.com/shawgibal
"""


# Import the required libraries
from tkinter import *
from tkinter import ttk

class ParkingResultWindow:

    def __init__(self):

        # Create an instance of tkinter frame
        win = Tk()

        win.title("이자 계산 결과")

        # Set the size of the tkinter window
        win.geometry("700x350")

        # Create an object of Style widget
        style = ttk.Style()
        style.theme_use('clam')

        self.win = win

    def setHeadRow(self, headRow):
        treeView = ttk.Treeview(self.win, column=headRow, show='headings', height=5)
        treeView.pack()

        for i, head in zip(range(len(headRow)), headRow):
            treeView.column("# {}".format(i+1), anchor=CENTER)
            treeView.heading("# {}".format(i+1), text=head)

        self.treeView = treeView

    def setBodyRows(self, bodyRows):
        # Insert the data in Treeview widget
        for bodyRow in bodyRows:
            self.treeView.insert('', 'end', text="1", values=bodyRow)


    def display(self):

        self.win.mainloop()


def test():
    headRow = ["파킹 통장", "이자"]
    bodyRows = [['OK 세컨드', '55,000'], ['페퍼스 파킹 통장', '60,000']]

    parkingResultWindow = ParkingResultWindow()
    parkingResultWindow.setHeadRow(headRow)
    parkingResultWindow.setBodyRows(bodyRows)
    parkingResultWindow.display()

if __name__ == '__main__':
    test()