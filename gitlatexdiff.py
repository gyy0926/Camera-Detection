import os, shutil, stat

#若安装了git-latexdiff，可以直接使用下面的语句
#os.system('git latexdiff --main main.tex --output main-diff.pdf HEAD --')

def readonly_handler(func, path, execinfo):
    os.chmod(path, stat.S_IWRITE)
    func(path)

os.system('git clone . ./OLD')
#若论文包含多个tex文件，可以使用下面的语句
#os.system('latexdiff --flatten ./OLD/main.tex main.tex > main-diff.tex')
os.system('latexdiff ./OLD/main.tex main.tex > main-diff.tex')
#若需要对idea文档diff，可以使用下面的语句
#os.system('latexdiff ./OLD/idea.tex idea.tex > idea-diff.tex')
shutil.rmtree('OLD', onerror = readonly_handler)