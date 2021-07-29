import glob

if __name__ == '__main__':

    released = dict({

        })
    released['samsung'] = []
    released['samsung'].append(2019)
    released['samsung'].append(2016)
    released['samsung'].append(2019)
    released['iphone5S'] = values = []
    released['iphone5S'] += [2015]
    released['iphone5S'] += [2016]
    released['iphone5S'].append(2018)

    print(released["iphone5S"])
    print(released['samsung'])
    for e in released:
        print(len(released.get(e)))
    folder = glob.glob("C://Users/Admin/PycharmProjects/AD/data/foursum/*.txt")
    for files in folder:
        with open(files) as file:
            print(file.read())

