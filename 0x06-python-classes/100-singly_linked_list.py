#!/usr/bin/python3
"""
    This module contains two classes that implements a linked list in python

    - a  Node class that implememts a node in a list
    - a  Singly_linked_list class that implements a singly linked lists
"""


class Node:
    """
    This class definition of a singly linked list

    """
    def __init__(self, data, next_node=None):
        """
        Initializes the square
        Args:
            data(int), next_node
        Methods:
            __init__, __str__
        Returns:
            None
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        data getter
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        data setter
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        next_node getter
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        next_node setter
        """
        if type(value) is Node or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_Node must be a Node object")

    def __str__(self):
        """
        string representation of class Node
        """
        return str(self.__data)


class SinglyLinkedList:
    """
    Definition of a Singly linked list Using the Node class above

    Methods:
            sorted_insert, __init__, __str__
    """
    def __init__(self):
        """Initializes with a head Node"""
        self.__head = None

    def sorted_insert(self, value):
        """
        Gives a sorted representation of the singly linked list
        Arguments: value
        Return: None
        """
        new = Node(value)
        tmp = self.__head
        if tmp is None or tmp.data >= value:
            if tmp:
                new.next_node = tmp
            self.__head = new
            return
        while tmp.next_node is not None:
            if tmp.next_node.data >= value:
                break
            tmp = tmp.next_node
        new.next_node = tmp.next_node
        tmp.next_node = new

    def __str__(self):
        """
        String representation of Singly linked list

        Return:
            Returns a formatted string output
        """
        rep = ""
        tmp = self.__head
        while tmp is not None:
            rep += tmp.__str__()
            if tmp.next_node is not None:
                rep += '\n'
            tmp = tmp.next_node
        return rep
