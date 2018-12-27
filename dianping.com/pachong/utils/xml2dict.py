"""
Thunder Chen<nkchenz@gmail.com> 2007.9.1
"""
try:
    import xml.etree.ElementTree as ET
except:
    import cElementTree as ET # for 2.4

#from _object_dict import _object_dict
import re

class _object_dict(dict):
    '''object view of dict, you can
    >>> a = _object_dict()
    >>> a.fish = 'fish'
    >>> a['fish']
    'fish'
    >>> a['water'] = 'water'
    >>> a.water
    'water'
    >>> a.test = {'value': 1}
    >>> a.test2 = _object_dict({'name': 'test2', 'value': 2})
    >>> a.test, a.test2.name, a.test2.value
    (1, 'test2', 2)
    '''
    def __init__(self, initd=None):
        if initd is None:
            initd = {}
        dict.__init__(self, initd)

    def __getattr__(self, item):
        d = self.__getitem__(item)
        # if value is the only key in object, you can omit it
        if isinstance(d, dict) and 'value' in d and len(d) == 1:
            return d['value']
        else:
            return d

    def __setattr__(self, item, value):
        self.__setitem__(item, value)

class XML2Dict(object):

    def __init__(self):
        pass

    def _parse_node(self, node):
        node_tree = _object_dict()
        # Save attrs and text, hope there will not be a child with same name
        if node.text:
            node_tree.value = node.text
        for (k,v) in node.attrib.items():
            k,v = self._namespace_split(k, _object_dict({'value':v}))
            node_tree[k] = v
        #Save childrens
        for child in node.getchildren():
            tag, tree = self._namespace_split(child.tag, self._parse_node(child))
            if  tag not in node_tree: # the first time, so store it in dict
                node_tree[tag] = tree
                continue
            old = node_tree[tag]
            if not isinstance(old, list):
                node_tree.pop(tag)
                node_tree[tag] = [old] # multi times, so change old dict to a list
            node_tree[tag].append(tree) # add the new one

        return  node_tree


    def _namespace_split(self, tag, value):
        """
           Split the tag  '{http://cs.sfsu.edu/csc867/myscheduler}patients'
             ns = http://cs.sfsu.edu/csc867/myscheduler
             name = patients
        """
        result = re.compile("\{(.*)\}(.*)").search(tag)
        if result:
            print (tag)
            value.namespace, tag = result.groups()
        return (tag, value)

    def parse(self, file):
        """parse a xml file to a dict"""
        f = open(file, 'r', encoding='utf8')
        return self.fromstring(f.read())

    def fromstring(self, s):
        """parse a string"""
        t = ET.fromstring(s)
        root_tag, root_tree = self._namespace_split(t.tag, self._parse_node(t))
        return _object_dict({root_tag: root_tree})



if __name__ == '__main__':

    xml = XML2Dict()
    # <?xml version="1.0" encoding="utf-8" ?>, 每一个data都是一个文本,最外层必须是单独的一个标签
    s = """
    <result>
        <count n="1">10</count>
        <data><id>491691</id><name>test</name></data>
        <data><id>491692</id><name>test2</name></data>
        <data><id>503938</id><name>hello,
         world
        </name>
        </data>
    </result>
    """
    '''================================='''
    # r = xml.fromstring(s)
    # from pprint import pprint
    # pprint(r)
    # print (r.result.count.value)
    # print (r.result.count.n)
    #
    # for data in r.result.data:
    #     id = data.id
    #     name = data.name
    #     ntype = type(name)
    #     print (name.split(), ntype )
    # assert False
    '''================================='''
    import os

    # ../data/test.txt

    # resDir = input("输入文本路径：").strip()
    resDir = '../data/articles.xml'
    if not os.path.isfile(resDir):
        print("文本不存在")
        exit(0)

    r = xml.parse(resDir)
    dataList = r.articles.article
    print("查看文本内容,输入文本ID")
    id = int(input("num:"))

    try:
        curtext = dataList[id]
    except:
        print("文本ID不存在")
        exit(0)
    print("url:",curtext.url)
    print("title:", curtext.title)
    print("keys:",curtext.tags)
    print("content:",curtext.content)



    # print(len(r.articles.article), type(r.articles.article))
    #
    # # for data in r.articles.article:
    # #     pprint(data)
    # #     # c = data.content
    # #     ta = data.tags
    # #     ti = data.title
    # #     # ctype = type(c)
    # #     tatype = type(ta)
    # #     titype = type(ti)
    # #     print (ta)
    # #     print(ti)
