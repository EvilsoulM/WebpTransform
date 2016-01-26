##Webp png jpg 批量转webp脚本

###使用
- 配置环境 <p>
 1.安装cwebp <p>
   brew install webp <p>
- 参数 <p>
 -s 最小要压缩图片大小 （kb）<p>
 -i 要压缩的图片文件夹目录 <p>
 -o 输出目录 可以不输入 <p>
 -q 压缩图片质量  默认75 <p>
- 使用 <p>

 ```
    python webputils.py -i drawable-xhdpi/ -s 20 -q 50 -o output  #转换drawable-xhdpi中大于20kb的图片到output目录下（质量是50）
    简便方式直接输入即可 python webputils.py -i drawable-xhdpi/
 ```
