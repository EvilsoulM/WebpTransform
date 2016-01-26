# encoding=utf-8
# author EvilsoulM
import commands
import os
import sys, getopt
import shutil

input_file = ""
quality = "75"

output_file = "webp"
compressSize = ""


def handleSysArguments():
    opts, args = getopt.getopt(sys.argv[1:], "hi:o:q:s:")
    global quality
    global output_file
    global compressSize
    global input_file

    for op, value in opts:
        print("op:" + op + "__" + value)
        if op == "-i":
            input_file = value
        elif op == "-o":
            output_file = value
        elif op == "-h":
            print("help")
        elif op == "-q":
            quality = value
        elif op == "-s":
            compressSize = value


def transform():
    final_input_file = sys.path[0] + "/" + input_file

    files = os.listdir(final_input_file)
    for f in files:
        spliteName = os.path.splitext(f)
        filePath = final_input_file + f
        outputPath = final_input_file

        print(spliteName[1])
        if (spliteName[1] == ".webp" or (spliteName[1] != ".jpg" and spliteName[1] != ".png")):
            continue

        if (compressSize.strip() != "" and os.path.getsize(filePath) / 1024.0 > int(compressSize)):
            command = "cwebp -q " + quality + " " + filePath + " -o " + outputPath + "/" + \
                      spliteName[0] + ".webp"
            commands.getstatusoutput(command)
            print("执行了:" + command)
        elif (compressSize.strip() == ""):
            command = "cwebp -q " + quality + " " + filePath + " -o " + outputPath + "/" + \
                      spliteName[0] + ".webp"
            commands.getstatusoutput(command)
            print("执行了:" + command)
        else:
            print("不压缩")

    copyWebpFiles(final_input_file, outputPath + output_file)


def checkArgs():
    if (input_file.strip() == ""):
        print("请输入要转换的文件夹路径")
        exit()


def copyToOutputFile():
    final_input_file = sys.path[0] + "/" + input_file

    files = os.listdir(final_input_file)
    for f in files:
        print(f)


def copyWebpFiles(sourceDir, targetDir):
    if not os.path.exists(targetDir):
        os.makedirs(targetDir)

    print sourceDir
    print(targetDir)

    for file in os.listdir(sourceDir):
        spliteName = os.path.splitext(file)
        if (spliteName[1] != ".webp"):  # 只复制webp文件
            continue

        sourceFile = os.path.join(sourceDir, file)
        targetFile = os.path.join(targetDir, file)

        if os.path.isfile(sourceFile):
            shutil.copy(sourceFile, targetFile)
            os.remove(sourceFile)


if __name__ == '__main__':
    handleSysArguments()
    checkArgs()
    transform()
