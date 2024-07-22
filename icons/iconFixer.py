import os


class Main:
    def __init__(self):
        self.workSpaceFolders = ['Active', 'Deactivate', 'NonActive']
        self.currentPath = os.getcwd()
        self.fix_icons()

    def fix_icons(self):
        for folderName in self.workSpaceFolders:
            folderPath = os.path.join(self.currentPath, folderName)
            if not os.path.exists(folderPath):
                continue

            filesList = os.listdir(folderPath)
            for fileName in filesList:
                correctPrefix = f'{folderName}_'
                if not fileName.startswith(correctPrefix):
                    newFileName = f'{correctPrefix}{fileName[0].upper()}{fileName[1:]}'
                    if os.path.exists(os.path.join(folderPath, newFileName)):
                        os.remove(os.path.join(folderPath, newFileName))
                    os.rename(os.path.join(folderPath, fileName), os.path.join(folderPath, newFileName))
                    print(f'{fileName} was renamed to {newFileName}')
                elif fileName[len(correctPrefix)].islower():
                    newFileName = f'{correctPrefix}{fileName[len(correctPrefix)].upper()}{fileName[len(correctPrefix) + 1:]}'
                    os.rename(os.path.join(folderPath, fileName), os.path.join(folderPath, newFileName))
                    print(f'{fileName} was renamed to {newFileName}')

            else:
                print(f'No files were found in {folderName}')


if __name__ == "__main__":
    Main()
