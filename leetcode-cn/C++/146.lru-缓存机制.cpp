/*
 * @lc app=leetcode.cn id=146 lang=cpp
 *
 * [146] LRU 缓存机制
 */

// @lc code=start
#include <unordered_map>
using namespace std;

struct DListNode
{
    DListNode *pre;
    DListNode *next;
    int val;
    int key;
};

class LRUCache
{
public:
    unordered_map<int, DListNode *> mem;
    int capacity = 0;
    int size = 0;
    DListNode *head;
    DListNode *tail;

    LRUCache(int capacity)
    {
        this->capacity = capacity;

        head = new DListNode();
        tail = new DListNode();
        head->next = tail;
        tail->pre = head;
    }

    void deleteNode(DListNode *node)
    {
        node->pre->next = node->next;
        node->next->pre = node->pre;

        node->pre = nullptr;
        node->next = nullptr;
    }

    void move2head(DListNode *node)
    {
        node->next = head->next;
        head->next->pre = node;

        head->next = node;
        node->pre = head;
    }

    int get(int key)
    {
        if (mem.count(key))
        {
            DListNode *node = mem[key];
            deleteNode(node);
            move2head(node);
            return node->val;
        }
        else
        {
            return -1;
        }
    }

    void put(int key, int value)
    {
        if (mem.count(key))
        {
            DListNode *node = mem[key];
            node->val = value;
            deleteNode(node);
            move2head(node);
        }
        else
        {
            if (size == capacity)
            {
                DListNode *node = tail->pre;
                deleteNode(node);
                mem.erase(node->key);
                delete node;
                size--;
            }

            DListNode *new_node = new DListNode();
            new_node->val = value;
            new_node->key = key;
            mem[key] = new_node;

            move2head(new_node);
            size++;
        }
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
// @lc code=end
