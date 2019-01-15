# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2019-01-13 15:48:18
# @Last Modified time: 2019-01-15 14:51:00


class element():

    def __init__(self, type, id, no):
        self.type = type.lower()
        self.id = id
        self.no = no
        # root
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent

    def gatherAttrs(self):
        return ",".join("{}={}"
                        .format(k, getattr(self, k))
                        for k in self.__dict__.keys())


type_dict = {}
id_dict = {}


def add_dict(element):
    type = element.type
    type_list = type_dict.get(type, [])
    type_list.append(element)
    type_dict[type] = type_list

    id = element.id
    if id is not None:
        id_dict[id] = element


def get_element(name):
    s_element = None
    if name.startswith('#'):
        s_element = [id_dict.get(name)]
    else:
        s_element = type_dict.get(name)
    return s_element


def search_parent(child, target):
    # print(child.type, child.parent.type)
    parent_element = child.parent
    while parent_element is not None:
        # print(parent_element.type, parent_element.id, target)

        if target.startswith('#') and parent_element.id == target:
            return parent_element
        elif not target.startswith('#') and parent_element.type == target:
            return parent_element
        parent_element = parent_element.parent
    return None


def main():
    line_num, query_num = [int(i) for i in input().split()]

    pre_dot_num = 0
    parent_stack = []
    for i in range(line_num):
        line_content = input()
        dot_num = line_content.count('.')

        line_content = line_content.lstrip('.')
        ss = line_content.split(' ')

        new_element = None
        if len(ss) == 2:
            type, id = ss
            new_element = element(type, id, i + 1)
        else:
            type = ss[0]
            new_element = element(type, None, i + 1)

        # only executed once
        if dot_num == 0:
            parent_stack.append(new_element)
        # new child
        elif dot_num - 2 == pre_dot_num:
            new_element.set_parent(parent_stack[-1])
            # print(new_element.parent.type)
            parent_stack.append(new_element)
        elif dot_num + 2 == pre_dot_num:
            parent_stack.pop()
            parent_stack.pop()
            new_element.set_parent(parent_stack[-1])
            # print(new_element.parent.type)
            parent_stack.append(new_element)
        elif dot_num == pre_dot_num:
            new_element.set_parent(parent_stack[-1].parent)
            # print(new_element.parent.type)
            parent_stack.append(new_element)

        pre_dot_num = dot_num
        add_dict(new_element)

    res = []
    for i in range(query_num):
        query = input()
        ss = query.split(' ')
        if len(ss) == 1:
            s_element = get_element(ss[0])
            if s_element is None:
                res.append(str(0))
            else:
                lines = [str(e.no) for e in s_element]
                res.append(str(len(lines)) + ' ' + ' '.join(lines))

        else:
            ss.reverse()
            candidate_elements = get_element(ss[0])
            lines = []
            for candidate_element in candidate_elements:
                cur_element = candidate_element
                is_find = True
                for s in ss[1:]:
                    cur_element = search_parent(cur_element, s)
                    if cur_element is None:
                        is_find = False
                        break
                if is_find:
                    lines.append(str(candidate_element.no))
            res.append(str(len(lines)) + ' ' + ' '.join(lines))

    for r in res:
        print(r)


if __name__ == '__main__':
    main()
