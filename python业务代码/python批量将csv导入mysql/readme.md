# 代码功能

代码实现将一个文件夹中的所有csv文件批量导入到mysql中去。

# 输入

需要更改os.chdir('/home/wenbinyao/data/yiwudata/')这个地方的路径为你的文件夹所在的路径。

可能要更改pd.read_csv的编码方式。

可能需要更改f.rename。

可能需要更改字符的varchar的长度。

# 输出

将csv文件导入到了mysql中。