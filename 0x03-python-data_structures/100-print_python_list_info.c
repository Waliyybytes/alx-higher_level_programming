#include "Python.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * print_python_list_info - print info on python list
 * @p: PyObject
 * Return: Nothing
 */

void print_python_list_info(PyObject *p)
{
	PyListObject *list;
	int size, i = 0;
	PyOject *obj;

	list = (PyListObject *)p;
	size = PyList_Size(p);
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	while (i < size)
	{
		obj = list->ob_item[i];
		type = obj->ob_type;
		printf("Element %d: %s\n", i, type->tp_name);
		i++;
	}
}

