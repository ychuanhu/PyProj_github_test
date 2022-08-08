import zipfile


zipfilename = "projych.pcwex"
print(zipfile.is_zipfile(zipfilename))
zfile = zipfile.ZipFile(zipfilename, 'r')
print(zfile)
with zipfile.ZipFile(zipfilename, 'r') as zfile:
    print(zfile.infolist())
with zipfile.ZipFile(zipfilename, 'r') as zfile:
    nl = zfile.namelist()
    il = zfile.infolist()

    print(nl)
    for n in nl:
        if "DataList.dl" in n:
            print(n)


    infomation = zfile.getinfo("PROJECT/Hardware/CFG_64DB093CD00642BE8AEA46AAE240A875/DataList.dl")
    print(infomation.file_size)

