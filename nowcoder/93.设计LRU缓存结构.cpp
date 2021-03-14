#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

class Node {
public:
    int key, value;
    Node* prev;
    Node* next;
    Node(int k, int v)
    {
        key = k;
        value = v;
        prev = NULL;
        next = NULL;
    }
};

class Solution {
private:
    int size = 0;
    int capacity;

    Node* head;
    Node* tail;
    unordered_map<int, Node*> cache;

public:
    /**
     * lru design
     * @param operators int整型vector<vector<>> the ops
     * @param k int整型 the k
     * @return int整型vector
     */
    vector<int>
    LRU(vector<vector<int>>& operators, int k)
    {
        capacity = k;
        size = 0;
        head = new Node(0, 0);
        tail = new Node(0, 0);
        head->next = tail;
        tail->prev = head;

        vector<int> res;

        for (vector<int> op : operators) {
            if (op[0] == 1) {
                set(op[1], op[2]);
            } else if (op[0] == 2) {
                int value = get(op[1]);
                res.push_back(value);
            }
        }

        return res;
    }

    void addHead(Node* node)
    {
        node->next = head->next;
        node->prev = head;
        node->next->prev = node;
        head->next = node;
    }

    Node* removeTail()
    {
        Node* node = tail->prev;
        removeNode(node);
        return node;
    }

    void removeNode(Node* node)
    {
        node->prev->next = node->next;
        node->next->prev = node->prev;
    }

    void moveHead(Node* node)
    {
        removeNode(node);
        addHead(node);
    }

    void set(int key, int val)
    {
        // 没找到
        if (cache.find(key) == cache.end()) {
            Node* node = new Node(key, val);
            cache[key] = node;

            addHead(node);
            size += 1;
            if (size > capacity) {
                Node* node = removeTail();
                cache.erase(node->key);
                delete node;
                size -= 1;
            }
        } else {
            Node* node = cache[key];
            node->value = val;
            moveHead(node);
        }
    }

    int get(int key)
    {
        // 没找到
        if (cache.find(key) == cache.end()) {
            return -1;
        } else {
            Node* node = cache[key];
            moveHead(node);
            return node->value;
        }
    }
};