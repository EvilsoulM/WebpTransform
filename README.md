##Webp png jpg 批量转webp脚本

###使用
- 配置环境 <p>
 1.安装cwebp <p>
   brew install webp <p>
 2.参数 <p>
 -s 最小要压缩图片大小 不输入 为全部压缩 （kb）<p>
 -i 要压缩的图片文件夹目录 <p>
 -o 输出目录 可以不输入 <p>
 -q 压缩图片质量  默认75 <p>
 3.使用 <p>

 ```
    python webputils.py -i drawable-xhdpi/ -s 20 #压缩drawble-xhdpi目录下图片大于20kb的图片
 ```
