# sync-grid

- 运行sync-grid.py启动后端，然后在OBS中添加浏览器源，地址localhost:22708
- 在另一设备上访问 你的电脑IP地址:22708，用来控制格子点亮与熄灭。

## 编辑表格内文字

- 修改grid-text.txt
- 每一行会被依次填入表格

## 识别已有的表格

- 复制已有的表格图片
- 运行recognize.py
- 识别结果会自动写入grid-text.txt
- *此功能使用了[百度的文字识别API](https://ai.baidu.com/ai-doc/OCR/Al1zvpylt)，需要将[access_token](https://ai.baidu.com/ai-doc/REFERENCE/Ck3dwjhhu)填入ocr/baidu/access_token
