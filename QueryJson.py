import json
import collections


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.label = set()


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.found = set()
        self.storage = {}

    def insert(self, json_data, index):
        cur = self.root
        for item in json_data:
            if isinstance(item, list):
                for i in item:
                    cur = cur.children[i]
                    cur.label.add(index)
            else:
                cur = cur.children[item]
                cur.label.add(index)

    def search(self, json_data):
        cur = self.root
        for item in json_data:
            if isinstance(item, list):
                for i in item:
                    cur = cur.children[i]
                    self.found = self.found.intersection(cur.label)

            else:
                cur = cur.children[item]
                self.found = self.found.intersection(cur.label)

    def add(self, s, index):
        data = json.loads(s)
        if data:
            self.add_helper(data, index, [])

    def add_helper(self, json_data, index, arr):
        if isinstance(json_data, dict):
            for i in json_data.keys():
                arr.append(i)
                self.add_helper(json_data[i], index, arr)
                arr.pop()

        elif isinstance(json_data, list):
            for i in json_data:
                arr.append(i)
                self.add_helper(i, index, arr)
                arr.pop()

        else:
            arr.append(json_data)
            self.insert(arr, index)
            arr.pop()

    def get(self, s):
        data = json.loads(s)
        self.found = set(self.storage.keys())
        self.get_helper(data, [])
        for i in enumerate(self.found):
            print(self.storage[i[1]])

    def get_helper(self, json_data, arr):
        if isinstance(json_data, dict):
            for i in json_data.keys():
                arr.append(i)
                self.get_helper(json_data[i], arr)
                arr.pop()

        elif isinstance(json_data, list):
            for i in json_data:
                arr.append(i)
                self.get_helper(i, arr)
                arr.pop()

        else:
            arr.append(json_data)
            self.search(arr)
            arr.pop()

    def delete(self, s):
        data = json.loads(s)
        if data:
            self.found = set(self.storage.keys())
            self.get_helper(data, [])
            for i in self.found:
                self.storage.pop(i, None)


def main():
    node = Trie()
    idx = 1
    while True:
        try:
            line = input()
            if 'add' in line:
                node.storage[idx] = line.replace('add ', '')
                node.add(line.replace('add ', ''), idx)
                idx += 1

            if 'get' in line:
                node.get(line.replace('get ', ''))

            if 'delete' in line:
                node.delete(line.replace('delete ', ''))

        except EOFError:
            return


if __name__ == '__main__':
    main()