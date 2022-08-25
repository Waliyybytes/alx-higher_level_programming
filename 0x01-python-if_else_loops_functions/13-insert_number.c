#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - if a singly list is a cycle
 * @list: list to check
 * Return: 1 for SUCCESS
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp;
	listint_t *current;

	temp = malloc(sizeof(listint_t));
    	if (temp == NULL)
        	return (NULL);
        	       
        temp->n = number;
	temp->next = NULL;
	if ((*head) == NULL)
	{
		*head = temp;
		return (*head);
	}
	if (temp->n < (*head)->n)	
	{
		temp->next = (*head);
		(*head) = temp;
		return (*head);
	}
	
	current = *head;
	while (current->next != NULL)
	{
		
		if (number < current->next->n)
		{
			temp->next = current->next;
			current->next = temp;
			return (*head);	
		}
		current = current->next;
	}
	current->next = temp;
	return (*head);
}
