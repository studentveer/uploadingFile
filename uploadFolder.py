import os
import dropbox
from dropbox.file import WriteMode

class TransferData:
    def __init__(self,accessToken):
        self.accessToken=accessToken
    def uploadFile(self,fileFrom,fileTo):
        dbx=dropbox.Dropbox(self.accessToken)
        for root, dirs, files in os.walk(fileFrom):
            for fileName in files:
                localpath=os.path.join(root,fileName)
                relative_path = os.path.relpath(localpath, fileFrom)
                dropbox_path = os.path.join(fileTo, relative_path)
                with open (localpath, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    accessToken='sl.AwLDrBi0wxzaqqQatIuEK0X6Tyg5ZAFSHJydZswtRcPLPtsWKhc-DG_zXDTrj7z8C6LqBCSOo7jjPF9Y1YElHwLtIkInvaNbiTNl2OJld14sqeeusjmbLtL-NIlXmZd0mFNYezU'
    transferData=TransferData(accessToken)
    fileFrom=str(input("enter the folder path to transfer"))
    fileTo=input("enter the full path to dropdox")
    transferData.uploadFile(fileFrom, fileTo)
    print("file Has BeeN  MovEd")

main()