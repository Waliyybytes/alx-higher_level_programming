#include "Python.h"

/**
 * print_python_list_info - print info on python list
 * @p: PyObject
 * Return: Nothing
 */

void print_python_list_info(PyObject *p)
{
	PyListObject *list;
	Py_ssize_t size, i = 0;
	PyObject *obj;

	list = (PyListObject *)p;
	size = PyList_Size(list);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	while (i < size)
	{
		obj = PyList_GetItem(list, i);
		printf("Element %ld: %s\n", i, Py_Type(obj)->tp_name);
		i++;
	}
}
