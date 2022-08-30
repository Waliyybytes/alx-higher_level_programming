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
	Py_ssize_t size, i;
	PyObject *object;
	PyTypeObject *type;

	list = (PyListObject *)p;
	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (i = 0; i < size; i++)
	{
		object = PyList_GetItem(list, i);
		type = object->ob_type;
		printf("Element %ld: %s\n", i, type->tp_name);
	}
}
