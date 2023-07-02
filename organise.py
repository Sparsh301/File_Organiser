import os
import shutil
import pathlib

fileformat={

    "Web": [".html5",".html",".htm",".xhtml"],

    "Picture": [".jpeg",".jpg",".tiff",".gif",".bmp",".png",".bpg","svg",".heif",".psd"],

    "Video": [".avi",".mkv",".flv",".wmv",".mov",".mp4",",webm",".vob",".mng",".qt",".mpg",".mpeg",".3pg"],

    "Document": [".oxps", ".epub", ".pages", ". docx",".txt", ".pdf", ".doc", ".fdf" ,".ods", ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox", ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", "pptx"],

    "Compressed": [".a", ".ar",".cpio",".iso", ".tar", ".gz", ".rz", ".72",".dmg", ".rar", ".xar", ".zip"],
    
    "Audio": [".aac", "kaa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"]
}

fileTypes=list(fileformat.keys())
fileFormats=list(fileformat.values())

print(fileTypes)
print(fileFormats)

for file in os.scandir():
    fileName=pathlib.Path(file)
    fileFormatType=fileName.suffix.lower()

    src=str(fileName)
    dest="Other"

    if fileFormatType == "":
        print(f"{src} has no file format")
    else:
        for formats in fileFormats:
            if fileFormatType in formats:
                folder=fileTypes[fileFormats.index(formats)]
                print(folder)

                dest=folder
                if os.path.isdir(folder)==False:
                    os.mkdir(folder)

                print(dest)
                
            else:
                if os.path.isdir("Other")==False:
                    os.mkdir("Other")

    
    print(src, "moved to ",dest)
    shutil.move(src,dest)


print("File organiser started")
input("Press enter to exit:")


