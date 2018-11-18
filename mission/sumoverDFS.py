# this is a package for sumover
# made at 2018/11/9
import os


def judge(__name__: str):
	return __name__.find('.') == -1


def traverse_directory(__root_: str, deep: int = 0):
	try:
		pathList = os.listdir(__root_)
	except NotADirectoryError:
		return
	if len(pathList) == 0:
		return
	if deep == 0:
		print(__root_)
	for n in pathList:
		if not judge(n):
			print(2 * (deep + 1) * '-', n)
		else:
			print(2 * (deep + 1) * '-', n)
			traverse_directory(__root_ + '\\' + n, deep + 1)


if __name__ == '__main__':
	__root__: str = input()
	try:
		os.listdir(__root__)
		traverse_directory("F:\\git")
	except NotADirectoryError:
		print("Not Exist!")
		exit()
	except FileNotFoundError:
		print("Not Exist!")
		exit()
