#include <Python.h>
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
	int size, i;
	PyObject *object;
	PyTypeObject *type;
	int alloc_size;

	list = (PyListObject *)p;
	size = PyList_Size(p);
	alloc_size = list->allocated;
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc_size);
	for (i = 0; i < size; i++)
	{
		object = PyList_GetItem(list, i);
		type = object->ob_type;
		printf("Element %d: %s\n", i, type->tp_name);
	}
}
